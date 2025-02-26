#create a function that returns True if a number is prime else False

def isPrimeNumber(num):
    if num <= 1:
        return False
    for i in range (2, int(num ** 0.5) + 1):
        if num % i ==0:
            return False

    return True

num = int(input("Enter the number: "))
print(isPrimeNumber(num))
