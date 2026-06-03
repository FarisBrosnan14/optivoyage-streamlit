import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="NR OptiVoyage Dashboard", layout="wide")

# CSS untuk mematikan fungsi scroll pada Streamlit
st.markdown("""
    <style>
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
            overflow: hidden !important;
        }
        header { display: none !important; }
        footer { display: none !important; }
        body, html { overflow: hidden !important; }
        iframe {
            display: block;
            border: none;
            height: 100vh !important;
            width: 100vw !important;
        }
    </style>
""", unsafe_allow_html=True)

html_file_path = "NR_OptiVoyage (7).html"
try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=1000, scrolling=False)
except FileNotFoundError:
    st.error(f"File {html_file_path} tidak ditemukan.")
