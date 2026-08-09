
#exercise 1
def say_hello():
    print("hello")

say_hello()
say_hello()
say_hello()


#exercise 2
def great(name):
    print(f"Hello,{name}!")

great("Alice")


#exercise 3
def introduce(name,age):
    print(f"My name is {name} and i am {age} years old")

introduce("Sara",23)



#exercise 4
def square(number):
    print(number**2)

square(5)


#exercise 5
def check_age(age):
    if age>=18:
        print("Adult")
    else:
        print("minor")

check_age(22)
check_age(15)

print("!part one is finished!")

#part 2==============================================

#exercise 1
def add(a,b):
    return(a+b)
result=add(10,5)
print(result)


#exercise 2
def multiply(a,b):
    return(a*b)
print(multiply(4,6))

#exercise 3
def square(number):
    return(number**2)
x=square(7)
print(x)

#exercise 4
def is_even(number):
    return(number%2==0)
print(is_even(7))
print(is_even(8))

#exercise 5
def check_age(age):
    if age>=18:
        return("Adult")
    else:
        return("Minor")

result=check_age(22)
print(result)

print("!part two is finished!")

#part 3==============================================

#exercise 1
def check_number(number):
    if number>0:
        return("positive")
    elif number<0:
        return("negative")
    else:
        return("zero")

#exercise 2
def larger(a,b):
    if a>b:
        return(a)
    elif a<b:
        return(b)
    else:
        return("equal")
print(larger(10,7))



#exercise 3
def count_even(numbers):
    even=0
    for number in numbers:
        if number%2==0:
            even+=1
    return(even)

print(count_even([2,5,8,11,14,17,20]))



##while version 
def count_even(numbers):
    even=0
    i=0
    while i <len(numbers):
        if numbers[i]%2==0:
            even+=1
        i+=1
    return(even)

print(count_even([2,5,8,11,14,17,20]))


#exercise 4
def calculate_sum(numbers):
    result=0
    for number in numbers:
        result+=number
    return(result)
print(calculate_sum([5,10,15]))


##while version 
def calculate_sum(numbers):
    result=0
    i=0
    while i<len(numbers):
        result+=numbers[i]
        i+=1
    return(result)
print(calculate_sum([5,10,15]))





#exercise 5
def find_max(numbers):
    largest=0
    for number in numbers:
        if number>largest:
            largest=number
    return(largest)
print(find_max([4,12,7,25,9]))



##while version 
def find_max(numbers):
    largest=0
    i=0
    while i<len(numbers):
        if numbers[i]>largest:
            largest=numbers[i]
        i+=1
    return(largest)
print(find_max([4,12,7,25,9]))






#exercise 6
def count_vowels(text):
    vowel=["a","e","i","o","u"]
    count=0
    for i in text:
        if i in vowel:
            count+=1
    return(count)
print(count_vowels("Mechanical Engineering"))



##while version 
def count_vowels(text):
    vowel=["a","e","i","o","u"]
    i=0
    count=0
    while i<len(text):
        if text[i] in vowel:
            count+=1
        i+=1
    return(count)
print(count_vowels("Mechanical Engineering"))



print("!part three is finished!")

#part 4==============================================

#exercise 1
def great(name="mohi"):
    return(f"Hello,{name}")
print(great("sara"))
print(great())



#exercise 2
def power(number, exponent=2):
    return(number**exponent)
print(power(5))



#exercise 3
def introduce(name, age=23, major="Mechanical Engineering"):
    return(f"Hi, my name is {name} and i am {age} years old, i study {major}")
print(introduce("Mohi"))
print(introduce("noname","no one knows"))
print(introduce("Ali",30,'electronics'))


#exercise 4
print(introduce(name="masi",age=36,major='IT'))


print("!part four is finished!")


