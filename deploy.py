# Function to load Markdown content from a file
def load_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
    
