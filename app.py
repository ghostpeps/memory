import streamlit as st

main_page = st.Page("main.py", title="Memory Game", icon=":material/home:")
game_page = st.Page("pages/game.py", title="Memory Game", icon="🎮")

pg = st.navigation([main_page, game_page], position="hidden")
pg.run()
