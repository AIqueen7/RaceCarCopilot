import streamlit as st

def show_card(title, content):
    st.subheader(title)
    st.write(content)