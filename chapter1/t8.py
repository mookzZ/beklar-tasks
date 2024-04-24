a = input("Enter a numbers: ").strip()
b = a.split(" ")
c = list(map(int, b))

print(sum(c))
print(sum(c) / len(c))