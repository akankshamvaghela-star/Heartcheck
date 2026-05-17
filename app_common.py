from pathlib import Path

import streamlit as st

PROJECT_PDF = Path(__file__).resolve().parent / "Akanksha final (2).pdf"
PDF_DOWNLOAD_NAME = "Heart_Disease_Prediction_Project_Report.pdf"

HIDE_STREAMLIT_CHROME = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stHeader"] {display: none;}
[data-testid="stToolbar"] {display: none;}
[data-testid="stDecoration"] {display: none;}
[data-testid="stStatusWidget"] {display: none;}
.viewerBadge_container__1QSob {display: none !important;}
.viewerBadge_link__1S137 {display: none !important;}
.viewerBadge_text__1JaDK {display: none !important;}
[data-testid="stFloatingButton"] {display: none !important;}
[data-testid="stProfile"] {display: none !important;}
a[href*="streamlit.io"] {display: none !important;}
div[style*="position: fixed"][style*="bottom"] {display: none !important;}
div[data-testid="stSidebarNav"] {display: none;}
section[data-testid="stSidebar"] {display: none;}
.block-container {padding-top: 1rem;}
.app-header {
    background: linear-gradient(90deg, #7f1d1d 0%, #b91c1c 55%, #dc2626 100%);
    border-radius: 10px;
    padding: 0.85rem 1.25rem;
    margin-bottom: 1.25rem;
    color: #fff;
}
.app-header-title {
    font-size: 1.35rem;
    font-weight: 700;
    margin: 0;
}
</style>
"""


def init_navigation():
    if "nav_page" not in st.session_state:
        st.session_state.nav_page = "home"


def apply_page_config():
    st.set_page_config(page_title="Heart Disease Predictor", layout="wide", initial_sidebar_state="collapsed")


def render_chrome():
    st.markdown(HIDE_STREAMLIT_CHROME, unsafe_allow_html=True)


def render_header(current_page: str):
    st.markdown(
        """
        <div class="app-header">
            <p class="app-header-title">Heart Disease Predictor</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    nav_home, nav_about, nav_contact, _ = st.columns([1, 1.15, 1.15, 4.7], gap="small")
    with nav_home:
        if st.button(
            "Home",
            key="nav_home",
            use_container_width=True,
            type="primary" if current_page == "home" else "secondary",
        ):
            st.session_state.nav_page = "home"
            st.rerun()
    with nav_about:
        if st.button(
            "About Project",
            key="nav_about",
            use_container_width=True,
            type="primary" if current_page == "about" else "secondary",
        ):
            st.session_state.nav_page = "about"
            st.rerun()
    with nav_contact:
        if st.button(
            "Contact Us",
            key="nav_contact",
            use_container_width=True,
            type="primary" if current_page == "contact" else "secondary",
        ):
            st.session_state.nav_page = "contact"
            st.rerun()
