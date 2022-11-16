arr = [1, 2, 3, 3, 3, 4, 3]

def elemento_principal(arr):
    l = []
    for i in arr:
        n = arr.count(i)
        l.append(n)
    if max(l) <= 2:
        print(-1)
    elif max(l) >= 3:
        print(max(l))

elemento_principal(arr)