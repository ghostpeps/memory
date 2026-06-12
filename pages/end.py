import streamlit as st

st.write("Cards you said were NOT in the deck:", st.session_state.marked_not_in_deck)
st.write("Cards you said were IN the deck:", st.session_state.marked_in_deck)
