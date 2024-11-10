s = 3
a = 'helix'
s_p = 4
r = -3
alpha = 0.15
gamma = 0.4


W = [1,0.2,3,0.5]
actions = ['elevator', 'stairs', 'helix']

def f_0(s, a):
    return 1

def f_1(s, a):
    t = 0
    if a == 'elevator':
        t += 20
    elif a == 'stairs':
        t += 15
    else:
        t += 10
    
    return (abs(s-4) +1)*t

def f_2(s, a):
    if a == 'stairs':
        return 2
    elif a == 'helix':
        return 5
    else:
        return 8

def f_3(s, a):
    if a == 'elevator':
        if s == 3:
            return 40
        elif s == 4:
            return 80
        elif s == 5:
            return 40
    else:
        return 0

FUNCTIONS = [f_0, f_1, f_2, f_3]

partial = [f_i(s, a) for f_i in FUNCTIONS]

def Q_w(W, s, a, f = FUNCTIONS):
    return sum([f[i](s, a) * W[i] for i in range(4)])

Qw = Q_w(W, s, a, FUNCTIONS)
max_a_p = max([Q_w(W, s_p, a_p, FUNCTIONS) for a_p in actions])

td = r + gamma * max_a_p - Qw

print(td)

W_p = [(W[i] + alpha * td * partial[i]) for i in range(4)]

print(W_p)
