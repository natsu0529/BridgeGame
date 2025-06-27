# 🃏 Contract Bridge Game - Multi-Agent Edition

Contract Bridgeゲームをプレイできるウェブアプリケーション。Google Gemini APIを使用した3人のAIエージェントと対戦できます。

## 🎯 主な機能

- **正式なContract Bridgeルール**: オークションとプレイフェーズの完全実装
- **AIプレイヤー**: Google Gemini APIによる知的な入札とプレイ
- **マルチラウンドゲーム**: 5ラウンドのトーナメント形式
- **インタラクティブUI**: カラー表示対応のクリーンなインターフェース
- **パートナーシップ制**: 伝統的なNorth-South vs East-West形式

## 🚀 インストール

### ローカル開発環境

1. リポジトリをクローン:
```bash
git clone https://github.com/natsu0529/BridgeGame.git
cd BridgeGame/Desktop/bridge
```

2. 仮想環境を作成:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

3. 依存関係をインストール:
```bash
pip install -r requirements.txt
```

4. 環境変数を設定:
```bash
cp .env.example .env
# .envファイルを編集してGEMINI_API_KEYを追加
```

5. アプリケーションを実行:
```bash
streamlit run app.py
```

### 🌐 Streamlit Cloudデプロイ

1. このリポジトリをフォーク
2. [Streamlit Cloud](https://share.streamlit.io/)に接続
3. アプリをデプロイ
4. アプリ設定で以下のシークレットを追加:
   - `GEMINI_API_KEY`: Google Gemini APIキー（オプション）

**注意**: APIキーなしでもアプリは動作しますが、AIプレイヤーは簡単なフォールバックロジックを使用します。

## ⚙️ 設定

### 環境変数

- `GEMINI_API_KEY`: Google Gemini APIキー（AIプレイヤー用、オプション）

### Streamlit Cloudシークレット

Streamlit Cloudのアプリ設定で以下を追加:
```toml
GEMINI_API_KEY = "your_api_key_here"
```

## 🎮 ゲームルール

このゲームは正式なContract Bridgeルールに従います:

1. **オークションフェーズ**: プレイヤーが入札してコントラクトを決定
2. **プレイフェーズ**: 13トリックのトリックテイキングゲーム
3. **スコアリング**: 標準的なBridgeスコアリングシステム
4. **パートナーシップ**: 固定のNorth-South vs East-West

## 🛠️ 技術仕様

- **フレームワーク**: Streamlit
- **AI**: Google Gemini API
- **言語**: Python 3.8+
- **デプロイ**: Streamlit Cloud対応

## 📁 プロジェクト構造

- `app.py`: メインアプリケーション
- `requirements.txt`: Python依存関係
- `.env.example`: 環境変数テンプレート
- `.streamlit/`: Streamlit設定ファイル

## 🤝 開発への貢献

1. リポジトリをフォーク
2. フィーチャーブランチを作成
3. 変更を加える
4. 必要に応じてテストを追加
5. プルリクエストを送信

## 📄 ライセンス

このプロジェクトはMITライセンスの下でオープンソースとして公開されています。
- 最終スコアが最も高いプレイヤーが勝利

## 技術仕様

- **フロントエンド**: Streamlit
- **AI**: Google Gemini API
- **言語**: Python 3.10+
- **アーキテクチャ**: マルチエージェント

## セキュリティ

APIキーは`.env`ファイルで管理され、`.gitignore`によりGitリポジトリには含まれません。
