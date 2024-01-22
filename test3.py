fruits = [["apple", "banana", "cherry"],["apple", "banana"]]
newFruit=list(fruits)
for fruit in fruits:
    newFruit.remove('banana')
    print(fruit)