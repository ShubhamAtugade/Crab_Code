#WAP to check char of the given string is consonant or vowel

char = input('Enter your desird character : ')

if  char in 'AEIOUaeiou':
    print(f'The first character {char} is a vowel')
else:
    print(f'The first character {char} is a consonant')
