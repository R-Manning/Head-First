vowels = ['a','e','i','o','u']
found = []
word = "Milliways"
for letter in word:
    if letter in vowels:
            if letter not in found:
                    found.append(letter)

print(found)
