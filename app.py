import streamlit as st
import streamlit.components.v1 as components

# Sidebar ditutup secara default agar layar HP lebih lega
st.set_page_config(page_title="NR OptiVoyage Dashboard", layout="wide", initial_sidebar_state="collapsed")

# CSS Super Agresif untuk memaksa Auto-Ratio di Layar HP
st.markdown("""
    <style>
        /* Hilangkan margin/padding Streamlit bawaan */
        .block-container {
            padding: 0rem !important;
            margin: 0rem !important;
            max-width: 100% !important;
            overflow: hidden !important;
        }
        header { display: none !important; }
        footer { display: none !important; }
        
        /* Memaksa Body sesuai Dynamic Viewport (Layar Asli HP) */
        body, html, [data-testid="stAppViewContainer"], [data-testid="stMain"] { 
            overflow: hidden !important; 
            height: 100vh !important; 
            height: 100dvh !important; 
            width: 100vw !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* Target khusus untuk Iframe Streamlit */
        iframe, div[data-testid="stHtml"] {
            display: block;
            border: none;
            width: 100vw !important;
            height: 100vh !important;
            height: 100dvh !important;
        }
    </style>
""", unsafe_allow_html=True)

html_file_path = "NR_OptiVoyage (7).html"
try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    # Tetap beri nilai fallback height, tapi CSS di atas yang akan mengambil alih secara absolut
    components.html(html_content, height=800, scrolling=False)
except FileNotFoundError:
    st.error(f"File {html_file_path} tidak ditemukan.")
