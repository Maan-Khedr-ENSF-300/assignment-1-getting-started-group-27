## A terminal based calculator application which prompts the user to enter a mathematical expression that includes three integer values and two operators.
## 

def myAdd(x, y):
    '''
    Add two integers together

    Arguments:
    x, y

    returns the sum of two numbers received(integer)
    '''
    return(x + y)
    
def mySub(x, y):
    '''
    subtract two integers from each other

    Arguments:
    x, y

    returns the answer of subtraction(integer)
    '''
    return (x - y)

def myMul(x,y):
    '''
    multiply two integers by each other

    Arguments:
    x, y

    returns the answer of multipication(integer)
    '''
    return (x * y)

def myDiv(x, y):
    '''
    divide two integers by each other

    Arguments:
    x, y

    returns the answer of division(integer)
    '''
    return (x // y)




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
        x = input("\n\nSelection invalid. Choose an option from the list. \n\nSelect an operator:\n*\t/\t+\t-\n")
        return x

def main():
    print("\nSelect three integers and 2 operators as requested.\n")


    a = input_int()
    print('\na =', a)

    operator1 = input("\nSelect an operator:\n*\t/\t+\t-\n")
    input_op(operator1)                         
    if operator1 == '*':                            #first operation is multipication
        print('\nOperation 1: Multiply\n')
    elif operator1 == '/':                          #first operation is division 
        print('\nOperation 1: Divide\n')
    elif operator1 == '+':                          #first operation is adding
        print('\nOperation 1: Add\n')               
    elif operator1 == '-':                          #first operation is subtracting
        print('\nOperation 1: Subtract\n')          

    b = input_int()
    print('\nb =', b)
    if operator1 == '2' and b == 0:  ### if dividing by zero, print 'undefined' and ask for new integer.
            b = int(input('Undefined. Select an integer greater than 0 for valid operation:\n'))
    print('\nb =', b)

    operator2 = input("\nSelect an operator:\n*\t/\t+\t-\n")
    input_op(operator2)
    if operator2 == '*':                              #second operation is multipication
        print('\nOperation 2: Multiply\n')
    elif operator2 == '/':                            #second operation is divison 
        print('\nOperation 2: Divide\n')
    elif operator2 == '+':                            #second operation is adding
        print('\nOperation 2: Add\n')
    elif operator2 == '-':                            #second operation is subtracting
        print('\nOperation 2: Subtract\n')

    c = input_int()
    if operator2 == '2' and c == 0:     ### if dividing by zero, print 'undefined' and ask for new integer.
            c = int(input('Undefined. Select an integer greater than 0 for valid operation:\n'))
    print('\nc =', c)



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


if __name__ == '__main__':
    main()

