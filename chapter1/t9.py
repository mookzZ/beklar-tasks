a = input("Enter a string: ").lower()
b = a[::-1]

if a == b:
    print("Palindrome!")
else:
    print("Not Palindrome!")