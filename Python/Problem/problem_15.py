#WAP to check that the string is staring with uppercase or not. if not then covert whole sting to title case else lowercase.

strr = input('Enter a string : ')

if 'A' <= strr[0] <= 'Z':
    print(strr.lower())
else:
    print(strr.title())