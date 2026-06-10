import streamlit as st
import time
import random
import streamlit.components.v1 as components

main_page = st.Page("main.py", title="Home", icon="🏠")
game_page = st.Page("pages/game.py", title="Game", icon="🎮")

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


if st.session_state.difficulty_chosen:
    # 1. This displays a visual live countdown in the UI using JavaScript
    countdown_html = """
    <div style="font-family: sans-serif; font-weight: bold; font-size: 1.25rem; color: #31333F; margin-top: 20px;">
        You have <span id="timer">10</span> seconds left to memorize your cards.
    </div>
    <script>
        let timeLeft = 10;
        let timerElem = document.getElementById('timer');
        let interval = setInterval(function() {
            timeLeft--;
            timerElem.textContent = timeLeft;
            if (timeLeft <= 0) {
                clearInterval(interval);
            }
        }, 1000);
    </script>
    """
    components.html(countdown_html, height=60)
    
    # 2. This invisible snippet triggers the Streamlit page switch after exactly 10 seconds 
    # without causing intermediate Python state resets!
    redirect_html = """
    <script>
        setTimeout(function() {
            window.parent.postMessage({
                type: 'streamlit:set_page_url',
                pageName: 'game'
            }, '*');
        }, 10000);
    </script>
    """
    components.html(redirect_html, height=0, width=0)
    st.switch_page(game_page)
