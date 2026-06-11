import streamlit as st
from main import file_map

if "chosen_files" not in st.session_state:
    st.switch_page("main.py")
else:
    chosen_files = st.session_state["chosen_files"]
