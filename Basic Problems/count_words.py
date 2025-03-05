def count_words(s):
    words = s.split()
    return len(words)

sentence=input("Enter a sentence: ")
word_count = count_words(sentence)
print(f"Number of words: {word_count}")