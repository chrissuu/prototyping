f = open('input.txt', 'r')

reports = []

for line in f:

    reports.append(line.split(" "))

def isSafe(arr):
    if len(arr) <= 1:
        return True
    
    inc = None
    dec = None
    if arr[0] > arr[1]:
        inc = False
        dec = True
    elif arr[0] < arr[1]:
        inc = True
        dec = False
    else:
        return False
    
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) < 1 or abs(arr[i] - arr[i + 1]) > 3:
            return False
        if inc:
            if arr[i] > arr[i+1]:
                return False
        if dec:
            if arr[i] < arr[i+1]:
                return False
    return True

cnt = 0
for report in reports:
    if isSafe(list(map(lambda x : int(x), report))):
        cnt += 1

print(cnt)