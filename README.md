# Real Estate Scraper（日本の不動産サイト向けスクレイピング）

このプロジェクトは、日本の不動産情報サイトから物件の情報をスクレイピングし、  
件数取得やデータ保存（将来的にDB）を行うことを目的としています。

初期バージョンでは **神奈川県小田原市の新築戸建て件数を取得するテスト実装** を含みます。

---

## 📁 プロジェクト構成

```
project-root/
│── docker-compose.yml
│── Dockerfile
│── requirements.txt
│── .env（※Git管理に含めない）
│── README.md
│── src/
│ ├── scraper.py
│ └── db.py（将来用）
```

---

## 🚀 使用技術

- Python 3.11
- BeautifulSoup4（HTMLパーサ）
- Requests（HTTPクライアント）
- Docker / Docker Compose
- PostgreSQL（将来的にデータ保存をサポート）
- python-dotenv（環境変数管理）

---

## 🔧 セットアップ

### 1. リポジトリをクローン

```bash
git clone <your-repository-url>
cd <repository>
```

### 2. .env を作成（例）
```
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=realestate_db
DB_PORT=5432
```

## 🐳 Docker で実行
```bash
docker-compose up --build
```

起動すると scraper.py が実行され、
設定された URL の物件件数を取得して出力します。

## 📜 スクリプト概要
scraper.py

不動産サイトからHTMLを取得

BeautifulSoupで解析

物件件数を抽出して表示

db.py

将来的に PostgreSQL へ保存するための接続テンプレート

## 📌 将来の拡張予定

物件データの詳細取得

PostgreSQL へデータ保存

API 化（FastAPI）

定期実行（cron / GitHub Actions）

物件の価格推移トラッキング

## ⚠️ 注意事項

このプロジェクトは 個人学習目的 でのスクレイピングを前提としています。

対象サイトの利用規約を必ず確認し、過度なアクセスは避けてください。

## 📝 ライセンス

MIT License


---
