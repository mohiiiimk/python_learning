#List  Comprehensions===============================================

#excercise 1
numbers=[1,2,3,4,5]
square=[number**2 for number in numbers]
print(square)

#excercise 2
numbers=[1,2,3,4,5,6,7,8]
even=[number for number  in numbers if number%2==0]
print(even)

#excercise 3
numbers=[1,2,3,4,5,6,7,8,9,10]
square_even=[number**2 for number in numbers if number%2==0]
print(square_even)

#exercise 4
numbers=[3,8,12,5,7,20,11,4]
new=[number*2 for number in numbers if number>10]
print(new)

#exercise 5
words = ["python", "mechanical", "engineering", "code", "AI"]
length=[len(word) for word in words]
print(length)

#exercise 6
words = ["python", "AI", "mechanical", "code", "engineering", "ML"]
new=[word for word in words if len(word)>4]
print(new)

#exercise 7
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new=[number**2  if number%2==0 else number*2 for number in numbers]
print(new)