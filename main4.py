import webview
import os
from tkinter import filedialog

class Api:
    def download_text(self):
        text_data = "Hello, this is a string from Python!"
        
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

# ✅ You must pass js_api=api here
window = webview.create_window("My Page", f"file://{html_file}", js_api=api)
webview.start()
