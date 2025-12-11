# 🛒 E-Commerce データパイプラインプロジェクト

> **Apache Airflow を用いた自動オーケストレーション対応の完全な ELT (Extract, Load, Transform) パイプライン**

本プロジェクトは、**ブラジルの Olist 社のECデータ**を分析するための包括的なデータパイプラインを実装したものです。  
手動実行と自動オーケストレーションの両方をサポートし、モダンなデータエンジニアリングの実践を示しています。

---

## 📊 プロジェクト概要

### ビジネス課題
- 州や時間ごとの売上傾向の把握  
- 配送見積もりと実際のパフォーマンス比較  
- 商品カテゴリ別の売上成績  
- 顧客行動や地域特性の分析  

### データソース
- **一次データ**: Olist ブラジルEC公開データセット（9つのCSVファイル）  
- **二次データ**: ブラジルの祝日API  
- **出力**: SQLite データベース（分析用に変換済みテーブルを格納）

---

## 🏗️ アーキテクチャ概要

- **手動パイプライン**: 開発・テスト向けにステップを個別実行  
- **自動オーケストレーション**: Airflow による本番稼働、スケジューリング・監視対応  

---

## 📊 データセット準備

1. Kaggle より **[Olist Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)** をダウンロード  
2. `dataset/` フォルダを作成し、CSV ファイルを配置  

**必須ファイル**:  
- olist_customers_dataset.csv  
- olist_orders_dataset.csv  
- olist_order_items_dataset.csv  
- olist_order_payments_dataset.csv  
- olist_order_reviews_dataset.csv  
- olist_products_dataset.csv  
- olist_sellers_dataset.csv  
- olist_geolocation_dataset.csv  
- product_category_name_translation.csv  

---

## 🚀 クイックスタート

### 前提条件
- Python 3.8+  
- Docker Desktop  
- Kaggle データセット  

### 実行方法

**1. 自動パイプライン（推奨）**
```bash
cd airflow
docker-compose -f docker-compose-simple.yml up -d
```
- Web UI: http://localhost:8080  
- ログイン: `admin` / `admin`  

**2. 手動パイプライン**
```bash
pip install -r requirements.txt
python -c "from src.extract import extract; extract()"
python -c "from src.load import load; load()"
python -c "from src.transform import run_queries; run_queries()"
```

---

## 📁 プロジェクト構成

- `airflow/`: Airflow DAGs, 演算子, docker-compose 設定  
- `src/`: 抽出・変換・ロード処理のコード  
- `dataset/`: Olist データセット (9 CSV)  
- `queries/`: SQL 変換クエリ  
- `tests/`: 単体テスト・統合テスト  
- `olist.db`: 生成された SQLite DB  
- `AnyoneAI - Sprint Project 01.ipynb`: 分析ノートブック  

---

## 🔄 パイプライン詳細

1. **Extract**: CSV・祝日APIからデータを収集  
2. **Load**: SQLite にロード、正規化テーブル生成  
3. **Transform**: SQL クエリで分析用テーブル作成  
4. **Analyze**: Jupyter Notebookで可視化・洞察抽出  

---

## ⚡ Airflow による自動化機能

- **スケジューリング**: 毎日午前2時に自動実行  
- **信頼性**: リトライ・エラーハンドリング機能  
- **監視**: Web ダッシュボード、実行ログ  
- **保守性**: バージョン管理、設定管理、ロールバック対応  

---

## 📈 分析から得られる主なインサイト

- **売上分析**: 月次/年次トレンド、州別売上、カテゴリ成績  
- **物流パフォーマンス**: 配送見積もり vs 実際、地域別配送分析  
- **商品インテリジェンス**: 人気カテゴリ、成長トレンド  
- **顧客行動**: 地理的分布、レビュー傾向、購買タイミング  

---

## 🎯 ビジネス価値

- データエンジニア: 本番対応パイプライン、スケーラブル設計  
- ビジネスアナリスト: 信頼性の高い日次更新データセット  
- データサイエンティスト: クリーンで再現可能な特徴量生成  

---

## 🚀 今後の拡張

- Kafka によるリアルタイムストリーミング対応  
- AWS/GCP/Azure へのクラウド展開  
- Prometheus/Grafana による監視強化  
- 機械学習を用いた高度分析の導入  

---

## 🎉 実績まとめ

- ✅ 完全な ELT パイプラインの実装  
- ✅ Airflow による自動化・スケジューリング  
- ✅ Docker を用いたコンテナ化  
- ✅ テスト・監視による品質保証  
- ✅ ビジネスインサイトを導出  

**手動スクリプトからエンタープライズ級自動化へ —— これがモダンデータエンジニアリングです！** 🚀

---
