import webview
import os
from tkinter import filedialog

# Backend class with Python methods callable from JS
class Api:
    def download_text(self):
        text_data = "Hello, this is a string from Python!"
        
        # Ask user where to save the file
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )
        
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(text_data)
            return "File saved successfully."
        else:
            return "Download canceled."

api = Api()

# Path to your HTML file
html_file = os.path.abspath("index.html")

# Open the HTML file in a webview window
webview.create_window("My Page", f"file://{html_file}", js_api=api)
webview.start()
