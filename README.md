# Natural Language Processing

## Table of Contents
1. [Overview](#overview)
   - [1. Question Answering (Q&A)](#1-question-answering-qa)
   - [2. Sentiment Analysis](#2-sentiment-analysis)
   - [3. Machine Translation](#3-machine-translation)
   - [4. Summarization](#4-summarization)
2. [Installation](#installation)
3. [How to use text files](#how-to-use-text-files)
4. [GUI](#gui)

## Overview

### 1. Question Answering (Q&A)
This section allows you to provide text to the question and answer system and ask it a question, receiving an answer based on the context.

**Step 1 | Set Up Answering Questions:**
   - **qa_pipeline** is a tool for answering questions. It uses a pre-trained model, specifically "distilbert-base-cased-distilled-squad," to understand and respond to user queries effectively, making it useful for applications such as virtual assistants and information retrieval.

**Step 2 | Get and Display Answers (`get_answer`):**
   - Takes the user's question and context, uses the model to find answers, and displays the result.

### 2. Sentiment Analysis
Our project understands how people feel in written text. It figures out if something is happy, sad, or different, helping with understanding reviews, comments, or user feedback.

**Step 1 | Set Up Understanding Feelings:**
   - *classifier* is a tool for analyzing sentiment in text using *pipeline("sentiment-analysis")*. It employs a pre-trained model to assess the emotional tone, making it useful for understanding sentiments expressed in customer reviews, social media comments, or user feedback.

**Step 2 | Analyze Paragraph Feelings (`get_paragraph`):**
   - Looks at the feelings in a paragraph and tells if it's positive or negative, showing this with different colors.

### 3. Machine Translation
Our project can automatically change text from one language to another, making it easier for people who speak different languages to understand each other.

**Step 1 | Set Up Default Language:**
   - In this section, we can translate English to ("fr" for French) or ("de" for Germany) language, load a pre-trained translation model, and initialize a tokenizer. It's part of a system that automatically translates text from one language to another, facilitating cross-cultural communication.

**Step 2 | Load Language Models:**
   - Gets special tools for translating based on the chosen language.

**Step 3 | Start Translating (`get_text`):**
   - Takes text and turns it into another language, showing the original and translated text.

**Step 4 | Change Language (`change_language`):**
   - Lets you change the language using a menu bar.

**Step 5 | Menu Bar for Language (`create_menu_bar`):**
   - Makes a menu where you can choose the language you want to translate to.

### 4. Summarization
In this section, you can give the model a paragraph, and it will summarize it.

**Step 1 | Set Up Summarizing:**
   - Uses a pipeline for summarization from transformers using *pipeline("summarization")*. The summarizer pipeline automatically shortens text, using pre-trained models to create concise summaries of lengthy articles or documents, a valuable tool for quick understanding and decision-making with large amounts of textual data.

**Step 2 | Get Summary (`get_paragraph`):**
   - Takes a lot of text, summarizes it, and shows the summary in a neat way.

## Installation
Stuff you need to install to make our project work:

```terminal
pip install transformers
pip install torch
pip install ttkbootstrap
```

## How to use text files
I provided some text files that you can give to each specified model to get the result as text. For example, in Summarize.txt file, you can copy its content and paste it into the entry widget of the tkinter library to get a summarized text.

## GUI
I used a Graphical User Interface (GUI) with ttkbootstrap (a library for beautiful styles in tkinter widgets) for each .py file. This allows you to visually see the result of the codes, and you can use text in entry widgets to get summarizations, translations, and more.
