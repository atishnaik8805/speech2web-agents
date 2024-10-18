import streamlit as st
from st_pages import add_page_title, get_nav_from_toml

# Set the page configuration
st.set_page_config(page_title="Speech2Web", layout="centered")

nav = get_nav_from_toml()

# st.logo("logo.png")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()

