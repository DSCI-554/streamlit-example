import streamlit as st

# Function to load Markdown content from a file
def load_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Load the rubric Markdown content
rubric_content = load_markdown_file("./public/project-rubric.md")

# Display the rubric content
st.markdown(rubric_content)
