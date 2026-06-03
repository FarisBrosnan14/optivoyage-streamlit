import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi halaman utama (Favicon diubah ke pertamina.png di sini)
st.set_page_config(page_title="NR OptiVoyage Dashboard", page_icon="pertamina.png", layout="wide", initial_sidebar_state="collapsed")

# CSS Paksaan agar Streamlit benar-benar Full Screen 100% tanpa sisa hitam
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        header, footer { 
            display: none !important; 
        }
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
            overflow: hidden !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        iframe {
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
            display: block !important;
        }
    </style>
""", unsafe_allow_html=True)

html_file_path = "NR_OptiVoyage (7).html"
try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    components.html(html_content, height=2000, scrolling=False)
except FileNotFoundError:
    st.error(f"File {html_file_path} tidak ditemukan. Pastikan namanya sesuai.")
