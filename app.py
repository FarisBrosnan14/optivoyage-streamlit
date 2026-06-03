import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="NR OptiVoyage Dashboard", layout="wide")
st.title("🚢 Dashboard NR OptiVoyage")

# Membaca file HTML milikmu
html_file_path = "NR_OptiVoyage (7).html"

with open(html_file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Menampilkan HTML di dalam Streamlit
components.html(html_content, height=800, scrolling=True)