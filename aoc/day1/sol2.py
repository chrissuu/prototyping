f = open('input.txt', 'r')

L= []
R = []
for line in f:
    l, r = line.split()
    L.append(int(l))
    R.append(int(r))

D = {}
for r in R:
    D[r] = D.get(r, 0) + 1

s = 0
for l in L:
   
    s += l * D.get(l, 0)


print(s)
