import streamlit as st
from main import file_map
import random

if "chosen_files" not in st.session_state:
    st.switch_page("main.py")
else:
    chosen_files = st.session_state["chosen_files"]

c1, c2 = st.columns([1, 2])

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
    heart_icons += f'''<span class="material-symbols-rounded" style="
        color: red;
        font-size: 60px;
        font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 48;
    ">{icon}</span> '''

c1.markdown(f"""
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
<div>{heart_icons}</div>
""", unsafe_allow_html=True, text_alignment="justify")

c2.title("The Memory Game", text_alignment="justify")

card_chosen = random.randint(1, 9)
st.image(file_map[card_chosen], width=250)

col1, col2 = st.columns(2)
if col1.button("was not in the deck", shortcut="Left") and card_chosen in chosen_files:
    remove_life()
if col2.button("was in the deck", shortcut="Right") and card_chosen not in chosen_files:
    remove_life()
