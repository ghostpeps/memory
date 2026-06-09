import streamlit as st
import time

st.title("The Memory Game")
st.subheader("literally just a memory game")
st.text("just memorize cards and you'll be good")
c1, c2, c3 = st.columns(3)
easy = c1.button("Easy", icon=":material/chess_pawn:", width="stretch")
medium = c2.button("Medium", icon=":material/chess_knight:", width="stretch")
hard = c3.button("Hard", icon=":material/chess_queen:", width="stretch")
