## A terminal based calculator application which prompts the user to enter a mathematical expression that includes three integer values and two operators.
## 

def myAdd(x, y): ### a function that adds two integers
    return(x + y)
    
def mySub(x, y): ### a function that subtracts an integer from another integer
    return (x - y)

def myMul(x,y): ## a function that multiplies two integers to each other
    return (x * y)

def myDiv(x, y): ## a function that divides an integer by another integer
    return (x // y)

## This function validates integer input
def input_int():
    while True:
        try:
            x = int(input("Enter an integer: "))
            return x
        except ValueError:
            print('\nPlease enter an integer only.\n')
            
## A function that validates user input for operator1 and operator2
def input_op(x): 
    while x not in {'*', '/', '+', '-'}:
        try:
            x = input("\n\nSelection invalid. Choose an option from the list. \n\nSelect an operator:\n*\t/\t+\t-\n")
            return x
        except ValueError:
            x = input("\n\nSelection invalid. Choose an option from the list. \n\nSelect an operator:\n*\t/\t+\t-\n")



def calculator(x, y, z, op1, op2):
    if op1 == '*' and op2 == '*': ## create an expression for x * y * z
        print(x, '*', y, '*', z, '=', myMul(x, y, z))
    elif op1 == '1' and op2 == '/':  ## create an expression for x * y / z
            d = myMul(x, y)
            print(x, '*', y, '/', z, '=', myDiv(d, z))
    elif op1 == '*' and op2 == '+':  ## create an expression for x * y + z
            d = myMul(x, y)
            print(x, '*', y, '+', z, '=', myAdd(d, z))
    elif op1 == '*' and op2 == '-':  ## create an expression for x * y - z
            d = myMul(x, y)
            print(x, '*', y, '-', z, '=', mySub(d, z))

    elif op1 == '/' and op2 == '*':  ## create an expression for x / y * z
            d = myMul(y, z)
            print(x, '/', y, '*', z, '=', myDiv(x, d))
    elif op1 == '/' and op2 == '/':     ## create an expression for x / y / z
            d = myDiv(x, y)
            print(x, '/', y, '/', z, '=', myDiv(d, z))
    elif op1 == '/' and op2 == '+': ## create an expression for x / y + z
            d = myDiv(x, y)
            print(x, '/', y, '+', z, '=', myAdd(d, z))      
    elif op1 == '/' and op2 == '-':     ## create an expression for x / y - z
            d = myDiv(x, y)
            print(x, '/', y, '-', z, '=', mySub(d, z))  

    elif op1 == '+' and op2 == '*':## create an expression for x + y * z
            d = myMul(y, z)
            print(x, '+', y, '*', z, '=', myAdd(x, d))  
    elif op1 == '+' and op2 == '/': ## create an expression for x + y / z
            d = myDiv(y, z)
            print(x, '+', y, '/', z, '=', myAdd(x, d))
    elif op1 == '+' and op2 == '+': ## create an expression for x + y + z
            d = myAdd(y, z)
            print(x, '+', y, '+', z, '=', myAdd(x, d))
    elif op1 == '+' and op2 == '-': ## create an expression for x + y - z
            d = mySub(y, z)
            print(x, '+', y, '-', z, '=', myAdd(x, d))

    elif op1 == '-' and op2 == '*': ## create an expression for x - y * z
            d = myMul(y, z)
            print(x, '-', y, '*', z, '=', mySub(x, d))
    elif op1 == '-' and op2 == '/': ## create an expression for x - y / z
            d = myDiv(y, z)
            print(x, '-', y, '/', z, '=', mySub(x, d))
    elif op1 == '-' and op2 == '+':  ## create an expression for x - y + z
            d = mySub(x, y)
            print(x, '-', y, '+', z, '=', myAdd(d, z))
    elif op1 == '-' and op2 == '-':  ## create an expression for x - y - z
            d = mySub(x, y)
            print(x, '-', y, '-', z, '=', mySub(d, z))



               
            
                

def main():
    print("\nSelect three integers and 2 operators as requested.\n")


    a = input_int() # request input for first integer
    print('\na =', a) # validate user input

    operator1 = input("\nSelect an operator:\n*\t/\t+\t-\n") # requests user input for first operator
    input_op(operator1) # validate user input                       
    if operator1 == '*':                            #first operation is multipication
        print('\nOperation 1: Multiply\n')
    elif operator1 == '/':                          #first operation is division 
        print('\nOperation 1: Divide\n')
    elif operator1 == '+':                          #first operation is adding
        print('\nOperation 1: Add\n')               
    elif operator1 == '-':                          #first operation is subtracting
        print('\nOperation 1: Subtract\n')          

    b = input_int() ## request user input for second integer
    print('\nb =', b) ## validate user input
    while operator1 == '/' and b == 0:     ### if dividing by zero, print 'undefined' and ask for new integer.
            b = int(input('Undefined. Select an integer greater than 0 for valid operation:\n'))
    

    operator2 = input("\nSelect an operator:\n*\t/\t+\t-\n") # requests user input for second operator
    input_op(operator2) ## validates user input
    if operator2 == '*':                              #second operation is multipication
        print('\nOperation 2: Multiply\n')
    elif operator2 == '/':                            #second operation is divison 
        print('\nOperation 2: Divide\n')
    elif operator2 == '+':                            #second operation is adding
        print('\nOperation 2: Add\n')
    elif operator2 == '-':                            #second operation is subtracting
        print('\nOperation 2: Subtract\n')

    c = input_int() ## request user input for third integer
    while operator2 == '/' and c == 0:     ### if dividing by zero, print 'undefined' and ask for new integer.
            c = int(input('Undefined. Select an integer greater than 0 for valid operation:\n'))
    

    calculator(a, b, c, operator1, operator2)

if __name__ == '__main__':
    main()



