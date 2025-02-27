text = "Hello"

print(text.lower())
print(text.upper())
print(" Hello ".strip())
print(text.replace('l','i'))

#splits string into list
print("Hai,hello".split(","))
print('a,n,c'.split(","))
print("Hai Hello|hOW ARE|you".split("|")) #['Hai Hello', 'hOW ARE', 'you']
print("h a I".split(" "))

#join list into string
print("-".join(['a','b','c']))

data = ["Manova", "Chandramohan", "Working"]
print("%".join(data))