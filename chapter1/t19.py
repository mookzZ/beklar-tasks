a = input("Enter numbers: ").strip()
a = a.split(" ")
b = list(map(int, a))
print(max(b))