transitions = {
    ('Hill', 'RollL', 'Valley'): (0.9, (-4.3)/2),
    ('Hill', 'RollL', 'Hill'): (0.1, (-2.3)),
    ('Hill', 'RollR', 'Valley'): (0.95, 1.1),
    ('Hill', 'RollR', 'Hill'): (0.05, (1.5)),
    ('Valley', 'PushA', 'Hill'): (0.5, -0.2),
    ('Valley', 'PushB', 'Hill'): (0.5, -0.9)
}

actions = ['RollL', 'RollR', 'PushA', 'PushB']

states = {'Hill':0, 
          'Valley':1}

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

prev2 = [-1,-1]
prev1=[0,0]
curr = [None, None]
k = 0
while not converged(prev2, prev1):
    curr[0] = V(list(states.keys())[0], gamma, prev1, transitions)
    curr[1] = V(list(states.keys())[1], gamma, prev1, transitions)
    k+=1
    prev2 = prev1
    prev1 = curr
    curr = [None,None]


print(prev2[0])
print(prev2[1])

print(prev1[0])
print(prev1[1])
print(k)
    
    

