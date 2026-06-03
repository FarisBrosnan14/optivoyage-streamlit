import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi Halaman (Lebar Penuh)
st.set_page_config(page_title="NR OptiVoyage Dashboard", layout="wide")

# 2. Injeksi CSS untuk Full Screen (Menghilangkan margin, header, dan footer)
st.markdown("""
    <style>
        /* Menghilangkan padding utama Streamlit */
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        /* Menyembunyikan elemen bawaan yang tidak diperlukan */
        header { display: none !important; }
        footer { display: none !important; }
        /* Memastikan background berwarna gelap agar menyatu */
        .stApp {
            background-color: #0e1117;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Membaca dan Menampilkan File HTML
html_file_path = "NR_OptiVoyage (7).html"
try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    # Menampilkan komponen HTML. 
    # Height diset ke 1200 untuk memastikan cukup untuk layar resolusi tinggi, 
    # scrolling dimatikan agar tidak ada scrollbar ganda.
    components.html(html_content, height=1200, scrolling=False)
except FileNotFoundError:
    st.error(f"File {html_file_path} tidak ditemukan. Pastikan nama file sama persis dan berada di satu folder.")
