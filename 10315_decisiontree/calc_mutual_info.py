import numpy as np

data = [[0] for i in range(6)]
data = data.append([[1]for i in range(24)])

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

# print(entropy(0, data))
# Y = 5
# for R in range(6):
#     print(f"Mutual info between {Y} and {R}: {mutual_info(Y, R, data)}")

# print("NODE 2\n\n")

# Y = 5
# for R in range(6):
#     if R == 1:
#         continue
#     print(f"Mutual info between {Y} and {R}: {mutual_info(Y, R, data_pr)}")

H_Y = -(1/5 * np.log2(1/5) + 4/5 * np.log2(4/5))
print(H_Y)

H_Y_A = 1/2 * (6/15 * np.log2(6/15) + 9/15*np.log2(9/15) + 0 + 1 * np.log2(1))
print()
print(H_Y_A)

print()
print(H_Y + H_Y_A)

one = 1/4
two = 3/4

three = 0
four = 1
H_Y_B = 24/30*(one * np.log2(one) + two*np.log2(two)) + 6/30 * (0 + 1 * np.log2(1))


print()
print(H_Y_B)

print()

print(H_Y + H_Y_B)
