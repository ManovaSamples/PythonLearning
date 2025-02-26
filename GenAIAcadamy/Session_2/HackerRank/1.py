# https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

# Given an integer, , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

num = int(input("Enter number: "))
if num % 2 != 0 or num % 2 ==0 and (num >=6 and num <=20):
    print("Weird")
elif num % 2 ==0 and (num >=2 and num <=5) or num > 20:
    print("Not Weird")
else:
    print("Not an number")

