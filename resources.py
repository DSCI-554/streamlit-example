import streamlit as st

# Function to load Markdown content from a file
def load_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
# Load the resources Markdown content
resources_content = load_markdown_file("./public/project_resources.md")

# Display the resources content
st.markdown(resources_content)