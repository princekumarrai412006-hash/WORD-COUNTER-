import string
from collections import Counter

def clean_text(text: str) -> str:
    """Remove punctuation and convert text to lowercase."""
    translator = str.maketrans("", "", string.punctuation)
    return text.lower().translate(translator)


def count_words(text: str) -> Counter:
    """Return a Counter object with word frequencies."""
    cleaned = clean_text(text)
    words = cleaned.split()
    return Counter(words)


def display_results(counter: Counter, top_n: int = 10):
    """Display word frequency results."""
    total_words = sum(counter.values())
    unique_words = len(counter)

    print("\n📊 Word Count Analysis")
    print("----------------------")
    print(f"Total words         : {total_words}")
    print(f"Unique words        : {unique_words}")
    
    print(f"\nTop {top_n} Most Frequent Words:\n")
    for word, freq in counter.most_common(top_n):
        print(f"{word:<15} → {freq}")


def analyze_text_input():
    text = input("Enter the text you want to analyze:\n>>> ")
    counter = count_words(text)
    display_results(counter)


def analyze_file(filename: str):
    """Analyze a text file for word frequency."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
        counter = count_words(text)
        display_results(counter, top_n=15)
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    print("📌 Word Count Analyzer")
    print("1. Analyze text input")
    print("2. Analyze a text file")

    choice = input("Choose an option (1/2): ")

    if choice == "1":
        analyze_text_input()
    elif choice == "2":
        file_name = input("Enter filename (with extension): ")
        analyze_file(file_name)
    else:
        print("Invalid choice. Exiting.")