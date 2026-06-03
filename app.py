import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi halaman
st.set_page_config(page_title="NR OptiVoyage Dashboard", layout="wide")

# CSS Hacking untuk menonaktifkan bingkai Streamlit di HP
st.markdown("""
    <style>
        /* 1. Reset semua margin, padding, dan block-container bawaan */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
            margin: 0 !important;
            padding: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            overflow: hidden !important;
            background-color: #0f172a !important; /* Warna dasar gelap */
        }
        
        /* 2. Sembunyikan header/footer Streamlit yang memakan ruang di HP */
        header, footer, [data-testid="stHeader"] { 
            display: none !important; 
        }
        
        /* 3. Paksa iframe HTML untuk menjadi Absolute Full Screen */
        iframe {
            position: absolute !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
            z-index: 99999 !important;
        }
    </style>
""", unsafe_allow_html=True)

html_file_path = "NR_OptiVoyage (7).html"
try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    # Memuat HTML
    components.html(html_content, height=800, scrolling=False)
except FileNotFoundError:
    st.error(f"File {html_file_path} tidak ditemukan.")
