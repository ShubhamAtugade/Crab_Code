#WAp to check that the given word is upper case or not. if yes return lower case else return uppercase.

word = input('Enter a word : ')

if word.isupper():
    print(word.lower())
else:
    print(word.upper())