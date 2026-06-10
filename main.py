import streamlit as st
import time
import random

file_map = {
    1: "EARTH.png",
    2: "ELEPHANT.png",
    3: "FISH.png",
    4: "HUMAN.png",
    5: "ROBOT.png",
    6: "SHARK.png",
    7: "SUN.png",
    8: "TRAIN.png",
    9: "TREE.png",
}

if "difficulty_chosen" not in st.session_state:
    st.session_state.difficulty_chosen = False

def select_difficulty():
    st.session_state.difficulty_chosen = True

available_numbers = list(file_map.keys())
random_numbers = random.sample(available_numbers, 3)
chosen_files = [file_map[num] for num in random_numbers]

st.title("The Memory Game")
st.subheader("literally just a memory game")
st.text("just memorize the cards and you'll be good")
cards = 0
c1, c2, c3 = st.columns(3)
easy = c1.button("Easy", on_click=select_difficulty, icon=":material/chess_pawn:", disabled=st.session_state.difficulty_chosen, width="stretch")
medium = c2.button("Medium", on_click=select_difficulty, icon=":material/chess_knight:", disabled=st.session_state.difficulty_chosen, width="stretch")
hard = c3.button("Hard", on_click=select_difficulty, icon=":material/chess_queen:", disabled=st.session_state.difficulty_chosen, width="stretch")

if easy:
    cards = 3
    available_numbers = list(file_map.keys())
    random_numbers = random.sample(available_numbers, 3)
    chosen_files = [file_map[num] for num in random_numbers]
if medium:
    cards = 5
    available_numbers = list(file_map.keys())
    random_numbers = random.sample(available_numbers, 5)
    chosen_files = [file_map[num] for num in random_numbers]
if hard:
    cards = 7
    available_numbers = list(file_map.keys())
    random_numbers = random.sample(available_numbers, 7)
    chosen_files = [file_map[num] for num in random_numbers]
if cards == 3:
    col1, col2, col3 = st.columns(cards)
    col1.image(chosen_files[0])
    col2.image(chosen_files[1])
    col3.image(chosen_files[2])
elif cards == 5:
    col1, col2, col3, col4, col5 = st.columns(cards)
    col1.image(chosen_files[0])
    col2.image(chosen_files[1])
    col3.image(chosen_files[2])
    col4.image(chosen_files[3])
    col5.image(chosen_files[4])
elif cards == 7:
    col1, col2, col3, col4, col5, col6, col7 = st.columns(cards)
    col1.image(chosen_files[0])
    col2.image(chosen_files[1])
    col3.image(chosen_files[2])
    col4.image(chosen_files[3])
    col5.image(chosen_files[4])
    col6.image(chosen_files[5])
    col7.image(chosen_files[6])

if st.session_state.difficulty_chosen == True:
    countdown_placeholder = st.empty()
    for s in range(10, -1, -1):
        countdown_placeholder.subheader(f"You have {s} seconds left to memorize your cards.")
        time.sleep(1)
