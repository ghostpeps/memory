import streamlit as st

main_page = st.Page("main.py", title="Home", icon="🏠")
game_page = st.Page("pages/game.py", title="Game", icon="🎮")

st.session_state["game_page"] = game_page

pg = st.navigation([main_page, game_page])
pg.run()
