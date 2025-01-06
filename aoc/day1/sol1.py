f = open('input.txt', 'r')

L= []
R = []
for line in f:
    l, r = line.split()
    L.append(int(l))
    R.append(int(r))


print(sum(map(lambda x : abs(x[0] - x[1]), zip(sorted(L), sorted(R)))))