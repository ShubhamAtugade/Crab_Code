#WAP to check that the middle element of a given list is string of even length and first char as Vowel

lst = eval(input('Enter a list : '))

mid =  int(len(lst)//2)

if type(lst[mid]) is str and len(lst[mid])%2 ==0 and lst[mid[0]] in 'AEIOUaeiou':
    print('All conditions satisfied')
else:
    print('Condition not satisfied')