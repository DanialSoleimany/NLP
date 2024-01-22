from transformers import pipeline
import tkinter as tk
import ttkbootstrap as ttk

# Create a question-answering pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Function to get and display the answer based on user input
def get_answer():
    # Get the user's question and context from input fields
    user_question = question_entry.get()
    user_context = context_text.get("1.0", tk.END)

    # Perform question-answering using the pipeline
    result = qa_pipeline(question=user_question, context=user_context)

    # Display the answer in the label
    answer_label.config(text=f"Answer: {result['answer']}")

# Create the main Tkinter window
root = ttk.Window(themename="superhero")
root.geometry("1000x800")
root.title("Question Answering Chatbot")

# Create an entry for the user to input the question
question_entry = ttk.Entry(root, width=50)
question_entry.place(x=90, y=160)

# Create a text field for the user to input the context
context_text = ttk.Text(root, width=100, height=10)
context_text.place(x=90, y=200)

# Create a button to trigger question-answering
qa_button = ttk.Button(root, text="Get Answer", command=get_answer)
qa_button.place(x=810, y=430)

# Create a label to display the answer
answer_label = ttk.Label(root, text="", font=("Arial", 16))
answer_label.place(x=90, y=430)

# Run the Tkinter event loop
root.mainloop()
