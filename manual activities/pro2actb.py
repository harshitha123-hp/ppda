def word_count(sentence):
    words = sentence.split()  # Split sentence into words
    word_frequency = {}  # Dictionary to store word frequencies

    for word in words:
        word = word.lower()  # Convert to lowercase for case-insensitive counting
        word_frequency[word] = word_frequency.get(word, 0) + 1  # Update count

    return len(words), word_frequency  # Return total count and frequency dictionary

# Test the function
sentence = input("Enter sentence: ")
total_words, word_frequencies = word_count(sentence)

print(f"The number of words in the sentence is: {total_words}")
print("Word frequencies:")
for word, count in word_frequencies.items():
    print(f"{word}: {count}")