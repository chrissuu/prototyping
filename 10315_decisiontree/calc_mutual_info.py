import numpy as np

data = [
        [1, 1, 0, 0, 1, 1], 
        [1, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 1], 
        [0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 1], 
        [0, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0], 
        [1, 1, 1, 0, 0, 1],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0], 
        [1, 0, 0, 1, 0, 1]]

# data_pl = [
#         [1, 0, 0, 1, 1], 
#         [1, 1, 0, 1, 1],
#         [0, 1, 0, 0, 0],
#         [0, 1, 0, 1, 0],
#         [0, 1, 0, 0, 1], 
#         [0, 1, 1, 1, 1],
#         [1, 0, 0, 1, 0],
#         [0, 0, 1, 1, 1], 
#         [0, 1, 0, 1, 1],
#         [1, 0, 0, 0, 0], 
#         [1, 1, 0, 0, 1],
#         [0, 1, 1, 1, 0],
#         [0, 0, 0, 1, 0], 
#         [1, 0, 1, 0, 1]]

data_pr = [
        [1, 1, 0, 0, 1, 1], 
        [1, 1, 1, 0, 1, 1],
        [0, 1, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 1], 
        [0, 1, 0, 1, 1, 1], 
        [1, 1, 1, 0, 0, 1],
        [0, 1, 1, 1, 1, 0],]

# data_pl= [
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 1, 1, 1],
#         [1, 0, 0, 0, 1, 0],
#         [0, 0, 1, 0, 1, 1],
#         [1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0], 
#         [1, 0, 0, 1, 0, 1]]

def pmf(Y, y, arr):
    return sum([1 for i in range(len(arr)) if arr[i][Y] == y]) / len(arr)

def joint_pmf(Y, X, y, x, arr):
    return sum([1 for i in range(len(arr)) if arr[i][Y] == y and arr[i][X] == x]) / len(arr)

# P(X = x | Y = y) = P(X = x and Y = y) / P(Y = y)
def cond_pmf(Y, X, y, x, arr):
    return joint_pmf(Y, X, y, x, arr) / pmf(X, x, arr)

def entropy(Y, arr):
    classes = [0, 1]
    entropy = 0

    for y in classes:
        p = pmf(Y, y, arr)
        if p == 0:
            continue
        entropy -= p * np.log2(p)

    return entropy

def specific_conditional_entropy(Y, X, x, arr):
    classes = [0, 1]
    specific_cond_entropy = 0

    for y in classes:
        p = cond_pmf(Y, X, y, x, arr)
        if p == 0:
            continue
        specific_cond_entropy -= p * np.log2(p)

    return specific_cond_entropy

def conditional_entropy(Y, X, arr):
    classes = [0, 1]
    cond_entropy = 0

    for x in classes:
        p = pmf(X, x, arr)
        cond_entropy += p * specific_conditional_entropy(Y, X, x, arr)

    return cond_entropy

def mutual_info(Y, X, arr):
    return entropy(Y, arr) - conditional_entropy(Y, X, arr)

Y = 5
for R in range(6):
    print(f"Mutual info between {Y} and {R}: {mutual_info(Y, R, data)}")

print("NODE 2\n\n")

Y = 5
for R in range(6):
    if R == 1:
        continue
    print(f"Mutual info between {Y} and {R}: {mutual_info(Y, R, data_pr)}")