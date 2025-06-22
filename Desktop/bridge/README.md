# Contract Bridge Game - マルチエージェント版

GeminiAPIを使用した3人のAIエージェントと対戦するContract Bridgeゲームです。

## 機能

- StreamlitによるWebベースのUI
- GeminiAPIを使用したマルチエージェント実装
- 5ラウンド制のContract Bridge
- リアルタイムスコア表示
- インタラクティブなカード選択

## セットアップ

1. リポジトリをクローン
```bash
git clone <repository-url>
cd bridge
```

2. 仮想環境を作成・有効化
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# または
venv\Scripts\activate  # Windows
```

3. 依存関係をインストール
```bash
pip install -r requirements.txt
```

4. 環境変数を設定
```bash
cp .env.example .env
```
`.env`ファイルを編集してGemini APIキーを設定してください。

5. アプリケーションを起動
```bash
streamlit run app.py
```

## ゲームルール

- 4人プレイヤー（あなた + 3人のAI）
- 5ラウンド制
- 各ラウンドで全プレイヤーに13枚ずつカード配布
- トリックごとに1点獲得
- 最終スコアが最も高いプレイヤーが勝利

## 技術仕様

- **フロントエンド**: Streamlit
- **AI**: Google Gemini API
- **言語**: Python 3.10+
- **アーキテクチャ**: マルチエージェント

## セキュリティ

APIキーは`.env`ファイルで管理され、`.gitignore`によりGitリポジトリには含まれません。
