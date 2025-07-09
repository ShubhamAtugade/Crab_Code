#WAP to check the given string is pallindrome or not

strr = input('Enter a string : ')

if strr == strr[::-1]:
    print('given string is in pallindrome')
else:
    print('given string is not in pallindrome')