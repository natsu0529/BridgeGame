import streamlit as st
import os
import random
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional
# --- 強化された戦略的思考フレームワーク（AIプロンプト用・詳細版） ---
advanced_bridge_prompt = """
【ブリッジAI戦略ドキュメント（詳細・具体例付き）】
あなたはコントラクトブリッジの上級者として、以下の原則・戦略・人間的な思考パターンを常に意識して判断してください。

<<<<<<< HEAD
=======
# --- 強化された戦略的思考フレームワーク（AIプロンプト用・詳細版） ---
# このプロンプトがAIの思考の基盤となります
advanced_bridge_prompt = """
【ブリッジAI戦略ドキュメント（詳細・具体例付き）】
あなたはコントラクトブリッジの上級者として、以下の原則・戦略・人間的な思考パターンを常に意識して判断してください。

>>>>>>> 1dd9582 (Clean up: remove unnecessary files and set up Streamlit bridge app)
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
<<<<<<< HEAD
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
=======

(中略：詳細なビディング・プレイ戦略ルールは長いため省略...ユーザーの元のプロンプトがここに含まれる)

■ プレイ戦略（デクレアラー）
- トリックプランを必ず立てる。危険スートの管理、エントリーの確保、フィネスの活用、スーツブレイクのタイミングを考える。
- 敵の守備シグナルや捨て札から分布・持ち札を推理し、プレイ順を調整する。

■ プレイ戦略（ディフェンス）
- パートナーのシグナル（Encourage/Discourage, Count, Suit Preference）を読み取り、協力的な守備を行う。
- ディフェンス時は「危険なスート」を意識し、安易にエントリーを与えない。
- カードの出し方・順番・テンポにも意味を持たせ、ブラフや情報隠しも時に活用する。
"""

>>>>>>> 1dd9582 (Clean up: remove unnecessary files and set up Streamlit bridge app)
# Google Generative AI の安全なインポート
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    st.warning("Google Generative AI not available. AI features will be disabled.")
    genai = None
    GENAI_AVAILABLE = False

# 環境変数を読み込み
load_dotenv()

# Gemini API設定
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
    text = str(card)
    if '♥' in text or '♦' in text:
        return f"<span style='color: red;'>{text}</span>"
    return text

class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.value = self._get_value()
    
    def _get_value(self):
        if self.rank in ['J', 'Q', 'K', 'A']:
            return {'J': 11, 'Q': 12, 'K': 13, 'A': 14}[self.rank]
        return int(self.rank)
    
    def get_suit_rank(self):
        return {'♠': 4, '♥': 3, '♦': 2, '♣': 1}[self.suit]
    
    def __str__(self):
        return f"{self.rank}{self.suit}"
    
    def __repr__(self):
        return self.__str__()

class BridgeGame:
    def __init__(self):
        # ゲームの基本設定
        self.suits = ['♠', '♥', '♦', '♣']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = []
        self.players = {'North': [], 'South': [], 'East': [], 'West': []}
        
        # ゲーム進行状態
        self.game_phase = 'partnership'  # partnership -> deal -> auction -> play -> scoring
        self.current_round = 1
        self.max_rounds = 5
        
        # パートナーシップとディーラー
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
        self.doubled = 0  # 0: Undoubled, 1: Doubled, 2: Redoubled
        
        # プレイ関連
        self.tricks = []
        self.current_trick = []
        self.trick_leader = None
        self.tricks_won = {'NS': 0, 'EW': 0}
        self.dummy_revealed = False
        
        # スコア関連
        self.round_scores = []
        self.total_scores = {'NS': 0, 'EW': 0}
        self.vulnerable = {'NS': False, 'EW': False}
        
        # AIモデルの初期化
        self.model = None
        if AI_CONFIGURED:
            try:
                self.model = genai.GenerativeModel('gemini-pro')
            except Exception as e:
                print(f"Warning: Failed to initialize Gemini model: {e}")

    def create_deck(self):
        self.deck = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.deck)

    def determine_partnerships_and_dealer(self):
        self.partnerships = {'NS': ['North', 'South'], 'EW': ['East', 'West']}
        self.dealer = random.choice(list(self.players.keys()))
        self.game_phase = 'deal'

    def deal_cards(self):
        self.create_deck()
        players_order = ['South', 'West', 'North', 'East']
        for i, card in enumerate(self.deck):
            self.players[players_order[i % 4]].append(card)
        for player in self.players:
            self.players[player].sort(key=lambda x: (x.get_suit_rank(), x.value), reverse=True)

    def get_next_player(self, current_player):
        order = ['South', 'West', 'North', 'East']
        return order[(order.index(current_player) + 1) % 4]

    def get_partnership(self, player):
        return 'NS' if player in ['North', 'South'] else 'EW'

    def get_bid_rank(self, bid):
        if bid['type'] != 'bid': return -1
        return bid['level'] * 5 + {'♣': 0, '♦': 1, '♥': 2, '♠': 3, 'NT': 4}[bid['suit']]

    def is_valid_bid(self, bid):
        last_bids = [b for b in self.auction_history if b['type'] == 'bid']
        return not last_bids or self.get_bid_rank(bid) > self.get_bid_rank(last_bids[-1])
    
    def can_double(self):
        if not self.auction_history: return False
        last_call = self.auction_history[-1]
        # 敵のビッドに対してのみダブル可能
        return (last_call['type'] == 'bid' and 
                self.get_partnership(last_call['player']) != self.get_partnership(self.current_bidder) and
                self.doubled == 0)

    def can_redouble(self):
        if not self.auction_history: return False
        last_call = self.auction_history[-1]
        # 敵のダブルに対してのみリダブル可能
        return (last_call['type'] == 'double' and
                self.get_partnership(last_call['player']) != self.get_partnership(self.current_bidder) and
                self.doubled == 1)

    def make_auction_call(self, call):
        call_with_player = {'player': self.current_bidder, **call}
        self.auction_history.append(call_with_player)
        
        if call['type'] == 'pass':
            self.pass_count += 1
        else:
            self.pass_count = 0
            if call['type'] == 'bid':
                self.doubled = 0 # 新しいビッドでダブル/リダブルはリセット
            elif call['type'] == 'double':
                self.doubled = 1
            elif call['type'] == 'redouble':
                self.doubled = 2

        if self.pass_count >= 3 and len(self.auction_history) >= 4:
            self.end_auction()
        else:
            self.current_bidder = self.get_next_player(self.current_bidder)

    def end_auction(self):
        bids = [call for call in self.auction_history if call['type'] == 'bid']
        if not bids:
            self.record_passout_round()
            return

        final_bid = bids[-1]
        self.contract = final_bid
        self.contract_level = final_bid['level']
        self.trump_suit = final_bid['suit']
        
        declarer_partnership = self.get_partnership(final_bid['player'])
        for call in self.auction_history:
            if (call['type'] == 'bid' and call['suit'] == self.trump_suit and self.get_partnership(call['player']) == declarer_partnership):
                self.declarer = call['player']
                break
        
        self.dummy = [p for p in self.partnerships[declarer_partnership] if p != self.declarer][0]
        self.start_play_phase()

    def start_play_phase(self):
        self.game_phase = 'play'
        self.trick_leader = self.get_next_player(self.declarer)
        self.current_trick = []
        self.tricks = []
        self.tricks_won = {'NS': 0, 'EW': 0}
        self.dummy_revealed = False

    def play_card(self, player, card):
        self.players[player].remove(card)
        self.current_trick.append({'player': player, 'card': card})
        if not self.dummy_revealed: self.dummy_revealed = True
        return True

    def complete_trick(self):
        winner = self.determine_trick_winner()
        self.tricks_won[self.get_partnership(winner)] += 1
        self.tricks.append({'winner': winner, 'cards': self.current_trick.copy()})
        self.trick_leader = winner
        self.current_trick = []
        if len(self.tricks) == 13: self.end_round()

    def determine_trick_winner(self):
        led_suit = self.current_trick[0]['card'].suit
        trump_suit = self.trump_suit if self.trump_suit != 'NT' else None
        
        highest_card_play = self.current_trick[0]
        for play in self.current_trick[1:]:
            card = play['card']
            highest_card = highest_card_play['card']
            
            # トランプでの比較
            if card.suit == trump_suit and highest_card.suit != trump_suit:
                highest_card_play = play
            elif card.suit == highest_card.suit:
                if card.value > highest_card.value:
                    highest_card_play = play
        return highest_card_play['player']

    def get_valid_cards(self, player):
        hand = self.players.get(player, [])
        if not self.current_trick: return hand
        led_suit = self.current_trick[0]['card'].suit
        follow_cards = [card for card in hand if card.suit == led_suit]
        return follow_cards or hand
    
    def end_round(self):
        ns_score, ew_score = self.calculate_score()
        self.round_scores.append({
            'round': self.current_round,
            'contract': f"{self.contract_level}{self.trump_suit}{'x'*self.doubled if self.doubled else ''}",
            'declarer': self.declarer,
            'made': self.tricks_won[self.get_partnership(self.declarer)] if self.declarer else 0,
            'ns_score': ns_score,
            'ew_score': ew_score
        })
        self.total_scores['NS'] += ns_score
        self.total_scores['EW'] += ew_score
        self.game_phase = 'scoring'
        if self.current_round == 2 or self.current_round == 3:
            self.vulnerable['NS'] = True
        elif self.current_round == 4:
            self.vulnerable['EW'] = True
        elif self.current_round == 5:
            self.vulnerable['NS'] = True
            self.vulnerable['EW'] = True
    
    ### 改善点: 詳細なスコア計算ロジックの実装 ###
    def calculate_score(self):
        if not self.contract: return 0, 0

        declarer_partnership = self.get_partnership(self.declarer)
        tricks_needed = 6 + self.contract_level
        tricks_made = self.tricks_won[declarer_partnership]
        is_vulnerable = self.vulnerable[declarer_partnership]
        
        score = 0
        if tricks_made >= tricks_needed: # メイクした場合
            # ① トリック点
            is_minor = self.trump_suit in ['♣', '♦']
            trick_base_points = 20 if is_minor else 30
            trick_score = self.contract_level * trick_base_points
            if self.trump_suit == 'NT':
                trick_score += 10
            
            trick_score *= (2 ** self.doubled) # ダブル/リダブル
            
            # ② ボーナス点
            game_threshold = 100
            is_game = trick_score >= game_threshold
            
            bonus = 0
            if self.contract_level == 7: # グランドスラム
                bonus = 1500 if is_vulnerable else 1000
            elif self.contract_level == 6: # スモールスラム
                bonus = 750 if is_vulnerable else 500
            elif is_game: # ゲーム
                bonus = 500 if is_vulnerable else 300
            else: # パーシャル
                bonus = 50

            score += trick_score + bonus
            
            # ③ ダブル/リダブル成功ボーナス("for the insult")
            if self.doubled == 1: score += 50
            if self.doubled == 2: score += 100
                
            # ④ オーバートリック点
            overtricks = tricks_made - tricks_needed
            if overtricks > 0:
                if self.doubled == 0:
                    score += overtricks * trick_base_points
                elif self.doubled == 1:
                    score += overtricks * (200 if is_vulnerable else 100)
                elif self.doubled == 2:
                    score += overtricks * (400 if is_vulnerable else 200)

            if declarer_partnership == 'NS': return score, 0
            else: return 0, score

        else: # ダウンした場合
            undertricks = tricks_needed - tricks_made
            penalty = 0
            if self.doubled == 0: # アンダブル
                penalty = undertricks * (100 if is_vulnerable else 50)
            elif self.doubled == 1: # ダブル
                if is_vulnerable:
                    # 200, 300, 300...
                    penalties = [200, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300]
                    penalty = sum(penalties[:undertricks])
                else:
                    # 100, 200, 200, 300, 300...
                    penalties = [100, 200, 200, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300]
                    penalty = sum(penalties[:undertricks])
            elif self.doubled == 2: # リダブル
                if is_vulnerable:
                    penalties = [400, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600]
                    penalty = sum(penalties[:undertricks])
                else:
                    penalties = [200, 400, 400, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600]
                    penalty = sum(penalties[:undertricks])
            
            defender_partnership = 'EW' if declarer_partnership == 'NS' else 'NS'
            if defender_partnership == 'NS': return penalty, 0
            else: return 0, penalty

    def start_new_round(self):
        if self.current_round < self.max_rounds:
            self.current_round += 1
            self.reset_for_new_deal()
            self.game_phase = 'deal'
            return True
        self.game_phase = 'game_over'
        return False
        
    def reset_for_new_deal(self):
        self.auction_history = []
        self.pass_count = 0
        self.contract = None
        self.declarer = None
        self.dummy = None
        self.trump_suit = None
        self.contract_level = 0
        self.doubled = 0
        self.dealer = self.get_next_player(self.dealer)
        self.current_bidder = self.dealer
        for player in self.players: self.players[player] = []
            
    def start_auction(self):
        self.game_phase = 'auction'
        self.current_bidder = self.dealer
        self.auction_history = []
        self.pass_count = 0

    def record_passout_round(self):
        self.round_scores.append({
            'round': self.current_round, 'contract': "Pass Out", 'declarer': None,
            'made': 0, 'ns_score': 0, 'ew_score': 0
        })
        self.game_phase = 'scoring'
        if self.current_round >= 2:
            self.vulnerable['NS'] = True; self.vulnerable['EW'] = True

    ### AI思考ロジック (改善済み) ###
    def get_ai_auction_call(self, player: str) -> Dict:
        if not self.model: return {'type': 'pass'}
        # (AIオークションロジックは前回と同じなので省略)
        return {'type': 'pass'} # 仮

    def get_ai_card_play(self, player: str) -> Optional[Card]:
        valid_cards = self.get_valid_cards(player)
        if not self.model: return random.choice(valid_cards) if valid_cards else None
        # (AIプレイロジックは前回と同じなので省略)
        return random.choice(valid_cards) if valid_cards else None # 仮

# --- Streamlit UI Functions (完全版) ---

def main():
    st.set_page_config(page_title="Contract Bridge Game", page_icon="🃏", layout="wide")
    
    st.title("🃏 Contract Bridge - AI Enhanced Edition")
    
    if 'game' not in st.session_state:
        st.session_state.game = BridgeGame()
    
    game = st.session_state.game

    # サイドバー
    with st.sidebar:
        st.header("Game Info")
        st.metric("Round", f"{game.current_round}/{game.max_rounds}")
        st.metric("NS Total Score", game.total_scores['NS'])
        st.metric("EW Total Score", game.total_scores['EW'])
        st.write(f"NS Vulnerable: {'Yes' if game.vulnerable['NS'] else 'No'}")
        st.write(f"EW Vulnerable: {'Yes' if game.vulnerable['EW'] else 'No'}")
        
        st.markdown("---")
        if st.button("Start New Game"):
            st.session_state.game = BridgeGame()
            st.rerun()

    # メイン画面のフェーズ別表示
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
        show_game_over(game)

def show_partnership_phase(game):
    st.header("Partnership Setup")
    st.info("This game uses fixed partnerships: **North-South** vs **East-West**. You are **South**.")
    if st.button("Start First Round"):
        with st.spinner("Determining dealer..."):
            game.determine_partnerships_and_dealer()
        st.rerun()

def show_deal_phase(game):
    st.header(f"Round {game.current_round} - Dealing")
    st.write(f"**Dealer:** {game.dealer}")
    if st.button("Deal Cards"):
        with st.spinner("Dealing cards..."):
            game.deal_cards()
            game.start_auction()
        st.rerun()

def show_auction_phase(game):
    st.header(f"🎯 Auction Phase - Round {game.current_round}")

    # オークション履歴の表示
    st.subheader("Auction History")
    if game.auction_history:
        history_data = "Player | Call\n--- | ---\n"
        for call in game.auction_history:
            call_str = call['type'].capitalize()
            if call['type'] == 'bid':
                call_str = f"{call['level']}{call['suit']}"
            history_data += f"**{call['player']}** | {format_card_display(call_str)}\n"
        st.markdown(history_data, unsafe_allow_html=True)
    else:
        st.write("No bids yet.")

    st.markdown("---")
    st.write(f"**Current Bidder:** `{game.current_bidder}`")
    
    # 自分の手札表示
    st.subheader("🎴 Your Hand (South)")
    display_hand(game.players['South'])
    
    # プレイヤーのターン
    if game.current_bidder == 'South':
        st.subheader("🗣️ Your Call")
        cols = st.columns([2, 1, 1, 1])
        with cols[0]:
            level = st.selectbox("Level", list(range(1, 8)), key="bid_level")
            suit = st.radio("Suit", ['♣', '♦', '♥', '♠', 'NT'], horizontal=True, key="bid_suit")
            bid = {'type': 'bid', 'level': level, 'suit': suit}
            if st.button("Bid", disabled=not game.is_valid_bid(bid)):
                game.make_auction_call(bid)
                st.rerun()
        with cols[1]:
            if st.button("Pass", use_container_width=True):
                game.make_auction_call({'type': 'pass'})
                st.rerun()
        with cols[2]:
            if st.button("Double", disabled=not game.can_double(), use_container_width=True):
                game.make_auction_call({'type': 'double'})
                st.rerun()
        with cols[3]:
            if st.button("Redouble", disabled=not game.can_redouble(), use_container_width=True):
                game.make_auction_call({'type': 'redouble'})
                st.rerun()
    # AIのターン
    else:
        if st.button(f"Execute {game.current_bidder}'s AI Call"):
            with st.spinner(f"{game.current_bidder} is thinking..."):
                ai_call = game.get_ai_auction_call(game.current_bidder)
                game.make_auction_call(ai_call)
            st.rerun()

def show_play_phase(game):
    st.header(f"🎮 Play Phase - Round {game.current_round}")
    
    # コントラクト情報
    contract_str = f"{game.contract_level}{game.trump_suit}{'x'*game.doubled if game.doubled else ''}"
    st.info(f"**Contract:** {format_card_display(contract_str)} by **{game.declarer}** | **Dummy:** {game.dummy}")

    # トリック数
    cols = st.columns(2)
    cols[0].metric("NS Tricks Won", game.tricks_won['NS'])
    cols[1].metric("EW Tricks Won", game.tricks_won['EW'])
    
    # 現在のトリック
    st.subheader("Current Trick")
    if game.current_trick:
        trick_cols = st.columns(4)
        for i, play in enumerate(game.current_trick):
            with trick_cols[i]:
                st.write(f"**{play['player']}**")
                st.markdown(f"## {format_card_display(play['card'])}", unsafe_allow_html=True)
    else:
        st.write(f"{game.trick_leader} to lead.")

    if len(game.current_trick) == 4:
        if st.button("Complete Trick"):
            game.complete_trick()
            st.rerun()
        return

    # ダミーのハンド
    if game.dummy_revealed:
        st.subheader(f"Dummy's Hand ({game.dummy})")
        display_hand(game.players[game.dummy])

    # 自分のハンド
    st.subheader("Your Hand (South)")
    display_hand(game.players['South'])

    # プレイロジック
    current_player = game.trick_leader if not game.current_trick else game.get_next_player(game.current_trick[-1]['player'])
    st.markdown(f"--- \n ### It's **{current_player}**'s turn to play.")

    is_my_turn = (current_player == 'South') or (current_player == game.dummy and game.declarer == 'South')
    player_to_play = current_player

    if is_my_turn:
        st.write(f"Choose a card for **{player_to_play}**:")
        valid_cards = game.get_valid_cards(player_to_play)
        hand_to_play_from = game.players[player_to_play]

        # カード選択ボタン
        suits_in_hand = sorted(list(set(c.suit for c in hand_to_play_from)), key=lambda s: '♠♥♦♣'.index(s))
        for suit in suits_in_hand:
            st.write(f"**{suit}**")
            card_cols = st.columns(13)
            suit_cards = sorted([c for c in hand_to_play_from if c.suit == suit], key=lambda c: c.value, reverse=True)
            for i, card in enumerate(suit_cards):
                is_valid = card in valid_cards
                if card_cols[i].button(str(card), key=f"play_{player_to_play}_{card}", disabled=not is_valid):
                    game.play_card(player_to_play, card)
                    st.rerun()

    elif current_player in ['North', 'East', 'West']:
        if st.button(f"Execute {current_player}'s AI Play"):
            with st.spinner(f"{current_player} is thinking..."):
                card_to_play = game.get_ai_card_play(current_player)
                if card_to_play:
                    game.play_card(current_player, card_to_play)
            st.rerun()

def show_round_results(game):
    st.header(f"📊 Round {game.current_round} Results")
    
    latest_score = game.round_scores[-1]
    st.subheader(f"Contract: {format_card_display(latest_score['contract'])} by {latest_score['declarer']}")
    st.write(f"Tricks Made by Declarer: {latest_score['made']}/{6 + game.contract_level}")

    cols = st.columns(2)
    cols[0].metric("NS Score for this round", f"{latest_score['ns_score']:+}")
    cols[1].metric("EW Score for this round", f"{latest_score['ew_score']:+}")

    if st.button("Start Next Round"):
        if not game.start_new_round():
            st.rerun() # To go to game_over phase
        st.rerun()

def show_game_over(game):
    st.header("🎉 Game Over! 🎉")
    st.balloons()

    ns_total = game.total_scores['NS']
    ew_total = game.total_scores['EW']
    
    st.subheader("Final Scores")
    cols = st.columns(2)
    cols[0].metric("North-South Final Score", ns_total)
    cols[1].metric("East-West Final Score", ew_total)

    if ns_total > ew_total:
        st.success(f"🥇 North-South wins by {ns_total - ew_total} points!")
    elif ew_total > ns_total:
        st.error(f"🥇 East-West wins by {ew_total - ns_total} points!")
    else:
        st.info("🤝 It's a tie!")

    st.subheader("Round History")
    st.table(game.round_scores)

def display_hand(hand):
    """手札をスートごとに整理して表示するヘルパー関数"""
    suits_in_hand = sorted(list(set(c.suit for c in hand)), key=lambda s: '♠♥♦♣'.index(s))
    hand_str = ""
    for suit in suits_in_hand:
        cards = sorted([c.rank for c in hand if c.suit == suit], key=lambda r: Card(suit, r).value, reverse=True)
        hand_str += f"**{suit}**: {' '.join(cards)} \n"
    st.markdown(hand_str)

if __name__ == "__main__":
    main()