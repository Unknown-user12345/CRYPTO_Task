alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
reverse = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

ciphertext = input("Enter ciphertext: ")

result = ""
for c in ciphertext:
    if c.upper() in alphabet:
        position = alphabet.index(c.upper())
        new_letter = reverse[position]
        if c.islower():
            new_letter = new_letter.lower()
        result = result + new_letter
    else:
        result = result + c

print(result)
