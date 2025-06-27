import streamlit as st
import os
import random
import json
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional
# --- 強化された戦略的思考フレームワーク（AIプロンプト用・詳細版） ---
advanced_bridge_prompt = """
【ブリッジAI戦略ドキュメント（詳細・具体例付き）】
あなたはコントラクトブリッジの上級者として、以下の原則・戦略・人間的な思考パターンを常に意識して判断してください。

■ 基本原則
- パートナーとの協調・情報伝達（ビディング・プレイ）を重視する。
- 状況ごとに最善手を考え、安易な決め打ちや機械的な判断を避ける。
- すべての判断に「なぜその選択をするのか」という根拠を持つ。

■ ハンド評価・ビディング戦略
- HCP（High Card Point）だけでなく、配分点（分散点）、ロングスート・ショートスートの価値も加味して総合的に評価する。
- 例：ダブルフィットやシングルトン・ボイドの価値を積極的に評価。
- パートナーのビッド意図・意味（システムやコンベンション）を常に推測し、協力的な応答を心がける。
- 例：パートナーが1NTオープン→バランス型・15-17HCPと推測し、Staymanやトランスファーを活用。
- 競争的な場面では、犠牲ビッド・妨害ビッド・ダブル/リダブルの意図を明確に持つ。
- 例：敵が高いレベルで契約しそうな場合、妨害的に高めのビッドを検討。
- 人間らしい「迷い」や「バランス感覚」も再現し、常に最も合理的な選択肢だけでなく、時にリスクを取る判断も許容する。
- 直近のビディング履歴・パートナー/敵の傾向も考慮し、過去のビッドから相手の手の特徴を推理する。
- 例：敵が積極的にダブルを多用→攻撃的なスタイルと推測し、慎重な応札を心がける。
- 競りの途中で「パートナーの意図が不明瞭な場合」は、無理に高い契約を目指さず安全策を取る。
オークションの戦術：上級者への道
1. オープニングビッド：手札の「物語」を語る
オープニングビッドは、あなたの手札が持つ最も重要な情報をパートナーに伝える最初のチャンスです。単なるHCPの合計だけでなく、ハンドのシェイプ（形状）と各スートの品質を正確に伝える意識を持ちましょう。

1NTオープン (15-17HCP、バランスハンド):
これは非常に強力なオープニングです。パートナーに「私の手札はバランスが取れていて、主要なスートに致命的な弱点はない」という安心感を与えます。相手からの攻撃を予測しやすく、ノートランプゲームは点数が高いため、まずはこれを検討できるハンドを目指しましょう。

1メジャーオープン (1♥, 1♠):
HCPが12-21で、5枚以上の良質なメジャースートがある場合に行います。良質とは、トップランクのカード（A, K, Q）が含まれているか、枚数が多いことによるトリック確保の可能性が高いことを指します。メジャーゲームはパートスコアでも点数が高く、ゲームメイクの可能性も高いため、最優先で開示すべき情報です。パートナーが適切なサポートを見つければ、すぐにゲーム、あるいはスラムへと進む準備ができます。

1マイナーオープン (1♣, 1♦):
HCPが12-21で、メジャーのオープニングができない場合に行います。通常、4枚以上のマイナーを少なくとも1つ持っているか、メジャーが4-4でHCPが十分にある場合です。特に1クラブオープンは、バランスハンドでHCPが12-14の場合や、21HCP以上の非常に強いハンドを2クラブオープン（強制ビッド）の代わりに使う場合もあります（これはコンベンションによります）。マイナーオープニングは、ゲーム契約が達成しにくいものの、パートナーとの情報交換の足がかりとなります。

2クラブオープン (22HCP以上、または非常に強い片寄ったハンド):
これは**ゲームフォース（Game Forcing）**のビッドであり、パートナーは手札の強さに関わらず何らかの応答をしなければなりません。あなたのハンドがゲームを約束していることを明確に伝え、スラムの可能性を探るための出発点となります。

弱い2ビッド (2♥, 2♠, 2NT):
HCPは少ないが、非常に長い（6枚以上）で、良質なトップトリックが期待できるスートがある場合に行います。これはプリエンプティブビッドと呼ばれ、相手のオークションを妨害する目的が強いです。相手に適切なレベルでコントラクトを見つけさせないように、高いレベルでビッドすることで、相手に「高いリスクを負ってゲームを宣言するか、諦めるか」の選択を迫ります。パートナーには「少ないHCPだが、このスートだけは強い」と伝え、無理なゲーム追求を避けるよう促します。

2. パートナーのビッドへの応答：的確な情報交換
パートナーのオープニングビッドに対する応答は、あなたの手札とパートナーの手札の**「フィット（適合性）」**を見つけるための重要なステップです。

HCPとフィットの概念:
ブリッジでは、単なるHCPの合計だけでなく、パートナーのスートと自分のスートがどれだけ噛み合うか（フィット）が重要です。HCPが少なくても、フィットがあることでトリックが増えることがあります（フィットポイントやシェイプポイント）。

サポートビッド:
パートナーが宣言したスートに3枚以上あり、そのスートをトランペット（切り札）にするのが有効だと判断した場合、そのスートを宣言します。レベルを上げることで、自身のHCPの範囲を示します。例：パートナーが1♠と宣言し、自分に♠が4枚あり9HCPなら2♠。もし12HCP以上あれば、いきなり3♠や4♠と宣言してゲームを約束することも考えられます。

新しいスートの宣言:
パートナーのスートにフィットがなく、自分に5枚以上のスートがある場合に行います。この時、レベルの上げ方が重要です。より高いレベルで宣言するほど、より多くのHCPがあることを示します。

NTへの応答:
パートナーが1NTオープンした場合、あなたのHCPと手札の形状に応じて応答します。

パス: HCPが少ない（0-7HCP）場合。

2NT (8-9HCP): パートナーにゲームの可能性を示唆します。

3NT (10-12HCP): NTゲームへの到達を宣言します。

ジャコビー2NT（コンベンション）やステイマン（コンベンション）などの使用で、さらに詳細な情報を引き出します。

3. ディフェンシブビッド：相手のオークションをかく乱する
相手チームがオークションに参加してきた場合、あなたのビッドはディフェンシブビッドとなります。相手を妨害しつつ、パートナーに有益な情報を伝えることを目指します。

オーバーコール:
相手がビッドした後に、あなたが独立した5枚以上の良いスートと**十分なHCP（通常10HCP以上）**を持っている場合に行います。これはパートナーに、あなたのサイドにもゲームの可能性があり、ディフェンスにも自信があることを伝えます。ただし、オーバーコールしたスートでトリックを取れないと、大きなペナルティを受けるリスクもあります。

テイクアウトダブル:
相手のビッドに対して「ダブル」を宣言します。これは通常、あなたのHCPがオープニングハンドに匹敵し（12HCP以上）、相手の宣言したスートに短い（0～2枚）が、残りの3つのスートにバランスよくサポートがあることを示します。パートナーに「好きなスートを宣言してほしい」という明確なメッセージになります。相手をディフェンスで打ち負かす自信がある、または自分のサイドでゲームを達成する可能性を探るための強力なツールです。

競争ビッド:
相手チームとあなたのチームがゲームコントラクトを目指して競り合っている状況です。この時、「これはパートスコアの戦いなのか、ゲームの戦いなのか」を意識することが重要です。相手にゲームを達成させないために、あえて無理なレベルまでビッドするサクリファイスビッドも戦略の一つですが、その見極めは非常に難しいです。

4. スラムの探索：完璧なハンドの追求
非常に強いハンドを持った時、12トリックのスモールスラムや、13トリックのグランドスラムを目指すためのビッドは、まさにブリッジの醍醐味です。

強制ビッド（フォースイングビッド）の理解:
特定のビッドは、パートナーにパスを許さず、何らかの応答を強制します。これにより、オークションが途切れることなく、より詳細な情報交換が行われます。例えば、2クラブオープン後の応答、ジャンプビッド（通常のレベルを飛び越えて高いレベルで宣言する）などがこれにあたります。

エース・キングの確認（ブラックウッド、ガーバーなど）:
スラムを達成するためには、通常、トップトリック（エースやキング）の枚数が重要になります。ブラックウッドやガーバーといったコンベンションは、パートナーが持っているエースやキングの枚数を問い合わせるための決められたビッドシーケンスです。これにより、安全にスラムを宣言できるか、あるいはトップトリックが足りずに失敗するかを判断できます。

具体的なキュービッド:
相手のスートを宣言するなどして、特定のキーカードを持っているかを確認したり、セカンダリーコントロール（キング、クイーン、ジャックなど）の有無を伝えたりするビッドです。これは、スラムの安全性をさらに高めるための高度なテクニックです。

5. コンベンションの活用：共通言語の構築
上級者になるためには、パートナーとの間で**「コンベンション（約束事）」**を共有し、それらを適切に活用することが不可欠です。コンベンションは、限られたビッドの枠の中で、より多くの情報を交換するための「共通言語」です。

ステイマン: 1NTオープン後の2クラブビッドで、パートナーにメジャー4枚スーツの有無を問い合わせるコンベンション。

ジャコビー2NT: 1メジャーオープン後の2NTビッドで、パートナーにゲームフォースのフィットがあることを示すコンベンション。

トランスファー: 1NTオープン後、パートナーに特定のメジャーを強制的に宣言させることで、ディクレアラー（プレイする側）をコントロールするコンベンション。

その他の多くのコンベンション: スプリンター、ガブリエル、ライトナーなど、状況に応じた様々なコンベンションが存在します。これらを学ぶことで、あなたのオークションは格段に洗練されます。

■ プレイ戦略（デクレアラー）
- トリックプランを必ず立てる。危険スートの管理、エントリーの確保、フィネスの活用、スーツブレイクのタイミングを考える。
- 例：トランプコントロールが必要な場合、まずトランプを抜き切る。
- 例：フィネスが有効な場合、リスクとリターンを天秤にかけて実行。
- ダミーの手札を最大限活用し、エントリーの順序やスイッチを工夫する。
- 例：ダミーのAでエントリーし、手札のロングスートを伸ばす。
- 敵の守備シグナルや捨て札から分布・持ち札を推理し、プレイ順を調整する。
- 例：敵が特定スートを早めに捨てた→そのスートが短いと推測。
ブリッジのプレイにおいて上級者を目指すとのこと、素晴らしい目標ですね！オークションが「コントラクトを見つける対話」だとすれば、プレイは「コントラクトを実現する実践」です。高度な技術と洞察力が求められる、非常に奥深いフェーズです。

プレイの戦術：上級者への道のり
プレイには、**デクレアラープレイ（宣言者としてのプレイ）とディフェンスプレイ（守備としてのプレイ）**の2つの側面があり、どちらも極める必要があります。

1. デクレアラープレイ：コントラクト達成の指揮者
デクレアラー（宣言側）は、決められたコントラクトを達成する責任を負います。プレイを始める前に、徹底したプランニングが必要です。

初期プランニングの徹底

ルーザーズカウント (Losers Count): まず、手札にある失う可能性のあるトリック（ルーザー）の数を数えます。特に、切り札スートとサイドスート（切り札以外のスート）の両方でルーザーを見積もることが重要です。これがゲームの成功に必要なトリック数を明確にします。

トップトリックの確定 (Counting Top Tricks): エースやキングなど、確実に取れるトリックの数を数えます。これにより、足りないトリックをどこで補うかが見えてきます。

トリックの発展 (Developing Tricks): トップトリック以外でトリックを増やす方法を考えます。これは通常、より低いランクのカード（クイーン、ジャックなど）でトリックを取るために、相手のトップカードを抜く（フォースアウトする）ことを含みます。

フィネス (Finesse): 相手の持っているかもしれないトップカードを避けて、自分の低いカードでトリックを取るテクニックです。例えば、A-Qと持っていてKが相手にある場合、Qを出して相手のKを引かせ、その後Aでトリックを取る、といったことを指します。フィネスのリスクとリターンを常に評価しましょう。

ダミーのリソース評価: パートナー（ダミー）の手札が持つ価値を最大限に引き出すプランを立てます。ダミーのどのスートを伸ばすか、いつダミーにリードを渡すかなどを考えます。

切り札の管理 (Trump Management)

切り札の抜き方 (Drawing Trumps): コントラクトが切り札スートである場合、通常は相手から切り札を抜き切ることが最優先です。相手に切り札が残っていると、あなたのサイドスートが切り札で潰されてしまうリスクがあるからです。ただし、切り札をすぐに抜かない方が良い場合もあります（後述のクロストランプなど）。

切り札の配分 (Trump Distribution): 相手の切り札がどのように配分されているかを推測し、それに基づいてプレイを進めます。

切り札のタイミング (Timing of Trump Play): 切り札を抜くタイミングは非常に重要です。サイドスートのトリックを伸ばすために切り札を温存することもありますし、逆に早期に切り札を抜いて安全を確保することもあります。

リードとタイミングの調整 (Lead and Timing)

リードの重要性: どのスートからプレイを開始するか（オープニングリード）は、その後のゲーム展開を大きく左右します。ディクレアラーとして、自分のプランに沿って最適なスートをリードしましょう。

テンポ (Tempo): プレイの「テンポ」をコントロールします。例えば、相手にリードを渡すことで、相手に不利なスートからリードさせるといった戦略もあります。

ディスカードとスクイーズ (Discard and Squeeze)

ディスカード (Discard): 不要なカードを捨てることで、手札の形を整え、後続のトリックで有利になるようにします。相手のディスカードからも情報を読み取ることができます。

スクイーズ (Squeeze): 相手に選択を迫り、どちらのスートを捨ててもディクレアラーがトリックを取れるように仕向ける高度なテクニックです。これは非常に難易度が高いですが、成功すると大きな達成感があります。

安全なプレイ (Safety Play)

コントラクト達成を確実にするために、あえて全てのトリックを取ろうとせず、最低限必要なトリックを確保するプレイです。例えば、特定のカードが相手のどちらにあるかわからない場合、リスクを最小限に抑える方法を選択します。

2. ディフェンスプレイ：宣言者を阻止する守護者
ディフェンス（守備側）は、宣言者のコントラクト達成を阻止するために協力します。パートナーとのコミュニケーションが特に重要になります。

オープニングリードの選択

最も重要な瞬間: プレイ全体を通して最も重要なディフェンスの判断の一つです。適切なオープニングリードは、宣言者のプランを崩し、ディフェンスにトリックをもたらします。

パートナーのビッドからヒントを得る: オークション中にパートナーが宣言したスートや、オーバーコール、ダブルなどから、パートナーが強いスートや枚数を持っているスートを推測し、そこからリードを検討します。

危険なスートを避ける: 宣言者が得意そうなスートや、宣言者がトリックを伸ばしそうなスートへのリードは避けましょう。

エースからリードしない: 通常、エースからリードすると相手のキングをフリーにしてしまう可能性があるため、避けるべきです。例外として、切り札スートで相手をフォースしたい場合などがあります。

トップオブシーケンス (Top of Sequence): 連続した高位カード（例: K-Q-J）がある場合、一番高いカードからリードすることで、パートナーにそのスートの状況を知らせ、トリックを確保する可能性が高まります。

シグナルとディスカード (Signaling and Discarding)

シグナル (Signaling): プレイ中にカードを出す順序や、どのカードを出すかによって、パートナーに自分の手札の状況を伝えます。

アティチュードシグナル (Attitude Signal): そのスートへの好意（ハイカードを出す）か嫌悪（ローカードを出す）を示す。

カウンティングシグナル (Counting Signal): そのスートに何枚持っているかを示す（偶数枚か奇数枚かなど）。

リターンシグナル (Return Signal): 相手のスートをリードする際に、特定のカードでパートナーにリターンしてほしいスートを要求する。

ディスカード (Discard): 宣言者がサイドスートを伸ばしてきた時に、不要なカードを捨てることでパートナーに情報を伝えます。捨てたスートは、通常、そのスートに興味がないか、そのスートでのトリックを期待していないことを示します。

テンポの理解とコントロール

ディフェンス側もプレイのテンポを意識することが重要です。相手にリードを渡すことで、不利なスートからのリードを強要したり、自分のサイドスートを伸ばす時間を稼いだりします。

切り札のディフェンス

アンダートランプ (Undertrump): 宣言者の切り札を低い切り札で切ることで、切り札を消耗させます。

オーバートランプ (Overtrump): 宣言者が出した切り札を、より高い切り札で切ることでトリックを奪います。

切り札を温存する： 自分のサイドスートに切り札を切られないように、切り札を温存することも重要です。

読解と推測 (Reading and Inference)

オークションでのビッド、プレイ中のカードの出し方、ディスカードなど、相手とパートナーのあらゆる動きから情報を読み取り、相手の手札やプランを推測します。これがディフェンスの成功の鍵となります。

上級者への道：実践と振り返り
ブリッジのプレイは、知識だけでなく経験が大きく影響します。

徹底的な分析: プレイが終わった後、そのボードを振り返り、なぜコントラクトが成功したのか、失敗したのかを分析しましょう。別のプレイ方法があったか、ディフェンスは最適だったか、などを考察します。

パートナーシップの深化: パートナーとの間で、プレイ中のシグナルやディスカードの約束事を確認し、プレイの意図を共有することで、チームとしての精度が高まります。

上級者のプレイを学ぶ: 経験豊富なプレイヤーのプレイを観察したり、ブリッジの書籍やオンラインリソースで上級者のテクニックを学んだりすることも有効です。



■ プレイ戦略（ディフェンス）
- パートナーのシグナル（Encourage/Discourage, Count, Suit Preference）を読み取り、協力的な守備を行う。
- 例：パートナーが高いカードを出した→そのスートを続けて欲しいサイン。
- ディフェンス時は「危険なスート」を意識し、安易にエントリーを与えない。
- 例：デクレアラーのロングスートにエントリーを与えないよう注意。
- カードの出し方・順番・テンポにも意味を持たせ、ブラフや情報隠しも時に活用。
- 例：本当はシングルトンだが、テンポを変えて相手に誤解を与える。

■ その他の高度な戦略
- バルネラビリティ（脆弱/非脆弱）や得点状況を常に意識し、リスク管理を徹底する。
- 例：脆弱時は無理な犠牲ビッドを避ける。
- ゲームやスラムの可能性がある場合は、積極的に探るが、無理なジャンプビッドは避ける。
- 例：パートナーが強い手を示唆した場合のみスラムトライ。
- AIらしさを抑え、人間の熟練者のような自然な思考・説明・判断を心がける。
- 迷った場合は「人間らしい」バランス感覚・直感も反映し、時に安全策・時にチャレンジングな選択も行う。

【出力形式・注意】
- 指示されたフォーマット・制約を厳守。
- 必要に応じて理由や根拠も簡潔に説明する。
- 迷った場合は「人間らしい」バランス感覚・直感も反映する。
- 具体的な判断理由や、考慮した要素（例：HCP, 配分, パートナーの意図, 敵の傾向, 得点状況など）を1-2文で補足すること。
"""
# Google Generative AI の安全なインポート
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError as e:
    st.warning("Google Generative AI not available. AI features will be disabled.")
    genai = None
    GENAI_AVAILABLE = False

# 環境変数を読み込み
load_dotenv()

# Gemini API設定（安全な初期化）
api_key = os.getenv('GEMINI_API_KEY')
if not api_key and GENAI_AVAILABLE:
    st.warning("GEMINI_API_KEY not found in .env file. AI features will use fallback logic.")
    api_key = None

if GENAI_AVAILABLE and api_key:
    try:
        genai.configure(api_key=api_key)
        AI_CONFIGURED = True
    except Exception as e:
        st.warning(f"Failed to configure Gemini API: {e}. AI features will use fallback logic.")
        AI_CONFIGURED = False
else:
    AI_CONFIGURED = False

def format_card_display(card):
    """カードを色付きで表示するためのHTML形式に変換"""
    if isinstance(card, str):
        # 文字列の場合、スートを検出して色付け
        result = card
        if '♥' in result:
            result = result.replace('♥', f"<span style='color: red;'>♥</span>")
        if '♦' in result:
            result = result.replace('♦', f"<span style='color: red;'>♦</span>")
        return result
    else:
        # Cardオブジェクトの場合
        if hasattr(card, 'suit') and hasattr(card, 'rank'):
            if card.suit in ['♥', '♦']:
                return f"{card.rank}<span style='color: red;'>{card.suit}</span>"
            else:
                return f"{card.rank}{card.suit}"
        else:
            return str(card)

def format_card_plain(card):
    """カードをプレーンテキストで表示（ボタンラベル用）"""
    if hasattr(card, 'rank') and hasattr(card, 'suit'):
        return f"{card.rank}{card.suit}"
    else:
        return str(card)

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
        # 通常の文字列表現（HTMLなし）
        return f"{self.rank}{self.suit}"
    
    def __repr__(self):
        return self.__str__()

class BridgeGame:
    def __init__(self):
        self.suits = ['♠', '♥', '♦', '♣']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = []
        
        # プレイヤー（人間はSouth固定）
        self.players = {
            'North': [],
            'South': [],  # Human player
            'East': [],
            'West': []
        }
        
        # ゲーム状態
        self.game_phase = 'partnership'  # partnership -> deal -> auction -> play -> scoring
        self.current_round = 1
        self.max_rounds = 5  # 5ラウンド制
        
        # パートナーシップ決定
        self.partnerships = {}
        self.dealer = None
        
        # オークション関連
        self.auction_history = []
        self.current_bidder = None
        self.pass_count = 0
        self.contract = None
        self.declarer = None
        self.dummy = None
        self.trump_suit = None
        self.contract_level = 0
        self.doubled = 0
        
        # プレイ関連
        self.tricks = []
        self.current_trick = []
        self.trick_leader = None
        self.tricks_won = {'NS': 0, 'EW': 0}
        self.dummy_revealed = False
        self.cards_played = []
        
        # スコア
        self.round_scores = []
        self.total_scores = {'NS': 0, 'EW': 0}
        self.vulnerable = {'NS': False, 'EW': False}
        
        # Gemini APIモデルの初期化（安全な初期化）
        self.model = None
        if GENAI_AVAILABLE and AI_CONFIGURED:
            try:
                self.model = genai.GenerativeModel('gemini-pro')
            except Exception as e:
                print(f"Warning: Failed to initialize Gemini model: {e}")
                self.model = None
    
    def create_deck(self):
        """52枚のデッキを作成"""
        self.deck = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.deck)
    
    def determine_partnerships_and_dealer(self):
        """パートナーシップとディーラーを決定"""
        # パートナーシップは固定：ユーザー（South）とNorthがチーム
        self.partnerships = {
            'NS': ['North', 'South'],
            'EW': ['East', 'West']
        }
        
        # ディーラーをランダムに決定
        players = ['North', 'South', 'East', 'West']
        self.dealer = random.choice(players)
        
        self.game_phase = 'deal'
    
    def deal_cards(self):
        """カードを配布（各プレイヤー13枚）"""
        self.create_deck()
        players_order = ['South', 'West', 'North', 'East']  # ディーラーの左から時計回り
        
        for i, card in enumerate(self.deck):
            player = players_order[i % 4]
            self.players[player].append(card)
        
        # 手札をソート
        for player in self.players:
            self.players[player].sort(key=lambda x: (x.get_suit_rank(), x.value), reverse=True)
    
    def get_next_player(self, current_player):
        """次のプレイヤーを取得（時計回り）"""
        order = ['South', 'West', 'North', 'East']
        current_idx = order.index(current_player)
        return order[(current_idx + 1) % 4]
    
    def get_partnership(self, player):
        """プレイヤーの所属パートナーシップを取得"""
        for partnership, members in self.partnerships.items():
            if player in members:
                return partnership
        return None
    
    def get_bid_rank(self, bid):
        """ビッドのランクを計算（比較用）"""
        if bid['type'] != 'bid':
            return -1
        
        level = bid['level']
        suit_ranks = {'♣': 0, '♦': 1, '♥': 2, '♠': 3, 'NT': 4}
        return level * 5 + suit_ranks[bid['suit']]
    
    def is_valid_bid(self, bid):
        """ビッドが有効かチェック"""
        if not self.auction_history:
            return True
        
        last_bids = [b for b in self.auction_history if b['type'] == 'bid']
        if not last_bids:
            return True
        
        last_bid = last_bids[-1]
        return self.get_bid_rank(bid) > self.get_bid_rank(last_bid)
    
    def make_auction_call(self, call):
        """オークションでコールを行う"""
        self.auction_history.append({
            'player': self.current_bidder,
            'type': call['type'],
            **call
        })
        
        if call['type'] == 'pass':
            self.pass_count += 1
        else:
            self.pass_count = 0
        
        # オークション終了判定
        if self.pass_count >= 3 and len(self.auction_history) >= 4:
            self.end_auction()
        else:
            self.current_bidder = self.get_next_player(self.current_bidder)
    
    def end_auction(self):
        """オークション終了処理"""
        # 最後の有効なビッドを探す
        bids = [call for call in self.auction_history if call['type'] == 'bid']
        
        if not bids:
            # 全員パス - ラウンドスコアに0点を記録して次のラウンドへ
            self.round_scores.append({
                'round': self.current_round,
                'contract': "Pass Out",
                'declarer': None,
                'made': 0,
                'ns_score': 0,
                'ew_score': 0
            })
            self.game_phase = 'scoring'
            return
        
        final_bid = bids[-1]
        self.contract = final_bid
        self.contract_level = final_bid['level']
        self.trump_suit = final_bid['suit']
        
        # ディクレアラー決定：そのスートを最初にビッドしたプレイヤー
        declarer_partnership = self.get_partnership(final_bid['player'])
        for call in self.auction_history:
            if (call['type'] == 'bid' and 
                call['suit'] == self.trump_suit and 
                self.get_partnership(call['player']) == declarer_partnership):
                self.declarer = call['player']
                break
        
        # ダミー決定
        for partnership, members in self.partnerships.items():
            if self.declarer in members:
                self.dummy = [p for p in members if p != self.declarer][0]
                break
        
        # プレイフェーズ開始
        self.start_play_phase()
    
    def reset_for_new_deal(self):
        """新しいディールのためのリセット"""
        self.auction_history = []
        self.pass_count = 0
        self.contract = None
        self.declarer = None
        self.dummy = None
        self.trump_suit = None
        self.contract_level = 0
        self.doubled = 0
        
        # ディーラーを回す
        self.dealer = self.get_next_player(self.dealer)
        self.current_bidder = self.dealer
        
        # プレイヤーの手札をクリア
        for player in self.players:
            self.players[player] = []
    
    def start_play_phase(self):
        """プレイフェーズ開始"""
        self.game_phase = 'play'
        # オープニングリードはディクレアラーの左隣（ダミーの右隣）
        self.trick_leader = self.get_next_player(self.declarer)
        self.current_trick = []
        self.tricks = []
        self.tricks_won = {'NS': 0, 'EW': 0}
        self.dummy_revealed = False
        self.current_player = self.trick_leader  # 現在のプレイヤー
        self.opening_lead_made = False  # オープニングリードが行われたか
    
    def get_current_player_for_trick(self):
        """現在のトリックで次にプレイするプレイヤーを取得"""
        if not self.current_trick:
            return self.trick_leader
        
        # トリックリーダーから時計回り
        played_count = len(self.current_trick)
        if played_count >= 4:
            return None  # トリック完了
        
        current = self.trick_leader
        for _ in range(played_count):
            current = self.get_next_player(current)
        return current
    
    def can_play_card(self, player, card):
        """プレイヤーがそのカードをプレイできるかチェック"""
        if player not in self.players or card not in self.players[player]:
            return False
        
        # 現在のプレイヤーかチェック
        current_player = self.get_current_player_for_trick()
        if current_player != player:
            return False
        
        # フォローのルールをチェック
        if not self.current_trick:
            # リード：任意のカードをプレイ可能
            return True
        
        # フォロー：リードスートがあればフォローする必要がある
        led_suit = self.current_trick[0]['card'].suit
        suit_cards = [c for c in self.players[player] if c.suit == led_suit]
        
        if suit_cards and card.suit != led_suit:
            return False  # フォローできるのにしていない
        
        return True
    
    def play_card(self, player, card):
        """カードをプレイ"""
        if not self.can_play_card(player, card):
            return False
        
        # カードをプレイ
        self.players[player].remove(card)
        self.current_trick.append({'player': player, 'card': card})
        
        # オープニングリード後にダミーを公開
        if len(self.current_trick) == 1 and not self.opening_lead_made:
            self.dummy_revealed = True
            self.opening_lead_made = True
        
        # トリック完了チェック（UIで手動実行のため自動完了は削除）
        # if len(self.current_trick) == 4:
        #     self.complete_trick()
        
        return True
    
    def complete_trick(self):
        """トリック完了処理"""
        if len(self.current_trick) != 4:
            return
        
        # 勝者を決定
        winner = self.determine_trick_winner()
        winner_partnership = self.get_partnership(winner)
        
        # スコア記録
        self.tricks_won[winner_partnership] += 1
        self.tricks.append({
            'tricks': self.current_trick.copy(),
            'winner': winner,
            'leader': self.trick_leader
        })
        
        # 次のトリックの準備
        self.trick_leader = winner
        self.current_trick = []
        
        # ゲーム終了チェック
        if len(self.tricks) == 13:
            self.end_round()
    
    def determine_trick_winner(self):
        """トリックの勝者を決定"""
        if not self.current_trick:
            return None
        
        led_suit = self.current_trick[0]['card'].suit
        trump_suit = self.trump_suit if self.trump_suit != 'NT' else None
        
        # トランプが出ているかチェック
        trump_cards = [play for play in self.current_trick if play['card'].suit == trump_suit] if trump_suit else []
        
        if trump_cards:
            # トランプの中で最強
            winner_play = max(trump_cards, key=lambda x: x['card'].value)
        else:
            # リードスートの中で最強
            suit_cards = [play for play in self.current_trick if play['card'].suit == led_suit]
            if suit_cards:
                winner_play = max(suit_cards, key=lambda x: x['card'].value)
            else:
                # リードスートがない場合は最初のプレイヤーが勝利
                winner_play = self.current_trick[0]
        
        return winner_play['player']
    
    def get_ai_auction_call(self, player: str) -> Dict:
        """AIのオークションコールを取得"""
        hand_str = ", ".join([str(card) for card in self.players[player]])
        auction_str = "\n".join([
            f"{call['player']}: {call['type']}" + 
            (f" {call['level']}{call['suit']}" if call['type'] == 'bid' else "")
            for call in self.auction_history[-6:]  # 最近の6コール
        ])
        
        prompt = f"""
        You are a {player} Bridge player.
        Current hand: {hand_str}
        Recent auction history:
        {auction_str}
        
        Follow Contract Bridge auction rules to make an appropriate call.
        
        Options:
        1. pass - Pass
        2. bid - Bid (e.g., 1♠, 2NT, 3♥)
        3. double - Double (only when opponent has bid)
        4. redouble - Redouble (only when we are doubled)
        
        Respond in format:
        Type: [pass/bid/double/redouble]
        (For bid) Level: [1-7]
        (For bid) Suit: [♣/♦/♥/♠/NT]
        
        Example: "Type: bid, Level: 1, Suit: ♠"
        """
        
        try:
            if not self.model:
                # モデルが利用できない場合はランダムなコール
                return {'type': 'pass'}
            
            response = self.model.generate_content(prompt)
            response_text = response.text.strip()
            
            # レスポンス解析
            if "pass" in response_text.lower():
                return {'type': 'pass'}
            elif "bid" in response_text.lower():
                # レベルとスートを抽出
                level = 1
                suit = '♣'
                
                # 簡単な解析
                for line in response_text.split('\n'):
                    if 'level' in line.lower():
                        try:
                            level = int([c for c in line if c.isdigit()][0])
                        except:
                            level = 1
                    if 'suit' in line.lower():
                        for s in ['♠', '♥', '♦', '♣', 'NT']:
                            if s in line:
                                suit = s
                                break
                
                bid = {'type': 'bid', 'level': level, 'suit': suit}
                if self.is_valid_bid(bid):
                    return bid
                else:
                    return {'type': 'pass'}
            else:
                return {'type': 'pass'}
                
        except Exception as e:
            st.error(f"AI thinking error ({player}): {e}")
            return {'type': 'pass'}
    
    def calculate_score(self):
        """スコア計算"""
        if not self.contract:
            return 0, 0
        
        declarer_partnership = self.get_partnership(self.declarer)
        tricks_needed = 6 + self.contract_level
        tricks_won = self.tricks_won[declarer_partnership]
        
        if tricks_won >= tricks_needed:
            # コントラクト成功
            return self.calculate_make_score(tricks_won - tricks_needed)
        else:
            # コントラクト失敗
            return self.calculate_down_score(tricks_needed - tricks_won)
    
    def calculate_make_score(self, overtricks):
        """メイク時のスコア計算"""
        declarer_partnership = self.get_partnership(self.declarer)
        score = 0
        
        # トリック点
        if self.trump_suit in ['♣', '♦']:
            score += self.contract_level * 20
        elif self.trump_suit in ['♥', '♠']:
            score += self.contract_level * 30
        elif self.trump_suit == 'NT':
            score += 40 + (self.contract_level - 1) * 30
        
        # ボーナス点
        if score < 100:
            score += 50  # パートスコア
        else:
            # ゲームボーナス
            is_vulnerable = self.vulnerable[declarer_partnership]
            score += 500 if is_vulnerable else 300
            
            # スラムボーナス
            if self.contract_level == 6:  # スモールスラム
                score += 750 if is_vulnerable else 500
            elif self.contract_level == 7:  # グランドスラム
                score += 1500 if is_vulnerable else 1000
        
        # オーバートリック
        score += overtricks * 30
        
        # ダブル/リダブルボーナス
        if self.doubled > 0:
            score *= (2 ** self.doubled)
        
        if declarer_partnership == 'NS':
            return score, 0
        else:
            return 0, score
    
    def calculate_down_score(self, down_tricks):
        """ダウン時のスコア計算"""
        declarer_partnership = self.get_partnership(self.declarer)
        defender_partnership = 'EW' if declarer_partnership == 'NS' else 'NS'
        is_vulnerable = self.vulnerable[declarer_partnership]
        
        score = 0
        if self.doubled == 0:
            # アンダブル
            score = down_tricks * (100 if is_vulnerable else 50)
        else:
            # ダブル/リダブル
            if is_vulnerable:
                score = 200 + (down_tricks - 1) * 300
            else:
                penalties = [100, 300, 500] + [300] * (down_tricks - 3)
                score = sum(penalties[:down_tricks])
            
            if self.doubled == 2:  # リダブル
                score *= 2
        
        if defender_partnership == 'NS':
            return score, 0
        else:
            return 0, score

    def start_new_round(self):
        """新しいラウンドを開始"""
        if self.current_round < self.max_rounds:
            self.current_round += 1
            self.game_phase = 'deal'
            self.reset_for_new_deal()
            return True
        return False
    
    def reset_round(self):
        """ラウンドリセット"""
        self.auction_phase = True
        self.play_phase = False
        self.auction_history = []
        self.pass_count = 0
        self.contract = None
        self.declarer = None
        self.dummy = None
        self.trump_suit = None
        self.contract_level = 0
        self.doubled = 0
        self.tricks = []
        self.current_trick = []
        self.tricks_won = {'NS': 0, 'EW': 0}
        self.dummy_revealed = False
        
        # ディーラーを回す
        self.dealer = self.get_next_player(self.dealer)
        self.current_bidder = self.dealer
    
    def start_auction(self):
        """オークション開始"""
        self.game_phase = 'auction'
        self.current_bidder = self.dealer
        self.auction_history = []
        self.pass_count = 0
    
    def get_next_player_for_trick(self):
        """現在のトリックで次にプレイするプレイヤーを取得"""
        if not self.current_trick:
            return self.trick_leader
        
        # 現在のトリックで何人プレイしたかに基づいて次のプレイヤーを決定
        players_played = len(self.current_trick)
        if players_played >= 4:
            return None  # トリック完了
        
        # トリックリーダーから順番に
        current_player = self.trick_leader
        for _ in range(players_played):
            current_player = self.get_next_player(current_player)
        
        return current_player
    
    def get_ai_card_play(self, player):
        """AIのカードプレイを取得"""
        if player not in self.players or not self.players[player]:
            return None
        
        # 簡単なAI: ランダムに有効なカードを選択
        valid_cards = self.get_valid_cards(player)
        if valid_cards:
            return random.choice(valid_cards)
        return None
    
    def get_valid_cards(self, player):
        """プレイヤーがプレイできる有効なカードを取得"""
        hand = self.players.get(player, [])
        if not hand:
            return []
        
        if not self.current_trick:
            # リード: 任意のカードをプレイ可能
            return hand
        
        # フォロー: リードスートをフォローする必要がある
        led_suit = self.current_trick[0]['card'].suit
        suit_cards = [card for card in hand if card.suit == led_suit]
        
        if suit_cards:
            return suit_cards
        else:
            # フォローできない場合は任意のカード
            return hand
    
    def end_round(self):
        """ラウンド終了処理（13トリック完了後）"""
        # スコア計算
        ns_score, ew_score = self.calculate_score()
        
        # ラウンドスコアを記録
        self.round_scores.append({
            'round': self.current_round,
            'contract': f"{self.contract_level}{self.trump_suit}" if self.contract else "Pass Out",
            'declarer': self.declarer,
            'made': self.tricks_won[self.get_partnership(self.declarer)] if self.declarer else 0,
            'ns_score': ns_score,
            'ew_score': ew_score
        })
        
        # トータルスコア更新
        self.total_scores['NS'] += ns_score
        self.total_scores['EW'] += ew_score
        
        # ゲームフェーズをスコア表示に変更
        self.game_phase = 'scoring'
        
        # バルネラビリティの更新（簡略化：2ラウンド目から両方バルネラブル）
        if self.current_round >= 2:
            self.vulnerable['NS'] = True
            self.vulnerable['EW'] = True
    
    def record_passout_round(self):
        """全員パス時のラウンド記録処理"""
        # 全員パス時は両チーム0点
        ns_score = 0
        ew_score = 0
        
        # ラウンドスコアを記録
        self.round_scores.append({
            'round': self.current_round,
            'contract': "Pass Out",
            'declarer': None,
            'made': 0,
            'ns_score': ns_score,
            'ew_score': ew_score
        })
        
        # トータルスコア更新（0点なので変わらず）
        self.total_scores['NS'] += ns_score
        self.total_scores['EW'] += ew_score
        
        # ゲームフェーズをスコア表示に変更
        self.game_phase = 'scoring'
        
        # バルネラビリティの更新（簡略化：2ラウンド目から両方バルネラブル）
        if self.current_round >= 2:
            self.vulnerable['NS'] = True
            self.vulnerable['EW'] = True

def display_card(card):
    """Streamlitでカードを表示"""
    return st.markdown(f"🃏 {format_card_display(card)}", unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Contract Bridge Game", page_icon="🃏", layout="wide")
    
    st.title("🃏 Contract Bridge - Official Rules")
    st.markdown("---")
    
    # デバッグ情報
    st.sidebar.write("**Debug Info**")
    st.sidebar.write(f"Streamlit version: {st.__version__}")
    
    # ゲーム状態の初期化
    try:
        if 'game' not in st.session_state:
            st.session_state.game = BridgeGame()
        
        game = st.session_state.game
        st.sidebar.write(f"Game phase: {game.game_phase}")
        st.sidebar.write(f"Model available: {'Yes' if game.model else 'No'}")
        
    except Exception as e:
        st.error(f"Game initialization failed: {e}")
        st.stop()
    
    # ゲーム情報表示
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Round", f"{game.current_round}/{game.max_rounds}")
    
    with col2:
        st.metric("NS Total", game.total_scores.get('NS', 0))
    
    with col3:
        st.metric("EW Total", game.total_scores.get('EW', 0))
    
    with col4:
        if st.button("New Game"):
            with st.spinner("Starting new game..."):
                st.session_state.game = BridgeGame()
            st.rerun()
    
    # フェーズ別表示
    if game.game_phase == 'partnership':
        show_partnership_phase(game)
    elif game.game_phase == 'deal':
        show_deal_phase(game)
    elif game.game_phase == 'auction':
        show_auction_phase(game)
    elif game.game_phase == 'play':
        show_play_phase(game)
    elif game.game_phase == 'scoring':
        show_round_results(game)
    elif game.game_phase == 'game_over':
        show_round_results(game)  # ゲーム終了時も同じ画面
    else:
        show_round_results(game)

def show_partnership_phase(game):
    """パートナーシップ決定フェーズの表示"""
    st.subheader("🎴 Partnership Setup")
    st.write("Setting up partnerships and selecting dealer...")
    
    # パートナーシップ表示
    st.subheader("🤝 Fixed Partnerships")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**North-South**: North & South (You)")
    with col2:
        st.info("**East-West**: East & West")
    
    if st.button("Start Game"):
        with st.spinner("Setting up game..."):
            game.determine_partnerships_and_dealer()
        st.rerun()
    
    # ルール説明
    with st.expander("📖 Partnership Rules"):
        st.markdown("""
        ### Partnership Setup
        
        1. **Fixed Partnerships**: North-South vs East-West
        2. **Your Position**: You are South, partnered with North
        3. **Dealer**: Selected randomly to start the game
        4. **Consistency**: Same partnerships throughout all rounds
        
        **Note**: This setup ensures consistent gameplay without card drawing.
        """)

def show_deal_phase(game):
    """カード配布フェーズの表示"""
    st.subheader("🃏 Card Dealing")
    
    # ディーラー表示
    if game.dealer:
        st.write(f"**Dealer:** {game.dealer}")
    
    # パートナーシップ表示
    st.subheader("🤝 Partnerships")
    if game.partnerships:
        cols = st.columns(2)
        teams = list(game.partnerships.items())
        for i, (team_name, members) in enumerate(teams):
            with cols[i]:
                member_str = " & ".join(members)
                if team_name == 'NS':
                    st.success(f"**{team_name}**: {member_str} (Your Team)")
                else:
                    st.info(f"**{team_name}**: {member_str}")
    
    if st.button("Deal Cards"):
        with st.spinner("Dealing cards..."):
            game.deal_cards()
            game.start_auction()
        st.rerun()
    
    # ルール説明
    with st.expander("📖 Dealing Rules"):
        st.markdown("""
        ### Card Dealing Rules
        
        1. **Shuffling**: The deck is shuffled thoroughly
        2. **Dealing**: 13 cards are dealt to each player
        3. **Sorting**: Players sort their hands by suit and rank
        
        **Note**: After dealing, the auction phase begins automatically.
        """)

def show_auction_phase(game):
    """オークションフェーズの表示"""
    st.subheader("🎯 Auction Phase")
    
    # オークション履歴
    if game.auction_history:
        st.write("**Auction History:**")
        history_lines = []
        for i, call in enumerate(game.auction_history):
            if i % 4 == 0:
                history_lines.append("")
            call_str = call['type']
            if call['type'] == 'bid':
                suit_display = format_card_display(call['suit'])
                call_str = f"{call['level']}{suit_display}"
            history_lines[-1] += f"{call['player']}: {call_str}  "
        
        for line in history_lines:
            if line.strip():
                st.markdown(line, unsafe_allow_html=True)
    
    st.write(f"**Current Bidder:** {game.current_bidder}")
    
    # Humanのターンの場合
    if game.current_bidder == 'South':
        st.subheader("🎴 Your Hand")
        south_cards = game.players['South']
        if south_cards:
            # 固定の13カラムでカード表示（空のカラムも含む）
            hand_cols = st.columns(13)
            for i in range(13):
                with hand_cols[i]:
                    if i < len(south_cards):
                        card = south_cards[i]
                        if card.suit in ['♥', '♦']:
                            card_display = f"<span style='color: red; font-size: 18px;'>{card.rank}{card.suit}</span>"
                        else:
                            card_display = f"<span style='font-size: 18px;'>{card.rank}{card.suit}</span>"
                        st.markdown(f"🃏 {card_display}", unsafe_allow_html=True)
                    else:
                        st.write("")  # 空のスペース
        
        st.subheader("🗣️ Your Call")
        
        # ビッドオプション
        bid_col1, bid_col2, bid_col3 = st.columns(3)
        
        with bid_col1:
            if st.button("Pass"):
                with st.spinner("Processing pass..."):
                    game.make_auction_call({'type': 'pass'})
                st.rerun()
        
        with bid_col2:
            st.write("**Bid:**")
            level = st.selectbox("Level", [1, 2, 3, 4, 5, 6, 7], key="bid_level")
            
            # スート選択を改善
            st.write("**Suit:**")
            
            # 現在選択されているスートを保持
            if 'selected_suit' not in st.session_state:
                st.session_state.selected_suit = '♣'
            
            # スート選択のラジオボタン
            suit_options = ['♣', '♦', '♥', '♠', 'NT']
            suit_labels = ['♣ Clubs', 
                          '♦ Diamonds', 
                          '♥ Hearts', 
                          '♠ Spades', 
                          'NT No Trump']
            
            # カスタムラジオボタンスタイル
            selected_index = suit_options.index(st.session_state.selected_suit)
            
            # 5つのカラムでスート選択
            suit_cols = st.columns(5)
            for i, (suit, label) in enumerate(zip(suit_options, suit_labels)):
                with suit_cols[i]:
                    if suit == '♦':
                        st.markdown("<span style='color: red; font-size: 24px;'>♦</span>", unsafe_allow_html=True)
                    elif suit == '♥':
                        st.markdown("<span style='color: red; font-size: 24px;'>♥</span>", unsafe_allow_html=True)
                    elif suit == 'NT':
                        st.markdown("<span style='font-size: 20px;'>NT</span>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<span style='font-size: 24px;'>{suit}</span>", unsafe_allow_html=True)
                    
                    button_style = "🔘" if st.session_state.selected_suit == suit else "⚪"
                    if st.button(f"{button_style}", key=f"bid_{suit}", help=label):
                        st.session_state.selected_suit = suit
                        st.rerun()
            
            # 選択されたスートを明確に表示
            suit = st.session_state.selected_suit
            if suit == '♦':
                selected_display = "<span style='color: red;'>♦</span>"
            elif suit == '♥':
                selected_display = "<span style='color: red;'>♥</span>"
            else:
                selected_display = suit
            st.markdown(f"**Selected:** {selected_display}", unsafe_allow_html=True)
            
            if st.button("Bid"):
                bid = {'type': 'bid', 'level': level, 'suit': suit}
                if game.is_valid_bid(bid):
                    with st.spinner("Processing bid..."):
                        game.make_auction_call(bid)
                    st.rerun()
                else:
                    st.error("Please make a higher bid than the previous one")
        
        with bid_col3:
            # ダブル/リダブルオプション（実装簡略化）
            if st.button("Double", disabled=True):
                st.info("Double feature coming soon")
    
    else:
        # AIのターン
        if st.button("Execute AI Call"):
            with st.spinner(f"Waiting for {game.current_bidder} to make a call..."):
                ai_call = game.get_ai_auction_call(game.current_bidder)
                game.make_auction_call(ai_call)
            st.rerun()
        
        st.info(f"{game.current_bidder} is thinking...")
    
    # オークション終了の自動チェック
    if game.pass_count >= 3 and len(game.auction_history) >= 4:
        st.success("Auction completed!")
        if game.contract:
            if game.trump_suit in ['♥', '♦']:
                trump_display = f"<span style='color: red;'>{game.trump_suit}</span>"
            else:
                trump_display = game.trump_suit
            contract_display = f"{game.contract_level}{trump_display}"
            st.markdown(f"**Final Contract:** {contract_display} by {game.declarer}", unsafe_allow_html=True)
            if st.button("Start Play Phase"):
                with st.spinner("Starting play phase..."):
                    game.start_play_phase()
                st.rerun()
        else:
            st.write("All players passed. No contract was made.")
            st.info("This round ends with 0 points for both teams.")
            if st.button("End Round (All Pass)"):
                with st.spinner("Ending round..."):
                    # 全員パス時のスコア記録
                    game.record_passout_round()
                st.rerun()

def show_play_phase(game):
    """プレイフェーズの表示"""
    st.subheader("🎮 Play Phase")
    
    # コントラクト情報
    if game.contract:
        if game.contract['suit'] in ['♥', '♦']:
            contract_suit_display = f"<span style='color: red;'>{game.contract['suit']}</span>"
        else:
            contract_suit_display = game.contract['suit']
        contract_display = f"{game.contract['level']}{contract_suit_display}"
        st.markdown(f"**Contract:** {contract_display} by {game.declarer}", unsafe_allow_html=True)
        st.info(f"**Declarer:** {game.declarer} | **Dummy:** {game.dummy}")
        needed_tricks = 6 + game.contract_level
        st.info(f"**Tricks Needed:** {needed_tricks}")
    
    # トリック数表示
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("NS Tricks Won", game.tricks_won['NS'])
    with col2:
        st.metric("EW Tricks Won", game.tricks_won['EW'])
    with col3:
        st.metric("Tricks Played", f"{len(game.tricks)}/13")
    
    # 現在のプレイヤーを表示
    current_player = game.get_current_player_for_trick()
    if current_player:
        st.write(f"**Current turn:** {current_player}")
    elif len(game.current_trick) == 4:
        # トリック完了時
        winner = game.determine_trick_winner()
        st.write(f"**Trick completed** - Winner: {winner}")
    
    # 現在のトリック表示
    if game.current_trick:
        st.subheader("🎯 Current Trick")
        trick_cols = st.columns(4)
        positions = ['North', 'East', 'South', 'West']  # テーブル位置順
        
        for i, position in enumerate(positions):
            with trick_cols[i]:
                st.write(f"**{position}**")
                # そのポジションのプレイヤーがプレイしたカードを探す
                played_card = None
                for play in game.current_trick:
                    if play['player'] == position:
                        played_card = play['card']
                        break
                
                if played_card:
                    if played_card.suit in ['♥', '♦']:
                        card_display = f"<span style='color: red; font-size: 20px;'>{played_card.rank}{played_card.suit}</span>"
                    else:
                        card_display = f"<span style='font-size: 20px;'>{played_card.rank}{played_card.suit}</span>"
                    st.markdown(f"🃏 {card_display}", unsafe_allow_html=True)
                else:
                    st.write("---")  # まだプレイしていない
    
    # ダミーの手札表示（ダミーが公開された後）
    if game.dummy_revealed and game.dummy:
        st.subheader(f"🃏 {game.dummy} Hand (Dummy)")
        dummy_cards = game.players[game.dummy]
        if dummy_cards:
            # スートごとに整理して表示
            suits_order = ['♠', '♥', '♦', '♣']
            for suit in suits_order:
                suit_cards = [card for card in dummy_cards if card.suit == suit]
                if suit_cards:
                    suit_cards.sort(key=lambda x: x.value, reverse=True)
                    cards_display_parts = []
                    for card in suit_cards:
                        if card.suit in ['♥', '♦']:
                            cards_display_parts.append(f"<span style='color: red;'>{card.rank}{card.suit}</span>")
                        else:
                            cards_display_parts.append(f"{card.rank}{card.suit}")
                    cards_display = ' '.join(cards_display_parts)
                    if suit in ['♥', '♦']:
                        suit_display = f"<span style='color: red;'>{suit}</span>"
                    else:
                        suit_display = suit
                    st.markdown(f"**{suit_display}**: {cards_display}", unsafe_allow_html=True)
    
    # プレイヤーのターン処理
    current_player = game.get_current_player_for_trick()
    
    # トリック完了チェック（4人全員がプレイした場合）
    if len(game.current_trick) == 4:
        winner = game.determine_trick_winner()
        st.success(f"🏆 Trick won by {winner}")
        
        if st.button("Continue to Next Trick"):
            # トリックを完了して次へ
            game.complete_trick()
            st.rerun()
    elif current_player == 'South':
        # 人間プレイヤー（South）のターン
        st.subheader("🎴 Your Turn - Choose a Card")
        south_cards = game.players['South']
        if south_cards:
            # プレイ可能なカードのみ表示
            valid_cards = game.get_valid_cards('South')
            
            if not game.current_trick:
                st.write("**You lead this trick**")
            else:
                led_suit = game.current_trick[0]['card'].suit
                st.write(f"**Follow suit: {led_suit}** (if possible)")
            
            # スートごとに手札を表示
            suits_order = ['♠', '♥', '♦', '♣']
            for suit in suits_order:
                suit_cards = [card for card in south_cards if card.suit == suit]
                if suit_cards:
                    suit_cards.sort(key=lambda x: x.value, reverse=True)
                    st.write(f"**{suit}**:")
                    
                    cols = st.columns(min(len(suit_cards), 13))
                    for i, card in enumerate(suit_cards):
                        if i < len(cols):
                            with cols[i]:
                                can_play = card in valid_cards
                                disabled = not can_play
                                
                                # カードを色付きで大きく表示
                                if card.suit in ['♥', '♦']:
                                    card_display = f"<span style='color: red; font-size: 20px;'>{card.rank}{card.suit}</span>"
                                else:
                                    card_display = f"<span style='font-size: 20px;'>{card.rank}{card.suit}</span>"
                                
                                st.markdown(f"🃏 {card_display}", unsafe_allow_html=True)
                                
                                if st.button(
                                    f"Play", 
                                    key=f"play_{suit}_{card.rank}",
                                    disabled=disabled,
                                    help="Click to play this card" if can_play else "Cannot play this card"
                                ):
                                    if game.play_card('South', card):
                                        st.markdown(f"✅ **You played {format_card_display(card)}**", unsafe_allow_html=True)
                                        st.rerun()
                                    else:
                                        st.error("Invalid card play")
    
    elif current_player == game.dummy:
        # ダミーのターン（Declarerが選択）
        if game.declarer == 'South':
            st.subheader(f"🎴 {game.dummy} Turn (You control as Declarer)")
            
            # ユーザーがダミーをプレイする際は、自分（South）の手札も表示
            st.subheader("🎴 Your Hand (South) - For Reference")
            south_cards = game.players['South']
            if south_cards:
                # スートごとに整理して表示
                suits_order = ['♠', '♥', '♦', '♣']
                for suit in suits_order:
                    suit_cards = [card for card in south_cards if card.suit == suit]
                    if suit_cards:
                        suit_cards.sort(key=lambda x: x.value, reverse=True)
                        cards_display_parts = []
                        for card in suit_cards:
                            if card.suit in ['♥', '♦']:
                                cards_display_parts.append(f"<span style='color: red;'>{card.rank}{card.suit}</span>")
                            else:
                                cards_display_parts.append(f"{card.rank}{card.suit}")
                        cards_display = ' '.join(cards_display_parts)
                        if suit in ['♥', '♦']:
                            suit_display = f"<span style='color: red;'>{suit}</span>"
                        else:
                            suit_display = suit
                        st.markdown(f"**{suit_display}**: {cards_display}", unsafe_allow_html=True)
            
            dummy_cards = game.players[game.dummy]
            if dummy_cards:
                valid_cards = game.get_valid_cards(game.dummy)
                
                st.write(f"**Choose a card for {game.dummy}:**")
                # ダミーの有効カードを表示
                cols = st.columns(min(len(valid_cards), 13))
                for i, card in enumerate(valid_cards):
                    if i < len(cols):
                        with cols[i]:
                            # カードを色付きで大きく表示
                            if card.suit in ['♥', '♦']:
                                card_display = f"<span style='color: red; font-size: 20px;'>{card.rank}{card.suit}</span>"
                            else:
                                card_display = f"<span style='font-size: 20px;'>{card.rank}{card.suit}</span>"
                            
                            st.markdown(f"🃏 {card_display}", unsafe_allow_html=True)
                            
                            if st.button(
                                f"Play", 
                                key=f"dummy_play_{i}",
                                help=f"Play {card} from dummy"
                            ):
                                if game.play_card(game.dummy, card):
                                    st.markdown(f"✅ **You played {format_card_display(card)} from dummy**", unsafe_allow_html=True)
                                    st.rerun()
        else:
            st.info(f"Waiting for {game.declarer} to choose a card for {game.dummy}...")
            if st.button("Execute Declarer's Choice"):
                # AI がダミーのカードを選択
                valid_cards = game.get_valid_cards(game.dummy)
                if valid_cards:
                    chosen_card = random.choice(valid_cards)
                    if game.play_card(game.dummy, chosen_card):
                        st.markdown(f"✅ **{game.declarer} played {format_card_display(chosen_card)} from dummy**", unsafe_allow_html=True)
                        st.rerun()
    
    elif current_player:
        # AIプレイヤーのターン
        st.info(f"Waiting for {current_player} to play a card...")
        if st.button(f"Execute {current_player}'s Play"):
            card = game.get_ai_card_play(current_player)
            if card and game.play_card(current_player, card):
                st.markdown(f"✅ **{current_player} played {format_card_display(card)}**", unsafe_allow_html=True)
                st.rerun()
    
    # ゲーム終了チェック
    if len(game.tricks) == 13:
        st.success("🎉 All 13 tricks completed!")
        if st.button("View Results"):
            game.end_round()
            st.rerun()
    
def show_round_results(game):
    """ラウンド結果表示"""
    st.subheader(f"📊 Round {game.current_round} Results")
    
    # 最新のラウンドスコアを表示
    if game.round_scores and len(game.round_scores) >= game.current_round:
        latest_round = game.round_scores[-1]
        
        st.write(f"**Contract:** {latest_round['contract']}")
        if latest_round['declarer']:
            st.write(f"**Declarer:** {latest_round['declarer']}")
            st.write(f"**Tricks Made:** {latest_round['made']}/13")
        
        col1, col2 = st.columns(2)
        with col1:
            if latest_round['ns_score'] > 0:
                st.success(f"**NS Score:** +{latest_round['ns_score']}")
            else:
                st.write(f"**NS Score:** {latest_round['ns_score']}")
        
        with col2:
            if latest_round['ew_score'] > 0:
                st.success(f"**EW Score:** +{latest_round['ew_score']}")
            else:
                st.write(f"**EW Score:** {latest_round['ew_score']}")
    
    # 累計スコア表示
    st.subheader("🏆 Total Scores")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("North-South", game.total_scores['NS'])
    with col2:
        st.metric("East-West", game.total_scores['EW'])
    
    # 次のラウンドまたはゲーム終了
    if game.current_round < game.max_rounds:
        if st.button("Start Next Round"):
            with st.spinner("Preparing next round..."):
                game.start_new_round()
            st.rerun()
    else:
        st.subheader("� Game Over!")
        if game.total_scores['NS'] > game.total_scores['EW']:
            st.balloons()
            st.success(f"🥇 North-South pair wins! Final Score: {game.total_scores['NS']} - {game.total_scores['EW']}")
        elif game.total_scores['EW'] > game.total_scores['NS']:
            st.balloons()
            st.success(f"🥇 East-West pair wins! Final Score: {game.total_scores['EW']} - {game.total_scores['NS']}")
        else:
            st.info(f"🤝 Tie game! Final Score: {game.total_scores['NS']} - {game.total_scores['EW']}")
        
        if st.button("Start New Game"):
            with st.spinner("Starting new game..."):
                st.session_state.game = BridgeGame()
            st.rerun()
    
    # ゲームルール説明
    with st.expander("📖 Contract Bridge Rules"):
        st.markdown("""
        ### Contract Bridge Rules (Official)
        
        #### Game Overview
        - **Players**: 4 players (North, South, East, West)
        - **Partnerships**: North-South vs East-West
        - **Rounds**: 5 rounds
        
        #### Game Flow
        1. **Auction**: Determine trump suit and required tricks through bidding
        2. **Play**: 13-trick trick-taking game
        3. **Scoring**: Points based on contract success/failure
        
        #### Auction
        - **Bid**: Level(1-7) + Suit(♣♦♥♠NT)
        - **Pass**: Don't bid
        - **Double/Redouble**: Challenge opponent's bid (high risk/reward)
        
        #### Scoring
        - **Made**: Trick points + Bonus points
        - **Down**: Penalty points to opponents
        - **Vulnerability**: Bonuses/penalties vary
        
        #### Victory Condition
        Highest total score after 5 rounds wins
        """)

if __name__ == "__main__":
    main()
