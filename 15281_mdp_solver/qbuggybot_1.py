transitions1 = {
    ('HillA', 'RollL', 'Valley'): (1.0, -2.0),
    ('HillA', 'RollR', 'Valley'): (1.0, 0.7),
    ('HillB', 'RollL', 'Valley'): (0.8, -2.3),
    ('HillB', 'RollL', 'HillA'): (0.2, -2.3),
    ('HillB', 'RollR', 'Valley'): (0.9, 1.5),
    ('HillB', 'RollR', 'HillA'): (0.1, 1.5),
    ('Valley', 'PushA', 'HillA'): (1.0, -0.2),
    ('Valley', 'PushB', 'HillB'): (1.0, -0.9)
}

transitions2 = {
    ('Hill', 'RollL', 'Valley'): (0.9, -2.15),
    ('Hill', 'RollL', 'Hill'): (0.1 , -2.15),
    ('Hill', 'RollR', 'Valley'): (0.95, 1.1),
    ('Hill', 'RollR', 'Hill'): (0.05, 1.1),
    ('Valley', 'PushA', 'HillA'): (1.0, -0.2),
    ('Valley', 'PushB', 'HillB'): (1.0, -0.9)
}

q_values = {
    ('HillA', 'RollL') : 0.302,
    ('HillA', 'RollR') : 3.00,
    ('HillB', 'RollL') : 0.082,
    ('HillB', 'RollR') : 3.84,
    ('Valley', 'PushA') : 2.51,
    ('Valley', 'PushB') : 2.56,
}


actions = ['RollL', 'RollR', 'PushA', 'PushB']

actions1 = {'HillA' : ['RollL', 'RollR'],
            'HillB' : ['RollL', 'RollR'],
            'Valley' : ['PushA', 'PushB']}

actions2 = {'Hill' : ['RollL', 'RollR'],
           'Valley': ['PushA', 'PushB']
           }

states2 = ['Hill', 'Valley']

states1 = ['HillA', 'HillB', 'Valley']

gamma = 0.9

def V_p(pi, gamma, transitions, states, num_iterations):
    prev = dict([(s, 0) for s in states])
    print(prev)
    for i in range(num_iterations):
        curr = dict([(s, 0) for s in states])
        for s in states:
            running_sum = 0
            for s_p in states:
                curr_key = (s, pi[s], s_p)
                T_rt = transitions.get(curr_key, 0)
                P = 0
                R = 0
                if T_rt != 0:
                    P = T_rt[0]
                    R = T_rt[1]
                running_sum += P * (R + gamma * prev[s_p])
            curr[s] = running_sum
            prev = curr

    return prev

def pi_n(v_pi, gamma, transitions, actions, states):
    pi_ip1 = dict([(s, None) for s in states])
    for s in states:
        curr_best_action = None
        curr_best_val = None        
        for a in actions[s]:
            
            running_sum = 0

            for s_p in states:
                curr_key = (s, a, s_p)
                T_rt = transitions.get(curr_key, 0)
                P = 0
                R = 0
                if T_rt != 0:
                    P = T_rt[0]
                    R = T_rt[1]
                running_sum += P * (R + gamma * v_pi[s_p])
            
            if curr_best_val == None or running_sum > curr_best_val:
                curr_best_val = running_sum
                curr_best_action = a

            #if s== 'Valley':
            #    print('------')
            #    print(actions)
            #    print(states)
            #    print(f"{a} : {running_sum}")
            #    print('------')
        pi_ip1[s] = curr_best_action
    return pi_ip1
        


pi_1 = {
    'HillA':'RollR',
    'HillB':'RollR',
    'Valley':'PushB'
}

pi_2 = {
    'Hill': 'RollR',
    'Valley': 'PushA'
}

def prettyprint_by_state(dict, states):
    for s in states:
        print(f"{s} : {dict[s]}")

# Vp = V_p(pi_2, gamma, transitions2, states2, 1000)
# pi_next = pi_n(Vp, gamma, transitions2, actions2, states2)

# prettyprint_by_state(Vp, states2)
# prettyprint_by_state(pi_next, states2)

# Vpp = V_p(pi_next, gamma, transitions2, states2, 1000)
# pi_nn = pi_n(Vpp, gamma, transitions2, actions2, states2)

# prettyprint_by_state(Vpp, states2)
# prettyprint_by_state(pi_next, states2)


print('-----------------')
Vp = V_p(pi_1, gamma, transitions1, states1, 1000)
pi_next = pi_n(Vp, gamma, transitions1, actions1, states1)

prettyprint_by_state(Vp, states1)
prettyprint_by_state(pi_next, states1)

Vpp = V_p(pi_next, gamma, transitions1, states1, 1000)
pi_nn = pi_n(Vpp, gamma, transitions1, actions1, states1)

prettyprint_by_state(Vpp, states1)
prettyprint_by_state(pi_next, states1)