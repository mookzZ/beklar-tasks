a = int(input("Enter a number: "))

def isEven(num):
    if num % 2 == 0:
        print(True)
    else:
        print(False)

if type(a) == int:
    isEven(a)
else:
    print("Not a number")
