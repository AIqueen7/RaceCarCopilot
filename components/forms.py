import streamlit as st

def input_form(fields):
    data = {}
    for f in fields:
        data[f] = st.text_input(f)
    return data