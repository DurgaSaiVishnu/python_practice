# def demo(name,age):
#     print(name,age)

# demo("kelly",25)

# def func1(*args):
#     print(args)

# func1(1,2,3,4,5,6,4,2)

# def calculation(a,b):
#     print(a+b,f", {a-b}")

# calculation(40,10)
    


# def show_employee(name,salary=9000):
#     print(name)
#     print(salary)

# show_employee("eren",9000000)
# show_employee("armin")

# def outer(a,b):
#     def inner(a,b):
#         return a+b
#     add = inner(a,b)
#     return add+5

# print(outer(5,10))


# def addition(num):
#     if num:
#         return num + addition(num - 1)
#     else:
#         return 0

# res = addition(10)
# # print(res)

# def display_student(name, age):
#     print(name,age)

# show_studnet = display_student
# show_studnet("emma",26)

# def evens():
#     l = []
#     for i in range(4,30):
#         if i%2 == 0:
#             l.append(i)
#     print(l)

# evens()


# def large(lst):
#     largest = 0
#     for num in lst:
#         if num>largest:
#             largest = num
#     print(largest)

# large([4, 6, 8, 24, 12, 2])

# def describe_pet(animal_type, pet_name):
#     print(f"I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name}.\n")

# describe_pet("hamster", "Harry")

# describe_pet(pet_name="Willie", animal_type="dog")


# def print_info(**kwargs):
#     print(kwargs)

# print_info(name="Alice", age=30, city="New York")


# global_var = 10

# def change():
#     global global_var 
#     global_var = 20

# change()
# print(global_var)

# def factorial(n):
#     if n<=1:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(3))



# squarenum = lambda x: x**2
# print(squarenum(8))


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = list(filter(lambda x: x%2 == 0,nums))
# print(k)


# nums =  [1,2,3,4,5]
# k = list(map(lambda x: x*2,nums))
# print(k)

# grades = [("Alice", 101), ("Bob", 90), ("Charlie", 100)]

# print(sorted(grades,key=lambda grade: grade[1]))


# def apply_operation(k,x,y):
#     return k(x,y)
# def add(a,b): return a+b
# def sub(a,b): return a-b

# print(apply_operation(add,2,3))


# def perfectnumcheck(n):
#     sum = 0
#     for i in range(1,n):
#         if n%i == 0:
#             sum+=i
#     if sum == n:
#         print("its a perfect number")
#     else:
#         print("not a perfect number")

# perfectnumcheck(6)

