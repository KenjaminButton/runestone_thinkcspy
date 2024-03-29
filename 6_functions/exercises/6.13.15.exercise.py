'''
Write a function called myPi that will return an
approximation of PI (3.14159…).
Use the Leibniz approximation.
'''
# Leibniz Formula for Python:
# https://stackoverflow.com/questions/18036367/leibniz-formula-for-%CF%80-is-this-any-good-python

'''
def myPi(iters):
    # Calculate an approximation of PI using the Leibniz
    # approximation with iters number of iterations 
    pi = 0
    sign = 1
    denominator = 1
    for i in range(iters):
        pi = pi + (sign/denominator)
        sign = sign * -1  # alternate positive and negative
        denominator = denominator + 2

    pi = pi * 4.0
    return pi

pi_approx = myPi(10000)
print(pi_approx)

'''

def myPi(iters):
    pi = 0
    sign = 1
    denominator = 1
    for i in range(iters):
        pi = pi + (sign/denominator)
        sign = sign * -1 # alternate positive and negative
        denominator = denominator + 2

    pi = pi * 4.0
    return pi

pi_approx = myPi(10000)
print(pi_approx)
