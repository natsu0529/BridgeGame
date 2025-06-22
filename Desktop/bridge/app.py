import streamlit as st
import google.generativeai as genai
import os
import random
import json
from dotenv import load_dotenv
from typing import List, Dict, Any

# 環境変数を読み込み
load_dotenv()

# Gemini API設定
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.value = self._get_value()
    
    def _get_value(self):
        if self.rank in ['J', 'Q', 'K', 'A']:
            return {'J': 11, 'Q': 12, 'K': 13, 'A': 14}[self.rank]
        return int(self.rank)
    
    def __str__(self):
        return f"{self.rank}{self.suit}"
    
    def __repr__(self):
        return self.__str__()

class BridgeGame:
    def __init__(self):
        self.suits = ['♠', '♥', '♦', '♣']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = []
        self.players = {
            'Human': [],
            'North': [],
            'East': [],
            'South': []
        }
        self.current_round = 1
        self.max_rounds = 5
        self.scores = {'Human': 0, 'North': 0, 'East': 0, 'South': 0}
        self.current_trick = []
        self.trick_winner = None
        self.model = genai.GenerativeModel('gemini-pro')
        
    def create_deck(self):
        self.deck = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.deck)
    
    def deal_cards(self):
        self.create_deck()
        for i, card in enumerate(self.deck):
            player = list(self.players.keys())[i % 4]
            self.players[player].append(card)
    
    def get_ai_move(self, player_name: str, hand: List[Card], trick: List[Dict]) -> Card:
        """AIエージェントの行動を取得"""
        hand_str = ", ".join([str(card) for card in hand])
        trick_str = ", ".join([f"{play['player']}: {play['card']}" for play in trick])
        
        prompt = f"""
        あなたは{player_name}というブリッジプレイヤーです。
        現在の手札: {hand_str}
        現在のトリック: {trick_str}
        
        ブリッジのルールに従って、最適なカードを選択してください。
        手札からカードを1枚選んで、そのカードの文字列表現（例：A♠、K♥など）だけを返してください。
        他の説明は不要です。
        """
        
        try:
            response = self.model.generate_content(prompt)
            selected_card_str = response.text.strip()
            
            # 選択されたカードが手札にあるかチェック
            for card in hand:
                if str(card) == selected_card_str:
                    return card
            
            # AIが無効なカードを選んだ場合、ランダムに選択
            return random.choice(hand)
            
        except Exception as e:
            st.error(f"AI思考エラー ({player_name}): {e}")
            return random.choice(hand)
    
    def play_trick(self, human_card_index: int = None):
        """トリックをプレイ"""
        self.current_trick = []
        
        # 人間プレイヤーのターン
        if human_card_index is not None:
            human_card = self.players['Human'][human_card_index]
            self.current_trick.append({'player': 'Human', 'card': str(human_card)})
            self.players['Human'].pop(human_card_index)
        
        # AIプレイヤーのターン
        for ai_player in ['North', 'East', 'South']:
            if self.players[ai_player]:
                ai_card = self.get_ai_move(ai_player, self.players[ai_player], self.current_trick)
                self.current_trick.append({'player': ai_player, 'card': str(ai_card)})
                self.players[ai_player].remove(ai_card)
        
        # トリック勝者を決定（簡単な実装）
        self.trick_winner = random.choice(['Human', 'North', 'East', 'South'])
        self.scores[self.trick_winner] += 1
    
    def is_round_complete(self):
        return all(len(hand) == 0 for hand in self.players.values())
    
    def next_round(self):
        if self.current_round < self.max_rounds:
            self.current_round += 1
            self.deal_cards()
            return True
        return False

def main():
    st.set_page_config(page_title="Contract Bridge Game", page_icon="🃏", layout="wide")
    
    st.title("🃏 Contract Bridge - マルチエージェント版")
    st.markdown("---")
    
    # ゲーム状態の初期化
    if 'game' not in st.session_state:
        st.session_state.game = BridgeGame()
        st.session_state.game.deal_cards()
        st.session_state.game_started = True
    
    game = st.session_state.game
    
    # ゲーム情報表示
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("現在のラウンド", f"{game.current_round}/{game.max_rounds}")
    
    with col2:
        st.metric("あなたのスコア", game.scores['Human'])
    
    with col3:
        if st.button("新しいゲーム"):
            st.session_state.game = BridgeGame()
            st.session_state.game.deal_cards()
            st.rerun()
    
    # スコアボード
    st.subheader("📊 スコアボード")
    score_cols = st.columns(4)
    players = ['Human', 'North', 'East', 'South']
    for i, player in enumerate(players):
        with score_cols[i]:
            st.metric(player, game.scores[player])
    
    # 現在のトリック表示
    if game.current_trick:
        st.subheader("🎯 現在のトリック")
        trick_cols = st.columns(len(game.current_trick))
        for i, play in enumerate(game.current_trick):
            with trick_cols[i]:
                st.write(f"**{play['player']}**")
                st.write(f"🃏 {play['card']}")
    
    # プレイヤーの手札表示
    if game.players['Human']:
        st.subheader("🎴 あなたの手札")
        hand_cols = st.columns(len(game.players['Human']))
        
        selected_card = None
        for i, card in enumerate(game.players['Human']):
            with hand_cols[i]:
                if st.button(f"🃏 {card}", key=f"card_{i}"):
                    selected_card = i
        
        # カードが選択された場合
        if selected_card is not None:
            game.play_trick(selected_card)
            st.success(f"トリック完了！勝者: {game.trick_winner}")
            
            # ラウンド完了チェック
            if game.is_round_complete():
                if game.next_round():
                    st.success(f"ラウンド {game.current_round-1} 完了！次のラウンドを開始します。")
                else:
                    st.success("🎉 ゲーム終了！")
                    
                    # 最終結果
                    st.subheader("🏆 最終結果")
                    winner = max(game.scores.items(), key=lambda x: x[1])
                    st.success(f"勝者: {winner[0]} (スコア: {winner[1]})")
                    
                    if st.button("新しいゲームを開始"):
                        st.session_state.game = BridgeGame()
                        st.session_state.game.deal_cards()
                        st.rerun()
            
            st.rerun()
    
    # 他のプレイヤーの手札数表示
    st.subheader("👥 他のプレイヤー")
    other_cols = st.columns(3)
    other_players = ['North', 'East', 'South']
    for i, player in enumerate(other_players):
        with other_cols[i]:
            st.write(f"**{player}**")
            st.write(f"カード数: {len(game.players[player])}")
    
    # ゲームルール
    with st.expander("📖 ゲームルール"):
        st.markdown("""
        ### Contract Bridge ルール
        
        1. **プレイヤー**: あなた + 3人のAIエージェント (North, East, South)
        2. **ラウンド数**: 5ラウンド
        3. **カード配布**: 各ラウンドで全プレイヤーに13枚ずつ配布
        4. **トリック**: 各プレイヤーが1枚ずつカードを出してトリックを構成
        5. **得点**: トリックを取ったプレイヤーが1点獲得
        6. **勝利条件**: 5ラウンド終了時に最も多くの点数を獲得したプレイヤーが勝利
        
        ### 操作方法
        - 手札からカードをクリックして選択
        - AIプレイヤーが自動的に最適な手を選択
        - 各トリックの勝者が決定され、スコアが更新されます
        """)

if __name__ == "__main__":
    main()
