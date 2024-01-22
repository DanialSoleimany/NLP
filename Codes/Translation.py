from transformers import MarianMTModel, MarianTokenizer
import torch
import tkinter as tk
from tkinter import ttk, Menu
from ttkbootstrap import Style

# Default language
default_language = "fr"
selected_language = default_language

# Load pre-trained model and tokenizer
model_name = f"Helsinki-NLP/opus-mt-en-{selected_language}"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Initialize source_sentences
source_sentences = []

# Define translation function
def get_text():
    input_text = text.get("1.0", "end-1c")  
    source_tokenized = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)

    with torch.no_grad():
        model.eval()
        outputs = model.generate(**source_tokenized, max_length=50, num_beams=4, length_penalty=2.0, no_repeat_ngram_size=3)

    # Decodes the generated output tokens back into text 
    translated_sentences = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    # Update source_sentences with the user input
    global source_sentences
    source_sentences = [input_text]

    for source, translation in zip(source_sentences, translated_sentences):
        translation_lbl.config(text=f"Source: {source}\nTranslation: {translation}")

# Function to change the translation language
def change_language(lang):
    global selected_language, model_name, tokenizer, model
    selected_language = lang
    model_name = f"Helsinki-NLP/opus-mt-en-{selected_language}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

# Function to create menu bar
def create_menu_bar():
    menu_bar = Menu(root)

    lang_menu = Menu(menu_bar, tearoff=0)
    for lang in ["fr", "de"]: 
        lang_menu.add_command(label=lang, command=lambda l=lang: change_language(l))
    menu_bar.add_cascade(label="Select Language", menu=lang_menu)

    root.config(menu=menu_bar)

# Create the main Tkinter window
style = Style(theme='superhero')
root = style.master
root.geometry("800x700")
root.title("Translation App")

# Create a text entry for the user to input paragraphs
text = tk.Text(root, width=100, height=20)
text.place(x=90, y=160)

# Create a button to trigger the translation
translate_button = ttk.Button(root, text="Translate", command=get_text)
translate_button.place(x=630, y=500)

# Create a label to guide the user
user_lbl = ttk.Label(root, text="Type Something...", font=("Arial", 18))
user_lbl.place(x=90, y=110)

# Create a label to display the translation result
translation_lbl = ttk.Label(root, text="", font=("Arial", 18))
translation_lbl.place(x=90, y=500)

# Create the language selection menu bar
create_menu_bar()

# Run the Tkinter event loop
root.mainloop()
