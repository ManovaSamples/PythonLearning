person = {
    "name": "Manova",
    "age": "28",
    "city": "Bangalore"
}

#add new key
person["country"] = "India"
print(person)
#change the value of age, if the key is available it will update else create new key 
person["age"] = "30"
print(person)