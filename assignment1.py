## A terminal based calculator application which prompts the user to enter a mathematical expression htat includes three integer values and two operators.
## 

<<<<<<< HEAD
def myAdd(x, y):
    return(x + y)
    
def mySub(x, y):
    return (x - y)

def myMul(x,y):
    return (x * y)

def myDiv(x, y):
    return (x // y)
=======

def myMul(x, y):
    return x * y

def myDiv(x, y):
    return x // y

def myAdd(x, y):
    return x + y
    
def mySub(x, y):
    return x - y
>>>>>>> 3156288955ed395c0926365ff1e11f7f337c9999




## This function validates integer input
def input_int():
    while True:
        try:
            x = int(input("Enter an integer: "))
            return x
        except ValueError:
            print('\nPlease enter an integer only.\n')
            


def input_op(x):
    while x not in {'*', '/', '+', '-'}:
        x = input("\n\nSelection invalid. Choose a number from the list. \n\nSelect an operator:\n*\t/\t+\t-\n")
        return x


print("\nSelect three integers and 2 operators as requested.\n")


a = input_int()
print('\na =', a)

operator1 = input("\nSelect an operator:\n*\t/\t+\t-\n")
input_op(operator1)
if operator1 == '*':
    print('\nOperation 1: Multiply\n')
elif operator1 == '/':
    print('\nOperation 1: Divide\n')
elif operator1 == '+':
    print('\nOperation 1: Add\n')
elif operator1 == '-':
    print('\nOperation 1: Subtract\n')

b = input_int()
print('\nb =', b)
if operator1 == '2' and b == 0:  ### if dividing by zero, print 'undefined' and ask for new integer.
        b = int(input('Undefined. Select an integer greater than 0 for valid operation:\n'))
print('\nb =', b)

operator2 = input("\nSelect an operator:\n*\t/\t+\t-\n")
input_op(operator2)
if operator2 == '*':
    print('\nOperation 2: Multiply\n')
elif operator2 == '/':
    print('\nOperation 2: Divide\n')
elif operator2 == '+':
    print('\nOperation 2: Add\n')
elif operator2 == '-':
    print('\nOperation 2: Subtract\n')

c = input_int()
if operator2 == '2' and c == 0:     ### if dividing by zero, print 'undefined' and ask for new integer.
        c = int(input('Undefined. Select an integer greater than 0 for valid operation:\n'))
print('\nc =', c)


<<<<<<< HEAD
if (operator1 == '1'):
    first_operation = myMul(a,b)
    if (operator2 == '1'):
        second_operation = myMul(first_operation,c)
        print('Entered experssion =', a, '*', b, '*', c)
    elif(operator2 == '2'):
        econd_operation = myDiv(first_operation,c)
        print('Entered experssion =', a, '*', b, '/', c)
    elif(operator2 == '3'):
        second_operation = myAdd(first_operation,c)
        print('Entered experssion =', a, '*', b, '+', c)
    elif(operator2 == '4'):
        second_operation = mySub(first_operation,c)
        print('Entered experssion =', a, '*', b, '-', c)

if (operator1 == '2'):
    first_operation = myDiv(a,b)
    if (operator2 == '1'):
        second_operation = myMul(first_operation,c)
        print('Entered experssion =', a, '/', b, '*', c)
    elif(operator2 == '2'):
        econd_operation = myDiv(first_operation,c)
        print('Entered experssion =', a, '/', b, '/', c)
    elif(operator2 == '3'):
        second_operation = myAdd(first_operation,c)
        print('Entered experssion =', a, '/', b, '+', c)
    elif(operator2 == '4'):
        second_operation = mySub(first_operation,c)
        print('Entered experssion =', a, '/', b, '-', c)
    
if (operator1 == '3'):
    if (operator2 == '1'): 
        first_operation = myMul(b,c)
        second_operation = myAdd(a,first_operation)
        print('Entered experssion =', a, '+', b, '*', c)
    elif(operator2 == '2'):
        first_operation = myDiv(b,c)
        second_operation = myAdd(a,first_operation)
        print('Entered experssion =', a, '+', b, '/', c)
    elif(operator2 == '3'):
        first_operation= myAdd(a,b)
        second_operation = myAdd(first_operation,c)
        print('Entered experssion =', a, '+', b, '+', c)
    elif(operator2 == '4'):
        first_operation= myAdd(a,b)
        second_operation = mySub(first_operation,c)
        print('Entered experssion =', a, '+', b, '-', c)

if (operator1 == '4'):
    if (operator2 == '1'): 
        first_operation = myMul(b,c)
        second_operation = mySub(a,first_operation)
        print('Entered experssion =', a, '-', b, '*', c)
    elif(operator2 == '2'):
        first_operation = myDiv(b,c)
        second_operation = mySub(a,first_operation)
        print('Entered experssion =', a, '-', b, '/', c)
    elif(operator2 == '3'):
        first_operation= mySub(a,b)
        second_operation = myAdd(first_operation,c)
        print('Entered experssion =', a, '-', b, '+', c)
    elif(operator2 == '4'):
        first_operation= mySub(a,b)
        second_operation = mySub(first_operation,c)
        print('Entered experssion =', a, '-', b, '-', c)
=======

if operator1 == '*' and operator2 == '*':
    print(a, '*', b, '*', c, '=', myMul(a, b, c))
elif operator1 == '1' and operator2 == '/':
        d = myMul(a, b)
        print(a, '*', b, '/', c, '=', myDiv(d, c))
elif operator1 == '*' and operator2 == '+':
        d = myMul(a, b)
        print(a, '*', b, '+', c, '=', myAdd(d, c))
elif operator1 == '*' and operator2 == '-':
        d = myMul(a, b)
        print(a, '*', b, '-', c, '=', mySub(d, c))

elif operator1 == '/' and operator2 == '*':
        d = myMul(b, c)
        print(a, '/', b, '*', c, '=', myDiv(a, d))
elif operator1 == '/' and operator2 == '/':
        d = myDiv(a, b)
        print(a, '/', b, '/', c, '=', myDiv(d, c)) 
elif operator1 == '/' and operator2 == '+':
        d = myDiv(a, b)
        print(a, '/', b, '+', c, '=', myAdd(d, c))      
elif operator1 == '/' and operator2 == '-':
        d = myDiv(a, b)
        print(a, '/', b, '-', c, '=', mySub(d, c))  

elif operator1 == '+' and operator2 == '*':
        d = myMul(b, c)
        print(a, '+', b, '*', c, '=', myAdd(a, d))
elif operator1 == '+' and operator2 == '/':
        d = myDiv(b, c)
        print(a, '+', b, '/', c, '=', myAdd(a, d))
elif operator1 == '+' and operator2 == '+':
        d = myAdd(b, c)
        print(a, '+', b, '+', c, '=', myAdd(a, d))
elif operator1 == '+' and operator2 == '-':
        d = mySub(b, c)
        print(a, '+', b, '-', c, '=', myAdd(a, d))

elif operator1 == '-' and operator2 == '*':
        d = myMul(b, c)
        print(a, '-', b, '*', c, '=', mySub(a, d))
elif operator1 == '-' and operator2 == '/':
        d = myDiv(b, c)
        print(a, '-', b, '/', c, '=', mySub(a, d))
elif operator1 == '-' and operator2 == '+':
        d = mySub(a, b)
        print(a, '-', b, '+', c, '=', myAdd(d, c))
elif operator1 == '-' and operator2 == '-':
        d = mySub(a, b)
        print(a, '-', b, '-', c, '=', mySub(d, c))



>>>>>>> 3156288955ed395c0926365ff1e11f7f337c9999


<<<<<<< HEAD
### if dividing by zero, print 'undefined' and ask for new integer.
print('Answer of the operation =', second_operation)
=======
>>>>>>> 3156288955ed395c0926365ff1e11f7f337c9999
