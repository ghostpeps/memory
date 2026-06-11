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

heart_display = ""
for i in range(3):
    if i < st.session_state.lives:
        heart_display += ":red[:material/favorite:] "
    else:
        heart_display += ":red[:material/heart_broken:] "

st.markdown(heart_display)

if st.button("Lose a life", on_click=remove_life):
    pass
