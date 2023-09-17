def count_words(string):
    words = string.split()
    return len(words)
print(count_words("Hello world"))
print(count_words("This is a sentence"))
print(count_words("I love programming"))