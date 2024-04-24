a = int(input("Enter number: "))

if a <= 1:
    print("Not prime!")
elif a == 2:
    print("Prime!")
else:
    for i in range(2, a):
        if a % 2 == 0:
            print("Not prime!")
            break
        print("Prime!")
        break