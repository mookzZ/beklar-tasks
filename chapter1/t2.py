# works up to ["4", "3", "*", 2 /] (2 stage action)
# by acided aka bogdan4ik cutie <3

user_input = input("Enter Reverse Polish Notation: ")
devided_list = user_input.split(" ")
result = 0

def main(list):
    first_action(list)
    list = list[3:]
    if list[1] == "*":
        print(result * int(list[0]))
    elif list[1] == "/":
        print(result / int(list[0]))
    elif list[1] == "+":
        print(result + int(list[0]))
    elif list[1] == "-":
        print(result - int())
    else:
        print("Invalid operator")

def first_action(list):
    global result
    n1 = int(list[0])
    n2 = int(list[1])
    if list[2] == "*":
        result = n1 * n2
    elif list[2] == "/":
        result = n1 / n2
    elif list[2] == "+":
        result = n1 + n2
    elif list[2] == "-":
        result = n1 - n2
    else:
        print("Invalid operator")

main(devided_list)