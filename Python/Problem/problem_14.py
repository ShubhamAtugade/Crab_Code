#WAp to check that the number is off or even. if odd then add 1 to that number and make it even  else make a square of that number.

num = int(input('Enter a number : '))

if num %2 == 0 :
    print('Number is even', num**2)
else:
    print('Number is odd', num+1)