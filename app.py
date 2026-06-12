import streamlit as st

main_page = st.Page("main.py", title="Memory Game", icon=":material/home:")
game_page = st.Page("pages/game.py", title="Memory Game", icon=":material/playing_cards:")
end_page = st.Page("pages/end.py", title="Memory Game", icon=":material/equalizer:")

pg = st.navigation([main_page, game_page, end_page], position="hidden")
pg.run()
