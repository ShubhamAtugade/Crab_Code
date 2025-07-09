#WAP to check wheather the given string is in upper case or not

strr = input('enter a string : ')

if bool(strr.isupper()) == True:
    print(f'The string {strr} is in upper case')
else:
    print(f'The string {strr} is not in upper case')
    