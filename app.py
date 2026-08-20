"""
Second Brain Agent - Multi-format Desktop App Interface
"""

import os
import streamlit as st
from scanner import DocumentScanner
from brain import SecondBrain

st.set_page_config(page_title="Second Brain Agent", page_icon="🧠", layout="centered")

st.title("🧠 Second Brain Agent")
st.caption("Tavs proaktīvais stila un dokumentu šablonu asistents")

# API atslēgas ievade sānu joslā
with st.sidebar:
    st.header("⚙️ Iestatījumi")
    api_key = st.text_input("Gemini API Key", type="password", value=os.getenv("GEMINI_API_KEY", ""))
    st.markdown("---")
    st.markdown("**Statuss:** Gatavs darbam 🟢")

# 1. Solis: Failu ielāde (Drop Zone)
st.subheader("📁 1. solis: Ielādē savus parauga dokumentus")
uploaded_files = st.file_uploader(
    "Ievelc šeit iepriekšējos failus (.docx, .pdf, .xlsx, .txt, .md)", 
    accept_multiple_files=True,
    type=["docx", "pdf", "xlsx", "txt", "md"]
)

# Saglabājam sesijas atmiņā stila profilu
if "style_profile" not in st.session_state:
    st.session_state.style_profile = ""

if uploaded_files and api_key:
    if st.button("🔍 Analizēt manu Stila DNA"):
        with st.spinner("Sintezējam Tavu rokrakstu, struktūru un paradumus..."):
            try:
                doc_texts = [
                    DocumentScanner.extract_text_from_file(file) 
                    for file in uploaded_files
                ]
                doc_texts = [text for text in doc_texts if text.strip()]
                
                if not doc_texts:
                    st.warning("Failos netika atrasts teksts!")
                else:
                    brain = SecondBrain(api_key=api_key)
                    profile = brain.extract_style_profile(doc_texts)
                    st.session_state.style_profile = profile
                    st.success(f"✅ Stila profils veiksmīgi izveidots no {len(doc_texts)} failiem!")
            except Exception as e:
                st.error(f"Kļūda: {e}")

if st.session_state.style_profile:
    with st.expander("📊 Apskatīt Tavu Stila Profilu (Style DNA)"):
        st.markdown(st.session_state.style_profile)

    st.markdown("---")
    # 2. Solis: Jauna dokumenta ģenerēšana
    st.subheader("✍️ 2. solis: Ģenerē jaunu karkasu")
    task_input = st.text_area(
        "Ko Tev nepieciešams sagatavot?", 
        placeholder="Piemēram: Sagatavo komercpiedāvājumu jaunam klientam..."
    )

    if st.button("⚡ Izveidot melnrakstu"):
        if task_input.strip():
            with st.spinner("Ģenerējam dokumentu Tavā autentiskajā stilā..."):
                brain = SecondBrain(api_key=api_key)
                draft = brain.generate_draft(task_description=task_input, style_profile=st.session_state.style_profile)
                st.subheader("📑 Rezultāts:")
                st.markdown(draft)
        else:
            st.warning("Lūdzu, ievadi uzdevuma aprakstu!")
