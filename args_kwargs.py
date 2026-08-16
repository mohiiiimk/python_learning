#exercise 1
def multiply_all(*numbers):
    multi=1
    for number in numbers:
        multi=number*multi
    return multi

print(multiply_all(2,3,4))


#exercise 2
def show_items(*items):
    for item in items:
        print(item)

show_items("Python", "MATLAB", "Fluent", "SolidWorks")

#**kwargs===================================================================
#exericse 1
def show_info(**info):
    print(info)

show_info(name="Mohi", age=23, major="Mechanical Engineering")


#exericse 2
def calculate_sum(**numbers):
    summation=0
    for number in numbers.values():
        summation=number+summation
    return(summation)

print(calculate_sum(a=10, b=20, c=30))


#exericse 3
def student_info(*subjects,**details):
    print(f"subjects:{subjects},details:{details}")

student_info("python","matlab","cfd",name="mohi",age=23)




#exericse 4
def calculate(*numbers, **options):
    summation = 0
    multi=1
    if options["operation"] == "sum":
        for number in numbers:
            summation += number
        print(summation)
    elif options["operation"]=="multiply":
        for number in numbers:
                multi *= number
        print(multi)

calculate(10, 20, 30, operation="sum")
calculate(10, 20, 30, operation="multiply")