import streamlit as st

if "chosen_files" not in st.session_state:
    st.switch_page("main.py")

chosen_files = st.session_state["chosen_files"]
marked_not_in_deck = st.session_state.get("marked_not_in_deck", [])
marked_in_deck = st.session_state.get("marked_in_deck", [])

st.title("Game Over")

st.subheader("Original Deck")
cols = st.columns(len(chosen_files)) if chosen_files else []
for col, f in zip(cols, chosen_files):
    col.image(f, width=120)

st.subheader("Marked as 'was in the deck'")
cols = st.columns(len(marked_in_deck)) if marked_in_deck else []
for col, f in zip(cols, marked_in_deck):
    correct = f in chosen_files
    col.image(f, width=120)
    col.markdown(f":material/{'check' if correct else 'close'}:")

st.subheader("Marked as 'was not in the deck'")
cols = st.columns(len(marked_not_in_deck)) if marked_not_in_deck else []
for col, f in zip(cols, marked_not_in_deck):
    correct = f not in chosen_files
    col.image(f, width=120)
    col.markdown(f":material/{'check' if correct else 'close'}:")

if st.button("Play Again"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.switch_page("main.py")
