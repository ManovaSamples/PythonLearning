#write a function that takes a list of numbers, removes all odd numbers, sorts the ramining 
# even numbers in descending order and retruns the modied list

def sortEvenNumbers(numbers):

    res = [i for i in numbers if i % 2 !=0]
    res.sort()
    res.reverse()
    print(res)

numbers = [78, 13, 97, 26, 51, 73, 85, 80, 67, 36]
sortEvenNumbers(numbers)