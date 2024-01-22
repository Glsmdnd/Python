""" Doğru çalışan bu!!!! """
fruits = [["apple", "umbrella","cherry"],["apple", "banana","tomato"],
["banana","apple", "banana","tomato"],["apple", "umbrella","cherry"],["apple", "banana","tomato"],
["banana","apple", "banana","tomato"],["apple", "umbrella"]
for fruit in fruits:
  if 'banana' in fruit:
    fruit.remove("banana")
    fruit.remove("banana")
    print(fruit)
  else:
    print(fruit)
   
   
