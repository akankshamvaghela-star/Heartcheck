import streamlit as st

import app_common
import page_about
import page_contact
import page_home

app_common.apply_page_config()
app_common.init_navigation()
app_common.render_chrome()
app_common.render_header(st.session_state.nav_page)

if st.session_state.nav_page == "about":
    page_about.render()
elif st.session_state.nav_page == "contact":
    page_contact.render()
else:
    page_home.render()
