## A terminal based calculator application which prompts the user to enter a mathmematical expression htat includes three integer values and two operators.
## 

def myAdd(x, y, z):
    print(x, '+', y, '+', z, '=', x + y + z)
    
    
def mySub(x, y, z):
    return x - y -z

def myMul(x, y, z):
    return x * y * z

def myDiv(x, y, z):
    return x // y // z




## This function validates integer input
def input_int():
    while True:
        try:
            x = int(input("Select an integer: "))
            return x
        except ValueError:
            print('\nPlease enter an integer only.\n')

def input_op(x):
    while x not in {'1': '*', '2': '/', '3': '+', '4':'-'}:
        x = input("\n\nSelection invalid. Choose a number from the list. \n\nSelect an operator:\n1. *\n2. /\n3. +\n4. -\n\n")
        return x



print("\nSelect three integers and 2 operators as requested.\n")


a = input_int()
print('\na =', a)

operator1 = input("\nSelect an operator:\n1. *\n2. /\n3. +\n4. -\n")
input_op(operator1)

b = input_int()
print('\nb =', b)

operator2 = input("\nSelect an operator:\n1. *\n2. /\n3. +\n4. -\n")
input_op(operator2)


c = input_int()
print('\nc =', c)


if operator1 == '1' and operator2 == '1':
    print(a, '*', b, '*', c, '=', myMul(a, b, c))

else: 
    print('Bye')



