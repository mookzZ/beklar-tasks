a = input("Enter a number: ").strip()
a = a.split(" ")
max = ""

for i in a:
    if len(i) > len(max):
        max = i

print(max)