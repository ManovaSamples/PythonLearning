# numbers = [1,7,2,4,9,3]

##print list elements
# for i in numbers:
#     print(i)

#index
# print(numbers[3])

# # iterate through elements using index
# for i in range(len(numbers)):
#     print(numbers[i])

# creat a list contains the numbers 1-10 automatically

numbers2 = []

for i in range(1, 11):
    numbers2.append(i)
print(numbers2)
numbers2.remove(numbers2[-1])
print(numbers2)


