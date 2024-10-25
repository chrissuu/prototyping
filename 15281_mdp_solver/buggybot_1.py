transitions = {
    ('HillA', 'RollL', 'Valley'): (1.0, -2.0),
    ('HillA', 'RollR', 'Valley'): (1.0, 0.7),
    ('HillB', 'RollL', 'Valley'): (0.8, -2.3),
    ('HillB', 'RollL', 'HillA'): (0.2, -2.3),
    ('HillB', 'RollR', 'Valley'): (0.9, 1.5),
    ('HillB', 'RollR', 'HillA'): (0.1, 1.5),
    ('Valley', 'PushA', 'HillA'): (0.5, -0.2),
    ('Valley', 'PushB', 'HillB'): (1.0, -0.9)
}

actions = ['RollL', 'RollR', 'PushA', 'PushB']

states = {'HillA':0, 
          'HillB':1, 
          'Valley':2}

values = []

gamma = 0.9
def converged(prev, curr):
    
    for i in states.values():
        if abs(prev[i] -curr[i]) >= 1e-7:
            return False

    return True

def V(s, gamma, prev, transitions):
    curr_max = 0
    for a in actions:
        curr = 0
        for s_p in states.keys():
            curr_key = (s, a, s_p)
            if transitions.get(curr_key):
                info = transitions[curr_key]
                curr += info[0]*(info[1] + gamma * prev[states[s_p]])

        curr_max = max(curr, curr_max)
    return curr_max

prev2 = [-1,-1,-1]
prev1=[0,0,0]
curr = [None, None, None]
k = 0
while not converged(prev2, prev1):
    curr[0] = V(list(states.keys())[0], gamma, prev1, transitions)
    curr[1] = V(list(states.keys())[1], gamma, prev1, transitions)
    curr[2] = V(list(states.keys())[2], gamma, prev1, transitions)
    k+=1
    prev2 = prev1
    prev1 = curr
    curr = [None,None,None]


print(prev2[0])
print(prev2[1])
print(prev2[2])

print(prev1[0])
print(prev1[1])
print(prev1[2])
print(k)
    
    

