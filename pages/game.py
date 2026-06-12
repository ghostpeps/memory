import streamlit as st
from config import file_map
import random
import time

if "chosen_files" not in st.session_state:
    st.switch_page("main.py")
else:
    chosen_files = st.session_state["chosen_files"]

if "lives" not in st.session_state:
    st.session_state.lives = 3

if st.session_state.lives <= 0:
    st.switch_page("pages/end.py")

if "card_chosen" not in st.session_state:
    st.session_state.card_chosen = random.randint(1, 20)

if "deadline" not in st.session_state:
    st.session_state.deadline = time.time() + 5

if "marked_not_in_deck" not in st.session_state:
    st.session_state.marked_not_in_deck = []

if "marked_in_deck" not in st.session_state:
    st.session_state.marked_in_deck = []

def remove_life():
    if st.session_state.lives > 0:
        st.session_state.lives -= 1

def next_card():
    st.session_state.card_chosen = random.randint(1, 20)

def reset_timer():
    st.session_state.deadline = time.time() + 5

c1, c2 = st.columns([1, 2])

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
""", unsafe_allow_html=True)

@st.fragment(run_every=1)
def countdown():
    remaining = st.session_state.deadline - time.time()
    if remaining <= 0:
        remove_life()
        next_card()
        reset_timer()
        st.rerun()
    else:
        if int(remaining) + 1 == 1:
            st.title(f"{int(remaining) + 1} second remaining")
        else:
            st.title(f"{int(remaining) + 1} seconds remaining")

with c2:
    countdown()

card_chosen = st.session_state.card_chosen
card_file = file_map[card_chosen]

col1, col2, col3 = st.columns(3)

col2.image(card_file, width=250)

def handle_not_in_deck():
    st.session_state.marked_not_in_deck.append(card_file)
    if card_file in chosen_files:
        remove_life()
    next_card()
    reset_timer()

def handle_in_deck():
    st.session_state.marked_in_deck.append(card_file)
    if card_file not in chosen_files:
        remove_life()
    next_card()
    reset_timer()

col1.button("was not in the deck", on_click=handle_not_in_deck, shortcut="Left")
col3.button("was in the deck", on_click=handle_in_deck, shortcut="Right")
