def remove_vowels(string):
    vowels = "aeiouAEIOU"
    new_string = ""

    for char in string:
        if char not in vowels:
            new_string += char

    return new_string

print(remove_vowels("Guvi Geeks Netowork Private Limited"))
print(remove_vowels("programming"))
print(remove_vowels("aAeEiIoOUu"))