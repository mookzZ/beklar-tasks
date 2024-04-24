a = [1, -6, 0, 4, 7]

length = len(a)
for i in range(length - 1):
    min = a[i]
    index = i
    for j in range(index + 1, length):
        if min > a[j]:
            min = a[j]
            index = j
    if index != i:
        t = a[i]
        a[i] = a[index]
        a[index] = t

print(a)