import streamlit as st
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np

st.set_page_config(page_title="トマト葉病診断", page_icon="🍅", layout="wide")

@st.cache_resource
def load_model():
    return YOLO(r"C:\tomato\runs\tomato_v1\weights\best.pt")

model = load_model()

DISEASE_INFO = {
    "Bacterial Spot":        {"ja": "細菌性斑点病",      "対処": "銅系殺菌剤を散布してください"},
    "Early Blight":          {"ja": "早期疫病",          "対処": "罹患葉を除去し殺菌剤を散布してください"},
    "Healthy":               {"ja": "健康",              "対処": "処置不要です"},
    "Late Blight":           {"ja": "疫病",              "対処": "マンコゼブ系殺菌剤を使用してください"},
    "Leaf Mold":             {"ja": "葉かび病",          "対処": "風通しを良くし殺菌剤を散布してください"},
    "Leaf_Miner":            {"ja": "ハモグリバエ",      "対処": "殺虫剤を散布してください"},
    "Mosaic Virus":          {"ja": "モザイクウイルス",  "対処": "罹患株を除去し拡散を防いでください"},
    "Septoria":              {"ja": "セプトリア葉枯病",  "対処": "殺菌剤を早期に散布してください"},
    "Spider Mites":          {"ja": "ハダニ",            "対処": "殺ダニ剤を散布してください"},
    "Yellow Leaf Curl Virus":{"ja": "黄化葉巻ウイルス", "対処": "媒介するコナジラミを駆除してください"},
}

st.title("🍅 トマト葉病診断アプリ")

with st.sidebar:
    st.header("設定")
    conf_threshold = st.slider("信頼度しきい値", 0.1, 0.9, 0.25, 0.05)
    show_bbox = st.toggle("BBoxを表示", value=True)
    st.divider()
    st.caption("モデル: YOLO26m")
    st.caption("訓練: 50 epochs / mAP50: 0.83")

uploaded = st.file_uploader("葉の画像をアップロード", type=["jpg", "jpeg", "png"])

if uploaded:
    img_pil = Image.open(uploaded).convert("RGB")
    img_np  = np.array(img_pil)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("入力画像")
        st.image(img_pil, use_column_width=True)

    with col2:
        st.subheader("診断結果")
        with st.spinner("診断中..."):
            results = model(img_np, conf=conf_threshold)
            result  = results[0]

        boxes = result.boxes
        st.metric("検出数", f"{len(boxes)} 個")

        if len(boxes) == 0:
            st.warning("病気が検出されませんでした。信頼度しきい値を下げてみてください。")
        else:
            if show_bbox:
                annotated = result.plot()
                annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
                st.image(annotated_rgb, caption="検出結果", use_column_width=True)

            st.divider()
            detected_classes = {}
            for box in boxes:
                cls_id = int(box.cls[0])
                cls_name = model.names[cls_id]
                conf = float(box.conf[0])
                if cls_name not in detected_classes:
                    detected_classes[cls_name] = []
                detected_classes[cls_name].append(conf)

            for cls_name, confs in detected_classes.items():
                info = DISEASE_INFO.get(cls_name, {"ja": cls_name, "対処": "情報なし"})
                avg_conf = sum(confs) / len(confs)
                ja_name = info["ja"]
                treatment = info["対処"]
                is_healthy = cls_name == "Healthy"

                if is_healthy:
                    st.success(f"✅ {ja_name}（{cls_name}）")
                else:
                    st.error(f"⚠️ {ja_name}（{cls_name}）")

                st.progress(avg_conf, text=f"信頼度: {avg_conf*100:.1f}% / 検出数: {len(confs)}個")
                st.caption(f"💊 対処法: {treatment}")
                st.divider()
