import streamlit as st

home_page = st.Page("home.py", title="Home")
deploy_page = st.Page("deploy.py", title="Deployment Instructions")

pg = st.navigation([home_page, deploy_page])
st.set_page_config(page_title="DSCI 554 Final Project")
pg.run()

