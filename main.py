# Simple Tkinter app to display HTML content using tkhtmlview
import tkinter as tk
from tkhtmlview import HTMLLabel

root = tk.Tk()
root.title("HTML in Tkinter")

# Basic HTML content
html_code = """
<h1>Hello, Tkinter!</h1>
<p>This is <b>HTML</b> rendered in a Tkinter window.</p>
<a href="https://www.python.org">Go to Python.org</a>
"""

label = HTMLLabel(root, html=html_code)
label.pack(fill="both", expand=True)

root.mainloop()
