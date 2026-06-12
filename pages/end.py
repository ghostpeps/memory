# pages/end.py
import streamlit as st
from collections import Counter

if "chosen_files" not in st.session_state:
    st.switch_page("main.py")

chosen_files = st.session_state["chosen_files"]
marked_not_in_deck = st.session_state.get("marked_not_in_deck", [])
marked_in_deck = st.session_state.get("marked_in_deck", [])

st.title("Game Over")

def chunk(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]

def display_grouped(file_list, deck, correct_fn):
    counts = Counter(file_list)
    unique_files = list(counts.keys())
    for row in chunk(unique_files, 10):
        cols = st.columns(len(row))
        for col, f in zip(cols, row):
            count = counts[f]
            correct = correct_fn(f, deck)
            icon = "check" if correct else "close"
            label = "Correct" if correct else "Wrong"
            col.image(f, width=120)
            col.markdown(f":material/{icon}: {label} x{count}")

st.subheader("Original Deck")
deck_counts = Counter(chosen_files)
unique_deck = list(deck_counts.keys())
for row in chunk(unique_deck, 10):
    cols = st.columns(len(row))
    for col, f in zip(cols, row):
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
