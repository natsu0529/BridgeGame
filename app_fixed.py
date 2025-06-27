import streamlit as st
import google.generativeai as genai
import os
import random
import json
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional

# 環境変数を読み込み
load_dotenv()

# Gemini API設定
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def format_card_display(card):
    """カードを色付きで表示するためのHTML形式に変換"""
    if isinstance(card, str):
        # 文字列の場合、スートを検出して色付け
        if '♥' in card or '♦' in card:
            # ハートまたはダイヤが含まれている場合
            for suit in ['♥', '♦']:
                if suit in card:
                    card = card.replace(suit, f"<span style='color: red;'>{suit}</span>")
        return card
    else:
        # Cardオブジェクトの場合
        if card.suit in ['♥', '♦']:
            return f"{card.rank}<span style='color: red;'>{card.suit}</span>"
        return f"{card.rank}{card.suit}"

class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.value = self._get_value()
    
    def _get_value(self):
        """カードの数値（2-14、Aは14）"""
        if self.rank in ['J', 'Q', 'K', 'A']:
            return {'J': 11, 'Q': 12, 'K': 13, 'A': 14}[self.rank]
        return int(self.rank)
    
    def get_suit_rank(self):
        """スートの強さ（♠=4, ♥=3, ♦=2, ♣=1）"""
        return {'♠': 4, '♥': 3, '♦': 2, '♣': 1}[self.suit]
    
    def compare_for_partnership(self, other):
        """パートナー決定時の比較（カード強さ → スート強さ）"""
        if self.value != other.value:
            return self.value - other.value
        return self.get_suit_rank() - other.get_suit_rank()
    
    def __str__(self):
        return f"{self.rank}{self.suit}"
    
    def __repr__(self):
        return self.__str__()

class BridgeGame:
    def __init__(self):
        self.suits = ['♠', '♥', '♦', '♣']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = []
        
        # プレイヤー（North-South vs East-West）
        self.players = {
            'North': [],
            'South': [],  # Humanプレイヤー
            'East': [],
            'West': []
        }
        self.partnerships = {
            'NS': ['North', 'South'],
            'EW': ['East', 'West']
        }
        
        # ゲーム状態
        self.current_round = 1
        self.max_rounds = 5
        self.round_scores = []  # 各ラウンドのスコア
        self.total_scores = {'NS': 0, 'EW': 0}
        
        # オークション関連
        self.auction_phase = True
        self.auction_history = []
        self.dealer = 'South'  # Humanから開始
        self.current_bidder = 'South'
        self.pass_count = 0
        self.contract = None
        self.declarer = None
        self.dummy = None
        self.trump_suit = None
        self.contract_level = 0
        self.doubled = 0  # 0=なし, 1=ダブル, 2=リダブル
        
        # プレイ関連
        self.play_phase = False
        self.tricks = []
        self.current_trick = []
        self.trick_leader = None
        self.dummy_revealed = False
        self.vulnerability = {'NS': False, 'EW': False}  # バルネラビリティ
        
        self.create_deck()
        self.deal_cards()
    
    def create_deck(self):
        """デッキを作成"""
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank))
        random.shuffle(self.deck)
    
    def deal_cards(self):
        """カードを配る（各プレイヤーに13枚）"""
        players_order = ['North', 'East', 'South', 'West']
        for i, card in enumerate(self.deck):
            player = players_order[i % 4]
            self.players[player].append(card)
        
        # 各プレイヤーの手札をソート
        for player in self.players:
            self.players[player].sort(key=lambda x: (x.suit, -x.value))
    
    def get_next_player(self, current_player):
        """次のプレイヤーを取得（時計回り：South→West→North→East）"""
        order = ['South', 'West', 'North', 'East']
        current_index = order.index(current_player)
        return order[(current_index + 1) % 4]
    
    def is_valid_bid(self, bid):
        """ビッドが有効かチェック"""
        if bid in ['Pass', 'Double', 'Redouble']:
            return True
        
        # レベルとスートの形式チェック
        if len(bid) < 2:
            return False
        
        try:
            level = int(bid[0])
            suit = bid[1:]
            
            if level < 1 or level > 7:
                return False
            
            if suit not in ['♣', '♦', '♥', '♠', 'NT']:
                return False
            
            # 現在のコントラクトより高いビッドかチェック
            if self.auction_history:
                last_non_pass = None
                for bid_info in reversed(self.auction_history):
                    if bid_info['bid'] not in ['Pass', 'Double', 'Redouble']:
                        last_non_pass = bid_info['bid']
                        break
                
                if last_non_pass:
                    last_level = int(last_non_pass[0])
                    last_suit = last_non_pass[1:]
                    suit_order = ['♣', '♦', '♥', '♠', 'NT']
                    
                    if level < last_level:
                        return False
                    elif level == last_level:
                        if suit_order.index(suit) <= suit_order.index(last_suit):
                            return False
            
            return True
        except:
            return False
    
    def make_bid(self, player, bid):
        """ビッドを行う"""
        if bid == 'Pass':
            self.pass_count += 1
        else:
            self.pass_count = 0
            
            if bid == 'Double':
                self.doubled = 1
            elif bid == 'Redouble':
                self.doubled = 2
            else:
                # 通常のビッド
                self.contract_level = int(bid[0])
                self.trump_suit = bid[1:]
                self.declarer = player
                self.doubled = 0
        
        self.auction_history.append({
            'player': player,
            'bid': bid
        })
        
        # オークション終了判定
        if self.pass_count >= 3 and len(self.auction_history) >= 4:
            self.end_auction()
        else:
            self.current_bidder = self.get_next_player(self.current_bidder)
    
    def end_auction(self):
        """オークション終了"""
        self.auction_phase = False
        
        if self.declarer:
            # ダミーを決定（ディクレアラーのパートナー）
            if self.declarer in self.partnerships['NS']:
                partner = [p for p in self.partnerships['NS'] if p != self.declarer][0]
            else:
                partner = [p for p in self.partnerships['EW'] if p != self.declarer][0]
            
            self.dummy = partner
            self.contract = f"{self.contract_level}{self.trump_suit}"
            
            # プレイフェーズ開始
            self.play_phase = True
            self.trick_leader = self.get_next_player(self.declarer)  # ディクレアラーの左隣がリード
    
    def is_valid_play(self, player, card):
        """カードプレイが有効かチェック"""
        if not self.current_trick:
            return True  # 最初のカードは何でもOK
        
        lead_suit = self.current_trick[0]['card'].suit
        player_hand = self.players[player]
        
        # リードスートがある場合はフォローマスト
        if card.suit != lead_suit:
            # フォローできるカードがあるかチェック
            has_lead_suit = any(c.suit == lead_suit for c in player_hand)
            if has_lead_suit:
                return False
        
        return True
    
    def play_card(self, player, card):
        """カードをプレイ"""
        self.current_trick.append({
            'player': player,
            'card': card
        })
        
        # 手札からカードを削除
        self.players[player].remove(card)
        
        # ダミー公開（最初のトリック）
        if len(self.current_trick) == 1 and not self.dummy_revealed:
            self.dummy_revealed = True
        
        # トリック完了判定
        if len(self.current_trick) == 4:
            self.complete_trick()
    
    def complete_trick(self):
        """トリック完了"""
        # 勝者を決定
        winner = self.determine_trick_winner()
        
        self.tricks.append({
            'cards': self.current_trick.copy(),
            'winner': winner
        })
        
        self.current_trick = []
        self.trick_leader = winner
        
        # ゲーム終了判定
        if len(self.tricks) == 13:
            self.end_round()
    
    def determine_trick_winner(self):
        """トリックの勝者を決定"""
        if not self.current_trick:
            return None
        
        lead_suit = self.current_trick[0]['card'].suit
        trump_suit = self.trump_suit if self.trump_suit != 'NT' else None
        
        best_card = None
        winner = None
        
        for play in self.current_trick:
            card = play['card']
            player = play['player']
            
            if best_card is None:
                best_card = card
                winner = player
            else:
                # トランプ vs 非トランプ
                if trump_suit and card.suit == trump_suit and best_card.suit != trump_suit:
                    best_card = card
                    winner = player
                elif trump_suit and best_card.suit == trump_suit and card.suit != trump_suit:
                    continue
                # 同じスートの場合は強さで比較
                elif card.suit == best_card.suit:
                    if card.value > best_card.value:
                        best_card = card
                        winner = player
                # リードスートの場合
                elif card.suit == lead_suit and best_card.suit != lead_suit and (not trump_suit or best_card.suit != trump_suit):
                    best_card = card
                    winner = player
        
        return winner
    
    def calculate_score(self):
        """スコア計算"""
        if not self.contract:
            return {'NS': 0, 'EW': 0}
        
        # 取ったトリック数を計算
        ns_tricks = sum(1 for trick in self.tricks if trick['winner'] in ['North', 'South'])
        ew_tricks = sum(1 for trick in self.tricks if trick['winner'] in ['East', 'West'])
        
        # ディクレアラーのパートナーシップが取ったトリック数
        if self.declarer in ['North', 'South']:
            declarer_tricks = ns_tricks
            declarer_partnership = 'NS'
        else:
            declarer_tricks = ew_tricks
            declarer_partnership = 'EW'
        
        required_tricks = 6 + self.contract_level
        made_contract = declarer_tricks >= required_tricks
        
        if made_contract:
            # コントラクト成功
            base_score = 0
            
            # 基本点
            if self.trump_suit == 'NT':
                base_score = 40 + (self.contract_level - 1) * 30
            elif self.trump_suit in ['♠', '♥']:  # メジャースート
                base_score = self.contract_level * 30
            else:  # マイナースート
                base_score = self.contract_level * 20
            
            # ダブル/リダブル
            if self.doubled == 1:
                base_score *= 2
            elif self.doubled == 2:
                base_score *= 4
            
            # オーバートリック
            overtricks = declarer_tricks - required_tricks
            overtrick_score = 0
            if overtricks > 0:
                if self.doubled == 0:
                    if self.trump_suit in ['♠', '♥', 'NT']:
                        overtrick_score = overtricks * 30
                    else:
                        overtrick_score = overtricks * 20
                else:
                    # ダブル時のオーバートリック
                    overtrick_score = overtricks * (200 if self.vulnerability[declarer_partnership] else 100)
                    if self.doubled == 2:
                        overtrick_score *= 2
            
            # ボーナス
            bonus = 0
            if base_score >= 100:  # ゲーム
                bonus += 500 if self.vulnerability[declarer_partnership] else 300
            else:  # パートゲーム
                bonus += 50
            
            if self.doubled > 0:
                bonus += 50  # ダブルボーナス
            
            # グランドスラム・スモールスラム
            if self.contract_level == 7:  # グランドスラム
                bonus += 1500 if self.vulnerability[declarer_partnership] else 1000
            elif self.contract_level == 6:  # スモールスラム
                bonus += 750 if self.vulnerability[declarer_partnership] else 500
            
            total_score = base_score + overtrick_score + bonus
            
            if declarer_partnership == 'NS':
                return {'NS': total_score, 'EW': 0}
            else:
                return {'NS': 0, 'EW': total_score}
        
        else:
            # コントラクト失敗
            undertricks = required_tricks - declarer_tricks
            penalty = 0
            
            if self.doubled == 0:
                # 通常のペナルティ
                penalty = undertricks * (100 if self.vulnerability[declarer_partnership] else 50)
            else:
                # ダブル時のペナルティ
                if self.vulnerability[declarer_partnership]:
                    # バルネラブル
                    penalties = [200, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300]
                else:
                    # ノンバルネラブル
                    penalties = [100, 200, 200, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300]
                
                penalty = sum(penalties[:undertricks])
                
                if self.doubled == 2:
                    penalty *= 2
            
            defending_partnership = 'EW' if declarer_partnership == 'NS' else 'NS'
            
            if declarer_partnership == 'NS':
                return {'NS': -penalty, 'EW': penalty}
            else:
                return {'NS': penalty, 'EW': -penalty}
    
    def end_round(self):
        """ラウンド終了"""
        scores = self.calculate_score()
        self.round_scores.append(scores)
        self.total_scores['NS'] += scores['NS']
        self.total_scores['EW'] += scores['EW']
    
    def next_round(self):
        """次のラウンドへ"""
        if self.current_round < self.max_rounds:
            self.current_round += 1
            
            # ディーラーローテーション
            dealer_order = ['South', 'West', 'North', 'East']
            current_dealer_index = dealer_order.index(self.dealer)
            self.dealer = dealer_order[(current_dealer_index + 1) % 4]
            
            # バルネラビリティ設定
            if self.current_round in [2, 5]:
                self.vulnerability['NS'] = True
            if self.current_round in [3, 5]:
                self.vulnerability['EW'] = True
            
            # ゲーム状態リセット
            self.auction_phase = True
            self.auction_history = []
            self.current_bidder = self.dealer
            self.pass_count = 0
            self.contract = None
            self.declarer = None
            self.dummy = None
            self.trump_suit = None
            self.contract_level = 0
            self.doubled = 0
            self.play_phase = False
            self.tricks = []
            self.current_trick = []
            self.trick_leader = None
            self.dummy_revealed = False
            
            # 新しいデッキで配り直し
            self.create_deck()
            self.deal_cards()
            
            return True
        return False

class AIPlayer:
    def __init__(self, name: str, game: BridgeGame):
        self.name = name
        self.game = game
        self.model = genai.GenerativeModel('gemini-pro')
    
    def make_bid(self):
        """AIプレイヤーがビッドを行う"""
        try:
            # 現在の手札を文字列に変換
            hand_str = ', '.join([str(card) for card in self.game.players[self.name]])
            
            # オークション履歴を文字列に変換
            auction_str = ""
            if self.game.auction_history:
                auction_str = "\n".join([f"{bid['player']}: {bid['bid']}" for bid in self.game.auction_history])
            
            prompt = f"""
あなたは契約ブリッジのAIプレイヤー「{self.name}」です。
現在の手札: {hand_str}
オークション履歴:
{auction_str}

次のルールに従ってビッドしてください：
1. Pass, Double, Redouble, または 1♣ から 7NT までの正しいビッド
2. 前のビッドより高いレベル・スートでなければならない
3. スートの強さ: ♣ < ♦ < ♥ < ♠ < NT
4. 手札の強さとバランスを考慮
5. パートナーとの連携を考慮

ビッドのみを答えてください（例：「1♠」「Pass」「Double」）。
"""
            
            response = self.model.generate_content(prompt)
            bid = response.text.strip()
            
            # ビッドの妥当性チェック
            if not self.game.is_valid_bid(bid):
                return "Pass"
            
            return bid
            
        except Exception as e:
            return "Pass"
    
    def play_card(self):
        """AIプレイヤーがカードをプレイ"""
        try:
            available_cards = self.game.players[self.name]
            if not available_cards:
                return None
            
            # 現在の手札
            hand_str = ', '.join([str(card) for card in available_cards])
            
            # 現在のトリック
            trick_str = ""
            if self.game.current_trick:
                trick_str = ", ".join([f"{play['player']}: {play['card']}" for play in self.game.current_trick])
            
            # 既に完了したトリック
            completed_tricks_str = ""
            if self.game.tricks:
                completed_tricks_str = f"\n完了したトリック数: {len(self.game.tricks)}"
            
            prompt = f"""
あなたは契約ブリッジのAIプレイヤー「{self.name}」です。
コントラクト: {self.game.contract}
ディクレアラー: {self.game.declarer}
ダミー: {self.game.dummy}
トランプ: {self.game.trump_suit}

現在の手札: {hand_str}
現在のトリック: {trick_str}
{completed_tricks_str}

以下のルールに従ってカードをプレイしてください：
1. リードスートがある場合はフォローマスト
2. ない場合はトランプまたは任意のカードをプレイ可能
3. パートナーシップの利益を最大化
4. ディクレアラーの場合はコントラクト達成を目指す
5. ディフェンダーの場合はコントラクト阻止を目指す

プレイするカードを「ランク+スート」形式で答えてください（例：「A♠」「K♥」）。
"""
            
            response = self.model.generate_content(prompt)
            card_str = response.text.strip()
            
            # カードを検索
            for card in available_cards:
                if str(card) == card_str or f"{card.rank}{card.suit}" == card_str:
                    if self.game.is_valid_play(self.name, card):
                        return card
            
            # 有効なカードが見つからない場合、最初の有効なカードを返す
            for card in available_cards:
                if self.game.is_valid_play(self.name, card):
                    return card
            
            return available_cards[0] if available_cards else None
            
        except Exception as e:
            # エラーの場合、最初の有効なカードを返す
            available_cards = self.game.players[self.name]
            for card in available_cards:
                if self.game.is_valid_play(self.name, card):
                    return card
            return available_cards[0] if available_cards else None

def display_game_state(game: BridgeGame):
    """ゲーム状態を表示"""
    # ラウンド情報
    st.sidebar.subheader(f"🎯 ラウンド {game.current_round}/{game.max_rounds}")
    
    # スコア表示
    st.sidebar.subheader("📊 スコア")
    st.sidebar.write(f"**North-South**: {game.total_scores['NS']}")
    st.sidebar.write(f"**East-West**: {game.total_scores['EW']}")
    
    # バルネラビリティ
    vuln_ns = "🔴" if game.vulnerability['NS'] else "⚪"
    vuln_ew = "🔴" if game.vulnerability['EW'] else "⚪"
    st.sidebar.write(f"**Vulnerability**: NS{vuln_ns} EW{vuln_ew}")
    
    # ディーラー情報
    st.sidebar.write(f"**ディーラー**: {game.dealer}")
    
    if not game.auction_phase:
        # コントラクト情報
        if game.contract:
            st.sidebar.subheader("📋 コントラクト")
            double_str = ""
            if game.doubled == 1:
                double_str = " (ダブル)"
            elif game.doubled == 2:
                double_str = " (リダブル)"
            st.sidebar.write(f"**{game.contract}{double_str}**")
            st.sidebar.write(f"**ディクレアラー**: {game.declarer}")
            st.sidebar.write(f"**ダミー**: {game.dummy}")
            st.sidebar.write(f"**取ったトリック**: {len([t for t in game.tricks if t.get('winner') in game.partnerships['NS']])}/13 (NS)")

def display_auction(game: BridgeGame):
    """オークション表示"""
    st.subheader("🎪 オークション")
    
    if game.auction_history:
        cols = st.columns(4)
        headers = ['South', 'West', 'North', 'East']
        for i, header in enumerate(headers):
            with cols[i]:
                st.write(f"**{header}**")
        
        # ディーラーから開始するようにオフセット計算
        dealer_offset = headers.index(game.dealer)
        
        # ビッド履歴を4列に配置
        rows = []
        current_row = [''] * 4
        
        for i, bid_info in enumerate(game.auction_history):
            player_index = (headers.index(bid_info['player']) - dealer_offset) % 4
            row_index = i // 4
            
            if row_index >= len(rows):
                rows.append([''] * 4)
            
            actual_player_index = (player_index + dealer_offset) % 4
            rows[row_index][actual_player_index] = bid_info['bid']
        
        # 各行を表示
        for row in rows:
            cols = st.columns(4)
            for i, bid in enumerate(row):
                with cols[i]:
                    if bid:
                        st.write(bid)
    
    # 現在のビッダー表示
    if game.auction_phase:
        st.write(f"**現在のビッダー**: {game.current_bidder}")

def display_hands(game: BridgeGame):
    """手札表示"""
    # Southの手札（人間プレイヤー）
    st.subheader("🎴 あなたの手札 (South)")
    if game.players['South']:
        hand_cols = st.columns(min(len(game.players['South']), 13))
        for i, card in enumerate(game.players['South']):
            with hand_cols[i]:
                st.markdown(f"🃏 {format_card_display(card)}", unsafe_allow_html=True)
    
    # ダミーの手札表示（プレイフェーズで公開された後）
    if game.dummy_revealed and game.dummy:
        st.subheader(f"🎭 {game.dummy}の手札（ダミー）")
        dummy_cols = st.columns(min(len(game.players[game.dummy]), 13))
        for i, card in enumerate(game.players[game.dummy]):
            with dummy_cols[i]:
                st.markdown(f"🃏 {format_card_display(card)}", unsafe_allow_html=True)
    
    # 現在のトリック表示
    if game.current_trick:
        st.subheader("🎯 現在のトリック")
        trick_cols = st.columns(len(game.current_trick))
        for i, play in enumerate(game.current_trick):
            with trick_cols[i]:
                st.write(f"**{play['player']}**")
                st.markdown(f"🃏 {format_card_display(play['card'])}", unsafe_allow_html=True)

def display_play_phase(game: BridgeGame):
    """プレイフェーズの表示"""
    st.subheader("🎮 カードプレイ")
    
    # 現在のプレイヤー
    if game.current_trick:
        next_player = game.get_next_player(game.current_trick[-1]['player'])
    else:
        next_player = game.trick_leader
    
    if len(game.current_trick) < 4:
        st.write(f"**次のプレイヤー**: {next_player}")
    
    # 人間プレイヤーのターン
    if next_player == 'South' and len(game.current_trick) < 4:
        st.write("**あなたのターンです。プレイするカードを選択してください：**")
        
        # プレイ可能なカードのみ表示
        playable_cards = []
        for card in game.players['South']:
            if game.is_valid_play('South', card):
                playable_cards.append(card)
        
        if playable_cards:
            cols = st.columns(min(len(playable_cards), 13))
            for i, card in enumerate(playable_cards):
                with cols[i]:
                    if st.button(f"🃏 {format_card_display(card)}", key=f"play_card_{i}", help="クリックしてカードをプレイ"):
                        game.play_card('South', card)
                        st.success(f"{format_card_display(card)} をプレイしました")
                        st.rerun()

def main():
    st.set_page_config(
        page_title="Contract Bridge",
        page_icon="🃏",
        layout="wide"
    )
    
    st.title("🃏 Contract Bridge")
    st.write("人間 vs AI の本格的な契約ブリッジゲーム")
    
    # ゲーム状態の初期化
    if 'game' not in st.session_state:
        st.session_state.game = BridgeGame()
        st.session_state.ai_players = {
            'North': AIPlayer('North', st.session_state.game),
            'East': AIPlayer('East', st.session_state.game),
            'West': AIPlayer('West', st.session_state.game)
        }
    
    game = st.session_state.game
    ai_players = st.session_state.ai_players
    
    # ゲーム状態表示
    display_game_state(game)
    
    # ラウンド終了判定
    if len(game.tricks) == 13:
        st.subheader("🏁 ラウンド終了")
        
        # スコア表示
        if game.round_scores:
            last_score = game.round_scores[-1]
            st.write(f"**ラウンド {game.current_round} スコア**:")
            st.write(f"North-South: {last_score['NS']}")
            st.write(f"East-West: {last_score['EW']}")
        
        # 次のラウンドボタン
        if game.current_round < game.max_rounds:
            if st.button("次のラウンドへ"):
                game.next_round()
                st.rerun()
        else:
            st.subheader("🎉 ゲーム終了")
            if game.total_scores['NS'] > game.total_scores['EW']:
                st.write("**North-South の勝利！**")
            elif game.total_scores['EW'] > game.total_scores['NS']:
                st.write("**East-West の勝利！**")
            else:
                st.write("**引き分け！**")
            
            if st.button("新しいゲームを開始"):
                st.session_state.game = BridgeGame()
                st.session_state.ai_players = {
                    'North': AIPlayer('North', st.session_state.game),
                    'East': AIPlayer('East', st.session_state.game),
                    'West': AIPlayer('West', st.session_state.game)
                }
                st.rerun()
        return
    
    # オークションフェーズ
    if game.auction_phase:
        display_auction(game)
        display_hands(game)
        
        # ビッド処理
        if game.current_bidder == 'South':
            st.subheader("🎯 ビッド選択")
            
            # ビッドオプション
            bid_options = ['Pass']
            
            # 通常のビッド（1♣ から 7NT まで）
            suits = ['♣', '♦', '♥', '♠', 'NT']
            for level in range(1, 8):
                for suit in suits:
                    bid = f"{level}{suit}"
                    if game.is_valid_bid(bid):
                        bid_options.append(bid)
            
            # Double/Redouble
            if game.auction_history:
                last_bid = game.auction_history[-1]['bid']
                if last_bid not in ['Pass', 'Double', 'Redouble']:
                    if game.doubled == 0:
                        bid_options.append('Double')
                    elif game.doubled == 1:
                        bid_options.append('Redouble')
            
            # ビッド選択UI
            cols = st.columns(min(len(bid_options), 8))
            for i, bid in enumerate(bid_options):
                with cols[i % 8]:
                    if st.button(bid, key=f"bid_{bid}"):
                        game.make_bid('South', bid)
                        st.rerun()
        
        else:
            # AIプレイヤーのビッド
            if st.button(f"{game.current_bidder} のビッドを実行"):
                ai_bid = ai_players[game.current_bidder].make_bid()
                game.make_bid(game.current_bidder, ai_bid)
                st.success(f"{game.current_bidder}: {ai_bid}")
                st.rerun()
    
    # プレイフェーズ
    elif game.play_phase:
        display_hands(game)
        display_play_phase(game)
        
        # AIプレイヤーのプレイ
        if game.current_trick:
            next_player = game.get_next_player(game.current_trick[-1]['player'])
        else:
            next_player = game.trick_leader
        
        if next_player != 'South' and len(game.current_trick) < 4:
            if st.button(f"{next_player} のプレイを実行"):
                ai_card = ai_players[next_player].play_card()
                if ai_card:
                    game.play_card(next_player, ai_card)
                    st.success(f"{next_player}: {format_card_display(ai_card)}")
                    st.rerun()

if __name__ == "__main__":
    main()
