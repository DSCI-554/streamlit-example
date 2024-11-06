
import streamlit as st

def load_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

resources_content = load_markdown_file("./public/deploy.md")

# Display the resources content
st.markdown(resources_content)