#write a function that returns the factorial of given number
def printFactorial(num):
 
    if num < 0:
        print("Cannot calculate factorial for less than zero numbers")
    elif num == 0:
        print("Factorial value of 0 is always 1")
    else:
        factorial = 1
        for i in range(1, num+1):
            factorial = factorial * i
            # print(factorial)
        return(factorial)

num = int(input("Enter the number:"))
print(f"The factorial of {num} is {printFactorial(num)}")