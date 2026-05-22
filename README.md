# 🍅 トマト葉病診断アプリ

YOLOv26mを使ったトマトの葉の病気検出アプリです。  
葉の画像をアップロードするだけで、10種類の病気を自動診断します。

---

## 📊 対応している病気（10クラス）

| クラス名 | 日本語 |
|----------|--------|
| Bacterial Spot | 細菌性斑点病 |
| Early Blight | 早期疫病 |
| Healthy | 健康 |
| Late Blight | 疫病 |
| Leaf Mold | 葉かび病 |
| Leaf_Miner | ハモグリバエ |
| Mosaic Virus | モザイクウイルス |
| Septoria | セプトリア葉枯病 |
| Spider Mites | ハダニ |
| Yellow Leaf Curl Virus | 黄化葉巻ウイルス |

---

## 🎯 モデル精度

| 指標 | 値 |
|------|----|
| mAP50 | 0.83 |
| mAP50-95 | 0.66 |
| Precision | 0.82 |
| Recall | 0.77 |

訓練条件: YOLOv26m / 50 epochs / imgsz=640

---

## 🚀 ローカルで動かす

### ① リポジトリをクローン
```bash
git clone https://github.com/YOUR_USERNAME/tomato-disease-app
cd tomato-disease-app
```

### ② モデルをダウンロード
以下からbest.ptをダウンロードして、プロジェクトのルートに置いてください。

👉 [best.pt をダウンロード]（リンクをここに追加）

### ③ 依存パッケージをインストール
```bash
pip install -r requirements.txt
```

### ④ アプリを起動
```bash
streamlit run app.py
```

ブラウザで `http://localhost:8501` が自動で開きます。

---

## 📁 ファイル構成

```
tomato-disease-app/
├── app.py              # Streamlitアプリ本体
├── requirements.txt    # 依存パッケージ
├── data.yaml           # クラス設定
├── best.pt             # 訓練済みモデル（別途ダウンロード）
└── README.md
```

---
👉 **[アプリを開く](https://huggingface.co/spaces/kliework4510/tomato-disease-app)**

## 📦 データセット

- 出典: [Tomato Leaf Disease Dataset](https://universe.roboflow.com/universitas-atma-jaya/tomato-leaf-disease-rxcft/dataset/6)
- ライセンス: CC BY 4.0
- 画像数: 18,366枚（train）
- クラス数: 10
