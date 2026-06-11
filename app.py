import streamlit as st

main_page = st.Page("main.py", title="Home", icon="🏠")
game_page = st.Page("pages/game.py", title="Game", icon="🎮")

pg = st.navigation([main_page, game_page])
pg.run()
