import streamlit as st
from main import file_map

if "chosen_files" not in st.session_state:
    st.switch_page("main.py")
else:
    chosen_files = st.session_state["chosen_files"]


if "lives" not in st.session_state:
    st.session_state.lives = 3

def remove_life():
    if st.session_state.lives > 0:
        st.session_state.lives -= 1

heart_icons = ""
for i in range(3):
    if i < st.session_state.lives:
        icon = "favorite"
    else:
        icon = "heart_broken"
    heart_icons += f'''<span class="material-symbols-outlined" style="
        color: red;
        font-size: 60px;
        font-variation-settings: 'FILL' 1;
    ">{icon}</span> '''

st.markdown(f"""
<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Symbols+Outlined" />
<div>{heart_icons}</div>
""", unsafe_allow_html=True)

if st.button("Lose a life", on_click=remove_life):
    pass
