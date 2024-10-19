from math import factorial
from math import exp

Y = [0,1,2,3,4]
n = 20
p = 0.05


def choose(n, c):
    return factorial(n)/(factorial(c)*factorial(n-c))

def p_bin(n,p,y):
    return choose(n, y)*(p**y)*(1-p)**(n-y)

def p_pois(n,p,y):
    return ((n*p)**y)/(factorial(y)) * exp(-1*n*p)


print("BINOMIAL")
for i in Y:
    print(p_bin(n,p,i))

print("\n\n")


for i in Y:
    print(p_pois(n,p,i))

print("\n\n")

