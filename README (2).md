# **README -- Word Count Analyzer Project**

## **📌 Project Title**

**Word Count Analyzer (Python Text Processing Tool)**\
*By: Alok Ranjan Nanda \| Reg No: 25BAI10778 \| Branch: CSE AIML*

## **📖 Overview**

The **Word Count Analyzer** is a Python-based text processing tool that
reads user-entered text or a text file and analyzes it by:

-   Cleaning the text (lowercasing, removing punctuation)
-   Splitting text into words
-   Counting word frequencies using `collections.Counter`
-   Displaying summary statistics
-   Showing the Top N most frequent words

This mini-project is useful for **NLP beginners**, **text
preprocessing**, and **Python learners**.

## **✨ Features**

-   🔤 Converts all text to lowercase\
-   🧹 Removes punctuation automatically\
-   🔍 Counts total & unique words\
-   📊 Displays most frequent words\
-   📁 Accepts both:
    -   Direct text input\
    -   File input\
-   ✔ Simple, clean, and easy to understand

## **🧩 Code Structure**

    ├── clean_text()          # Cleans raw text
    ├── count_words()         # Counts word frequencies
    ├── display_results()     # Shows final formatted output
    ├── analyze_text_input()  # Handles user input
    ├── analyze_file()        # Reads file and analyzes
    └── main block            # Menu-driven program start

## **💡 How It Works**

### **1. clean_text(text)**

-   Removes punctuation using `str.maketrans`
-   Converts text to lowercase\
-   Returns cleaned text

### **2. count_words(text)**

-   Splits cleaned text into words
-   Uses `Counter` to count frequency\
-   Returns a Counter object

### **3. display_results(counter, top_n)**

-   Shows total & unique word count\
-   Prints Top N most frequent words\
-   Uses formatted and coloured output

### **4. analyze_text_input()**

-   Accepts user input\
-   Analyzes the text\
-   Prints results

### **5. analyze_file(filename)**

-   Reads a text file\
-   Passes content to analyzer\
-   Handles errors (missing file)

## **📥 How to Run**

### **🔧 Requirements**

-   Python 3.x\
-   No external libraries required

### **▶ Run the Script**

    python word_analyzer.py

### **Menu Options**

    📌 Word Count Analyzer
    1. Analyze text input
    2. Analyze a text file

## **📤 Sample Output**

    📊 Word Count Analysis
    ----------------------
    Total words         : 42
    Unique words        : 28

    Top 10 Most Frequent Words:

    python          → 5
    project         → 4
    word            → 3
    analysis        → 2
    count           → 2

## **📚 Applications**

-   Natural Language Processing (NLP)
-   Text preprocessing
-   Word frequency analysis
-   Basic Python learning project
-   Data cleaning and text mining tasks

## **🧑‍💻 Author**

**Name:** *Alok Ranjan Nanda*\
**Reg No:** *25BAI10778*\
**Branch:** *CSE AIML*

## **📜 License**

This project is free to use for academic and learning purposes.
