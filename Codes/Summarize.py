from transformers import pipeline
import tkinter as tk
import ttkbootstrap as ttk
import textwrap

# Create a summarization pipeline
summarizer = pipeline("summarization")

# Function to analyze the text and generate a summary
def get_paragraph():
    # Get the text from the Text widget
    paragraph_text = text.get("1.0", tk.END)

    # Perform summarization
    summary = summarizer(paragraph_text, max_length=50, min_length=5, length_penalty=2.0, num_beams=4)

    # Get the summarized text
    summarized_text = summary[0]['summary_text']

    # Break down the summarized text into lines appropriate for the width of the Text widget
    wrapped_summary = textwrap.fill(summarized_text, width=80)

    # Update the Label with the wrapped and left-justified summary
    summarized_lbl.config(text=wrapped_summary)

# Create the main Tkinter window
root = ttk.Window(themename="superhero")
root.geometry("1000x800")
root.title("Text Summarization Chatbot")

# Create a Text widget for the user to input paragraphs
text = ttk.Text(root, width=100, height=20, wrap=tk.WORD)
text.place(x=90, y=160)

# Create a button to trigger the summarization
summarize_button = ttk.Button(root, text="Summarize", command=get_paragraph)
summarize_button.place(x=805, y=110)

# Create a label to guide the user
user_lbl = ttk.Label(root, text="Type Something...", font=("Arial", 18))
user_lbl.place(x=90, y=110)

# Create a label to display the summarized text
summarized_lbl = ttk.Label(root, text="", font=("Arial", 12), wraplength=900, justify=tk.LEFT)
summarized_lbl.place(x=90, y=600)

# Run the Tkinter event loop
root.mainloop()
