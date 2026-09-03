# 🍅 トマト葉病害検出アプリ

## 概要

トマトの葉の画像から、病害または健康な葉を検出するWebアプリです。

YOLO26mで学習した物体検出モデルを、Streamlitを用いてアプリ化しました。画像をアップロードすると、検出された病害名、信頼度、検出位置を表示します。

## 公開デモ

**[Hugging Face Spacesでアプリを試す](https://kliework4510-tomato-disease-app.hf.space)**

## 主な機能

- トマトの葉の画像から病害候補を検出
- 検出位置をバウンディングボックスで表示
- 病害名を日本語と英語で表示
- 検出結果の信頼度を表示
- 信頼度のしきい値を画面上で調整
- 10クラスの病害・健康状態に対応

## 対応クラス

| クラス名 | 日本語 |
|---|---|
| Bacterial Spot | 細菌性斑点病 |
| Early Blight | 早期疫病 |
| Healthy | 健康 |
| Late Blight | 疫病 |
| Leaf Mold | 葉かび病 |
| Leaf Miner | ハモグリバエ |
| Mosaic Virus | モザイクウイルス |
| Septoria | セプトリア葉枯病 |
| Spider Mites | ハダニ |
| Yellow Leaf Curl Virus | 黄化葉巻ウイルス |

## モデル性能

| 指標 | スコア |
|---|---:|
| mAP50 | 0.83 |
| mAP50-95 | 0.66 |
| Precision | 0.82 |
| Recall | 0.77 |

## 学習条件

- モデル：YOLO26m
- エポック数：50
- 入力画像サイズ：640 × 640
- 学習画像数：18,366枚
- クラス数：10

## 使用技術

- Python
- Ultralytics YOLO
- Streamlit
- OpenCV
- Pillow
- NumPy
- Hugging Face Spaces

## 処理の流れ

1. ユーザーが葉の画像をアップロード
2. YOLOモデルが画像内の病害候補を検出
3. 検出位置、クラス名、信頼度を取得
4. Streamlit上に検出結果を表示

## ファイル構成

- `app.py`：Streamlitアプリ本体
- `data.yaml`：クラスおよびデータセット設定
- `requirements.txt`：必要なライブラリ
- `.gitignore`：Git管理対象外ファイルの設定

## データセット

[Tomato Leaf Disease Dataset](https://universe.roboflow.com/universitas-atma-jaya/tomato-leaf-disease-rxcft/dataset/6)を使用しました。

- クラス数：10
- ライセンス：CC BY 4.0

## 制約

- 撮影環境や葉の状態によって、検出精度が変化する可能性があります。
- 学習データに含まれない病害は検出できません。
- 本アプリは機械学習の学習・検証を目的としたものであり、専門家による診断を代替するものではありません。