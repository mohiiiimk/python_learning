#excercise 1
fruits = ["apple", "banana", "orange"]
fruits.append("mango")
print(fruits)

#excercise 2
numbers=[10,20,40,50]
numbers.insert(2,30)
print(numbers)

#excercise 3
names=["Alice","Bob","Sara","Bob","Mike"]
names.remove("Bob")
print(names)

#excercise 4
numbers = [10, 20, 30, 40, 50]
removed = numbers.pop(2)
print(numbers)
print(removed)

#excercise 5
numbers=[45,12,78,3,29,10]
numbers.sort()
numbers.reverse()
print(numbers)

#excercise 6
numbers = [1, 5, 2, 8, 3, 9, 4]
even=[]
for number in numbers:
    if number%2==0:
        even.append(number)
print(even)


#excercise 7
numbers = [3, 7, 2, 9, 4, 6, 1]
greater=[]
for number in numbers:
    if number>5:
        greater.append(number)
print(greater)


#while version
i=0
greater=[]
while i<len(numbers):
    if numbers[i]>5:
        greater.append(numbers[i])
    i+=1
print(greater) 


print("list topic is done")
#Tuples==========================================================

#excercise 1
fruits = ("apple", "banana", "orange", "mango")
print(fruits[2])

#excercise 2
print(fruits[:-3:-1])

#excercise 3
print(fruits[::-1])

#excercise 4
#fruits[1]="grape"
print("sorry, touples are not changabel")

#excercise 5
numbers=(10,15,20,25,30,35)
divisible_5=[]
for number in numbers:
    if number%5==0:
        divisible_5.append(number)
print(divisible_5)

#while version
numbers=(10,15,20,25,30,35)
divisible_5=[]
i=0
while i<len(numbers):
    if numbers[i]%5==0:
        divisible_5.append(numbers[i])
    i+=1
print(divisible_5)


print("Tuples topic is done")
#Sets==========================================================

#excercise 1
numbers = {1, 2, 2, 3, 4, 4, 5, 5, 5}
print(numbers)
print("repeated numbers are gathered into one")

#excercise 2
colors={"red","blue","green"}
colors.add("yellow")
print(colors)

#excercise 3
colors.remove("blue")
print(colors)

#excercise 4
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1 & set2)

#excercise 5
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1-set2)

#excercise 6
numbers=[1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
numbers_set=set(numbers)
for number in numbers_set:
    print(number)
    
print("Sets topic is done")

