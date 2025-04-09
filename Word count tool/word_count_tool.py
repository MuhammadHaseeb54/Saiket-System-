# Task 6
# Word Count Tool

import string
from collections import Counter

# Read file content 
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f" File not found: {file_path}")
    except UnicodeDecodeError:
        print(f" Encoding error reading the file: {file_path}")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")
    return None  # Return None on failure

# Count lines, words, characters
def count_basic_stats(text):
    try:
        lines = text.splitlines()
        num_lines = len(lines)
        num_words = len(text.split())
        num_chars = len(text)
        return num_lines, num_words, num_chars
    except Exception as e:
        print(f" Error in counting statistics: {e}")
        return 0, 0, 0

# Word frequency analysis
def word_frequency(text):
    try:
        translator = str.maketrans('', '', string.punctuation)
        clean_text = text.lower().translate(translator)
        word_list = clean_text.split()
        return Counter(word_list)
    except Exception as e:
        print(f" Error in frequency analysis: {e}")
        return Counter()

# Display results
def display_results(lines, words, chars, freq, top_n=10):
    try:
        print("\n=== Text Analysis Summary ===")
        print(f" Lines: {lines}")
        print(f" Words: {words}")
        print(f" Characters: {chars}")

        print("\n Top", top_n, "most frequent words:")
        for word, count in freq.most_common(top_n):
            print(f"  {word}: {count}")
    except Exception as e:
        print(f" Error displaying results: {e}")

file_path = 'sample.txt'  
text = read_file(file_path)

if text:
    lines, words, chars = count_basic_stats(text)
    freq = word_frequency(text)
    display_results(lines, words, chars, freq)
else:
    print(" Analysis aborted due to file read error.")
