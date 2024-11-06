import streamlit as st

home_page = st.Page("home.py", title="Home")
rubric_page = st.Page("rubric.py", title="Rubrics")
resources_page = st.Page("resources.py", title="Resources")
deploy_page = st.Page("deploy.py", title="Deployment Instructions")

pg = st.navigation([home_page, rubric_page, resources_page, deploy_page])
st.set_page_config(page_title="DSCI 554 Final Project")
pg.run()

