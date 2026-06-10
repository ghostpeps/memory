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

available_numbers = list(file_map.keys())
random_numbers = random.sample(available_numbers, 3)
chosen_files = [file_map[num] for num in random_numbers]

st.title("The Memory Game")
st.subheader("literally just a memory game")
st.text("just memorize cards and you'll be good")
c1, c2, c3 = st.columns(3)
easy = c1.button("Easy", icon=":material/chess_pawn:", width="stretch")
medium = c2.button("Medium", icon=":material/chess_knight:", width="stretch")
hard = c3.button("Hard", icon=":material/chess_queen:", width="stretch")

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
for file in chosen_files:
    # Split the row into two columns (e.g., 1 part image, 2 parts text)
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(file, width=1)
        
    with col2:
        st.subheader("Image Title")
        st.write("This description stays perfectly aligned with the image to its left.")
