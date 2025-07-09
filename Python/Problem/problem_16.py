#WAP to check that the datatype of the given input is individual or multvalued datatype. 

input_1 = eval(input('enter your value : '))
print(type(input_1))

if type(input_1) in [list, tuple, set, dict, str]  :
    print('the given input have Multvalued datatype')
else:
    print('the given input have individual datatype')
    
    
#note - to check for string, enclosed within quotes ''