import webview # pip install pywebview
import os
import sys
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

# Get the base path for assets when running as an executable
def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# Path to your HTML file
# html_file = os.path.abspath("index.html")

# In your Tkinter code, use this function to get the correct path
html_file = resource_path("index.html")
# Now you can use `html_file` to load your HTML content


# Open the HTML file in a webview window
webview.create_window("My Page", f"file://{html_file}", js_api=api)
webview.start()
