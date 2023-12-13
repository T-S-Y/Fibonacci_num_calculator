import random


def fib(x):
    '''
    function calculates Fibonacci
    number of x, using rekursion

    arg: x ; has to be an int >= 0

    returns: Fibonacci of x
    '''
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


# Testcase; how the function can be used
# to generate random fib. num. between 0-20
x = random.randint(0, 20)

print("x is :",x)
print("The Fibonacci number is :", fib(x))
