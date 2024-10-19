import itertools
import random
def impl(a,b):
    return not a or b

def bicon(a,b):
    return impl(a,b) and impl(b,a)

def bigland(assignments):
    bigland = [False] * len(assignments[0])
    for i in range(len(assignments[0])):
        for assignment in assignments:
            bigland[i] = bigland[i] or assignment[i]

    return bigland

def s1(x,y):

    return not(impl(not((not y) and y), (not x and False))) and ((bicon(x,y) and not (x or not y)))

        
def s2(x,y,z):

    return impl(not(x or not(x and (z or True))), not(y and(not y or (impl(True, False)))))



def random_sat(S, numvars, shots):
    assignments = []
    for i in range(shots):
        tempassignment = [False] * numvars
        for k in range(numvars):
            r = random.randint(0,1)
            if int(r):
                tempassignment[k] = False
            else:
                tempassignment[k] = True
        
        if S(*tempassignment):
            assignments.append(tempassignment)

     
    return assignments

a2 = random_sat(s2, 3, 100000)
if len(a2) == 0:
    print(False)
else: 
    print(bigland(a2))

