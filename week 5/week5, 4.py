def count_unique_characters(string):
    unique_chars = set(string)
    return len(unique_chars)

# Testing the function
print(count_unique_characters("hello"))
print(count_unique_characters("programming"))
print(count_unique_characters("playstation"))