#Dictionary Comprehensions=============================================
#exercise 1
numbers = [1, 2, 3, 4, 5]
new={number : number**2 for number in numbers}
print(new)

#exercise 2
numbers={1,2,3,4,5,6,7,8,9}
even={number : number**2 for number in numbers if number%2==0}
print(even)

#exercise 3
words = ["python", "AI", "engineering", "code"]
new_words={word: len(word) for word in words}
print(new_words)


#exercise 4
numbers = [3, 7, 10, 12, 15, 20]
new={number: number*10 for number in numbers if number>10}
print(new)



# zip()====================================================
#exercise 5
names = ["Ali", "Sara", "Mohi", "John"]
scores = [85, 92, 78, 90]
new=dict(zip(names,scores))
print(new)
#unpacking=============================================================
#exercise 6
student = ("Sara", 23, "Mechanical Engineering")
name , age ,major=student
print(name)
print(age)
print(major)

#exercise 7
names = ["Ali", "Sara", "Mohi"]
scores = [85, 92, 78]
inf=dict(zip(names,scores))
print(inf)
for name,score in zip(names,scores):
    print(name,score)

#Nested Comprehensions========================================
#exercise 8
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for row in matrix:
    for number in row:
        print(number)


numbers=[number for row in matrix for number in row]


single_row=[]
for row in matrix:
    for number in row:
        single_row.append(number)
print(single_row)



single_row=[number for row in matrix for number in row ]
print(single_row)



#exercise 9
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

single_row=[]
for row in matrix:
    for number in row:
        single_row.append(number*2)
print(single_row)

single_row=[number*2 for row in matrix for number in row ]
print(single_row)

