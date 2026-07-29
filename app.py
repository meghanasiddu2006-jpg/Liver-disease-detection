import streamlit as st
from prediction import predict_liver_disease
import base64
import os

# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="Liver Disease Detection",
    page_icon="🩺",
    layout="wide"
)
# ---------------------------------------
# Banner Image Function
# ---------------------------------------

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

banner = get_base64("images/banner.jpeg")
st.markdown(f"""
<style>

header {{
    visibility:hidden;
}}

footer {{
    visibility:hidden;
}}

#MainMenu {{
    visibility:hidden;
}}

.stApp{{
    background:#F4F8FC;
}}

.banner{{
    background-image:url("data:image/jpeg;base64,{banner}");
    background-size:cover;
    background-position:center;
    border-radius:20px;
    padding:50px;
    height:220px;
    display:flex;
    align-items:center;
}}

.banner h1{{
    color:white;
    font-size:48px;
    margin-bottom:10px;
}}

.banner p{{
    color:white;
    font-size:22px;
}}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="banner">

<div>

<h1>🩺 Liver Disease Detection System</h1>

<p>
AI Powered Early Detection using Machine Learning
</p>

</div>

</div>
""", unsafe_allow_html=True)
# ===========================================
# Main Layout
# ===========================================

left, right = st.columns([1,2], gap="large")
with left:

    st.markdown("""
    <div style="
        background:white;
        border-radius:20px;
        padding:20px;
        box-shadow:0px 5px 15px rgba(0,0,0,0.15);
        text-align:center;
    ">
    """, unsafe_allow_html=True)

    st.image("images/liver.jpg", use_container_width=True)

    st.markdown(
        "<h3 style='color:#0A4D8C;'>🫀 About This System</h3>",
        unsafe_allow_html=True
    )

    st.write("""
This application predicts liver disease
using an Artificial Intelligence &
Machine Learning model.

It helps doctors and patients
identify liver disease at an early stage.
""")

    st.success("✔ Early Detection Saves Lives")

    st.markdown("</div>", unsafe_allow_html=True)
with right:

    st.markdown("""
    <div style="
        background:white;
        padding:25px;
        border-radius:15px;
        box-shadow:0px 0px 10px rgba(0,0,0,0.15);
    ">
    """, unsafe_allow_html=True)

    st.subheader("👤 Patient Details")

    # -----------------------
    # Inputs INSIDE right card
    # -----------------------

    c1, c2 = st.columns(2)

    with c1:

        age = st.number_input("👤 Age", 1, 120, 30)

        gender = st.selectbox(
            "🚻 Gender",
            ["Male", "Female"]
        )

        total_bilirubin = st.number_input(
            "🧪 Total Bilirubin",
            value=1.0
        )

        direct_bilirubin = st.number_input(
            "🧪 Direct Bilirubin",
            value=0.3
        )

        alkaline_phosphotase = st.number_input(
            "🩺 Alkaline Phosphotase",
            value=200
        )

    with c2:

        alt = st.number_input("🧬 ALT", value=30)

        ast = st.number_input("🧬 AST", value=40)

        total_proteins = st.number_input(
            "🥛 Total Proteins",
            value=6.5
        )

        albumin = st.number_input(
            "💉 Albumin",
            value=3.5
        )

        ag_ratio = st.number_input(
            "⚖️ Albumin / Globulin Ratio",
            value=1.0
        )

    predict = st.button(
    "🔍 Predict Liver Disease",
    use_container_width=True,
    type="primary"
)
if predict:

    prediction, confidence = predict_liver_disease(
        age,
        gender,
        total_bilirubin,
        direct_bilirubin,
        alkaline_phosphotase,
        alt,
        ast,
        total_proteins,
        albumin,
        ag_ratio
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("## 📊 Prediction Result")
    if prediction == 1:

        st.success("✅ No Liver Disease Detected")

    else:

        st.error("❌ Liver Disease Detected")
        st.metric(
        label="Prediction Confidence",
        value=f"{confidence:.2f}%"
    )

    st.progress(int(confidence))

st.markdown("---")

st.markdown("""
<style>
.footer-box{
    background: linear-gradient(90deg,#0A4D8C,#1565C0);
    padding:18px;
    border-radius:15px;
    color:white;
    text-align:center;
    margin-top:20px;
}

.footer-box h3{
    color:white;
    margin:8px 0;
    font-size:30px;
}

.footer-box p{
    color:white;
    font-size:18px;
    margin:4px 0;
    line-height:1.5;
}

.footer-box hr{
    border:1px solid rgba(255,255,255,0.3);
    margin:15px 0;
}

.models{
    display:flex;
    justify-content:center;
    flex-wrap:wrap;
    gap:10px;
    margin-top:12px;
    margin-bottom:12px;
}

.model{
    background:white;
    color:#0A4D8C;
    padding:8px 16px;
    border-radius:25px;
    font-weight:bold;
    font-size:15px;
}

.names{
    font-size:18px;
    font-weight:bold;
    margin-top:8px;
}

.college{
    font-size:17px;
    margin-top:4px;
}

.copy{
    font-size:15px;
    margin-top:8px;
    opacity:0.9;
}
</style>

<div class="footer-box">

<h3>🤖 Machine Learning Models Used</h3>

<div class="models">
<div class="model">Logistic Regression</div>
<div class="model">Decision Tree</div>
<div class="model">⭐ Random Forest</div>
<div class="model">SVM</div>
<div class="model">XGBoost</div>
</div>

<hr>

<h3>👩‍💻 Developed By</h3>

<div class="names">
Rakshitha M • Abhinaya M • Meghana • Kavyashree B C
</div>

<div class="college">
Department of Computer Science & Engineering
</div>

<div class="college">
Maharaja Institute of Technology Thandavapura
</div>

<hr>

<div class="copy">
© 2026 Liver Disease Detection System | Capstone AIML-Project
</div>

</div>
""", unsafe_allow_html=True)