animal = {
    "name": "chuffie",
    "breed": "turtle",
    "age": 2
}

# for i in animal:
#     print(i,":", animal[i])

# print(animal.get("breed"))
# print(animal.keys())
# print(animal.values())
# print(animal.items()) #prints key values in a tuple--> dict_items([('name', 'chuffie'), ('breed', 'turtle'), ('age', 2)])

# for i in animal.items():
#     print(i)

animal.pop("breed")
print(animal)