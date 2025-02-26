#write a FizzBuzz program that prints number from 1 to 100 with "Fizz" for multiples of 3
#Buzz for multiples of 5 and FizzBuzz for multiples of both

for i in range(1,31):
    if i%3==0 and i%5==0:
        i="FizzBizz"
        print(i)
    elif i%3==0:
        i="Fizz"
        print(i)
    elif i%5==0:
        i="Bizz"
        print(i)
    
    else:
        print(i)