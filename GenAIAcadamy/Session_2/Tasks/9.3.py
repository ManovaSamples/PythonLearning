#reverse a number using while loop

#take input an integer n and caluclates the sum of the digits using while loop

num = int(input("enter more than 1 digit number: "))
total = 0
while(num>0):
    dig=num%10
    total=total*10+dig
    num=num//10
print(total)

