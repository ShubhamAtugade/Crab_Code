##WAP to check first and last char of the given string is consonant or vowel

strr = input('Enter your desird character : ')

if  strr[0] in 'AEIOUaeiou' and strr[-1] in 'AEIOUaeiou':
    print(f'The first and last character {strr} is a vowel')
else:
    print(f'The first or last character {strr} is a consonant')


