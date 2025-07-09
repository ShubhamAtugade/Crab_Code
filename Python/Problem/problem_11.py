#WAP to check that the number is divisible by 2 and 5, and convert that number into complex

num = int(input('Enter a desired number : '))\
    
if num % 2 == 0 and num % 5 == 0 :
    print(complex(num))
elif num%2 == 0:
    print(f'Enter valid number. {num} is  divisible by 2 but not divisble by 5')
elif num%5 == 0:
    print(f'Enter valid number. {num} is  divisible by 5 but not divisble by 2')
else:
    print(f'Enter valid number. {num} is not divisible by 2 but not divisble by 5')
