from transformers import pipeline
import tkinter as tk
import ttkbootstrap as ttk

# Create a sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Function to analyze the sentiment of the entered paragraph
def get_paragraph():
    # Get the text from the paragraph entry
    paragraph_text = paragraph.get("1.0", tk.END)

    # Perform sentiment analysis
    result = classifier(paragraph_text)[0]

    # Update the sentiment label based on the analysis
    sentiment_label = result["label"]
    sent_lbl.config(text=sentiment_label, bootstyle="success" if sentiment_label == "POSITIVE" else "danger")

# Create the main Tkinter window
root = ttk.Window(themename="superhero")
root.geometry("1000x800")
root.title("Sentiment Analysis Chatbot")

# Create a text entry for the user to input paragraphs
paragraph = ttk.Text(root, width=100, height=20)
paragraph.place(x=90, y=160)

# Create a button to trigger the sentiment analysis
sent_analysis = ttk.Button(root, text="Analyze Sentiment", command=get_paragraph)
sent_analysis.place(x=760, y=600)

# Create a label to guide the user
user_lbl = ttk.Label(root, text="Type Something...", font=("Arial", 18))
user_lbl.place(x=90, y=110)

# Create a label to display the sentiment analysis result
sent_lbl = ttk.Label(text="", font=("Arial", 18))
sent_lbl.place(x=90, y=600)

# Run the Tkinter event loop
root.mainloop()
