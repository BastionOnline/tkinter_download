

import webview
import os

# Path to your HTML file
html_file = os.path.abspath("index.html")

# Open the HTML file in a webview window
webview.create_window("My Page", f"file://{html_file}")
webview.start()
