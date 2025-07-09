
#WAP to check that the given programming language is present in the list or not

ls = ['python', 'java', 'c++', 'javascript', 'c#']

pl = input('Enter a programming language: ')

if pl.lower() in ls :
    print(f'{pl} is present in given programming list')
else:
    print(f'{pl} is not present in given programming list')