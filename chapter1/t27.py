def search(a):
    result = []
    a = int(input("Enter a number: "))
    for i in range(1, a+1):
        if is_prime(i):
            result.append(i)
    print(result)
def is_prime(n):
    if n <= 1:
        return False
    # Проверяем, что число n не делится нацело на любое число от 2 до квадратного корня из n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

search(17)