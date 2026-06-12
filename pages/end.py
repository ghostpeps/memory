# pages/end.py
import streamlit as st
from collections import Counter

if "chosen_files" not in st.session_state:
    st.switch_page("main.py")

chosen_files = st.session_state["chosen_files"]
marked_not_in_deck = st.session_state.get("marked_not_in_deck", [])
marked_in_deck = st.session_state.get("marked_in_deck", [])

st.title("Game Over")

def display_grouped(file_list, deck, correct_fn):
    counts = Counter(file_list)
    unique_files = list(counts.keys())
    cols = st.columns(len(unique_files)) if unique_files else []
    for col, f in zip(cols, unique_files):
        count = counts[f]
        correct = correct_fn(f, deck)
        icon = "check" if correct else "close"
        label = "Correct" if correct else "Wrong"
        color = "green" if correct else "red"
        col.image(f, width=120)
        col.markdown(f":{color}[:material/{icon}:] {label} x{count}")

st.subheader("Original Deck")
deck_counts = Counter(chosen_files)
unique_deck = list(deck_counts.keys())
cols = st.columns(len(unique_deck)) if unique_deck else []
for col, f in zip(cols, unique_deck):
    count = deck_counts[f]
    col.image(f, width=120)
    if count > 1:
        col.markdown(f"x{count}")

st.subheader("Marked as 'was in the deck'")
display_grouped(marked_in_deck, chosen_files, lambda f, deck: f in deck)

st.subheader("Marked as 'was not in the deck'")
display_grouped(marked_not_in_deck, chosen_files, lambda f, deck: f not in deck)

if st.button("Play Again"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.switch_page("main.py")
