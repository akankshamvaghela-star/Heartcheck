import streamlit as st


def render():
    st.title("Contact Us")
    st.markdown("For questions about this project or the heart-disease prediction application, reach out using the details below.")

    st.markdown(
        """
| | |
|---|---|
| **Name** | Akanksha Vaghela |
| **Phone** | [+91 99096 39661](tel:+919909639661) |
| **Email** | [akanksham.vaghela@gmail.com](mailto:akanksham.vaghela@gmail.com) |
        """
    )

    st.info("We typically respond to email inquiries within a few business days.")
