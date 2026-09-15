sentence = input("Enter a sentence: ")
symbol = input("Enter the symbol or character to display: ")

print("\n--- Output ---")

for character in sentence:
    ascii_value = ord(character)
    count = ascii_value % 15

    if count == 0:
        count = 15

    bar = symbol * count

    print(f"'{character}' (Count: {count}) -> {bar}")