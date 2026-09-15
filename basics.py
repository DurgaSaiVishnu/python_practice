# a = int(input("enter an numm: "))
# b = int(input("enter an numm: "))
# if a*b<=1000:
#     print(a*b)
# else:
#     print(a+b)

# for i in range(10):
#     if i == 0:
#         print(f"current num: 0 ,previous num: 0 Sum: 0")
#     else:
#         print(f"current num: {i} ,previous num: {i-1} Sum: {i+i-1}")

# char = input("enter a string: ")
# n = int(input("enter no of chars to truncate: "))
# def remove_chars(char,n):
#     c = list(char)
#     for i in range(n):
#         c.pop(0)
#     return "".join(c)

# print(remove_chars(char,n))


# a = 5
# b = 6
# a,b = b,a
# print(f"a={a},b={b}")


# text = "python"
# print(text[::-1])

# n = int(input("enter num: "))
# k = 1
# for i in range(1,n+1):
#     k = k*i
# print(k)

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# fruits.append("fig")
# fruits.pop(1)
# print(fruits)


# k = 0
# sentence = "Learning Python is funoooooo!"
# s = list(sentence)
# vowels = ['a','e','i','o','u']
# for i in sentence:
#     if i in vowels:
#         k+=1
# print(k)

# numbers_x = [10, 20, 30, 40, 50]
# if numbers_x[0] == numbers_x[-1]:
#     print(True)
# else:
#     print(False)



# k = []
# num_list = [10, 20, 33, 46, 55]
# for i in num_list:
#     if i%5  == 0:
#      print(i,end=",")


# str_x = "Emma is good developer. Emma is a writer"
# print(str_x.count("Emma"))


# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# n = int(input("enter an num: "))

# def palindrome_checker(n):
#     k = str(n)
#     if k[::-1] == k[::]:
#         print(True)
#     else:
#         print(False)

# palindrome_checker(n)


# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# final_list = []

# for i in list1:
#     if i%2 == 0:
#         final_list.append(i)
# for i in list2:
#     if i%2 != 0:
#         final_list.append(i)
# print(final_list)




# num = int(input("num: "))
# while num>0:
#     digit = num%10
#     num = num//10
#     print(digit,end="")





# income = int(input("enter salary: "))
# if income<=10000:
#     payable_tax = 0
# elif income>10000 and income<=20000:
#     payable_tax = (income - 10000)*(10/100)
# else:

#     payable_tax =  (10000)*(10/100)
#     payable_tax += (income - 20000)*(20/100)
# print(f"payable tax : {payable_tax}")


# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end="\t")
#     print()

# for i in range(6):
#     for j in range(6,i,-1):
#         print("*",end=" ")
#     print()



# def exponent(base,exp):
#     k = base
#     for i in range(1,exp):
#         k *= base
#     return k

# print(exponent(2,10))




# a = 123

# orignal = a
# reversed_num = 0
# while a > 0:
#     digit = a%10
#     reversed_num = reversed_num*10 + digit
#     a //= 10
# print(reversed_num)



# year = int(input("enter an year: "))
# if year%4 == 0:
#     print("Leap Year")
# elif year%100 == 0 and year%400 != 0:
#     print("Leap year")
# else:
#     print("Not a leap year")



# dict1 = {"name": "Alice", "age": 25}
# dict2 = {"city": "New York", "job": "Engineer"}
# merge = dict1|dict2
# print(merge)


# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6, 7, 8]

# print(set(a) & set(b))

# words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
# for word in words:
#     word = list(word)
#     print("".join(word),"-",len(word),end=" ")


# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

# text = "apple banana apple eren eren mikasa mikasa cherry banana apple"
# words = text.split()
# frequency = {}
# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1

# print(frequency)




# p = []
# n = int(input("enter num: "))
# for i in range(2,n+1):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         p.append(i)

# print(p[::2])

# s = {}
# for i in range(1,11):
#     s.update({i:i**2})
# print(s)

# string = "I love coding in Python"
# print(string.replace(" ","_"))



# STOPPED AT NUMBER 35


# string = "Pythone3r"
# is_digit = False
# for i in string:
#     if i.isdigit():
#         is_digit = True
# print(is_digit)



# text = "hello world from python"

# words = text.split()
# capitalWords = []
# for word in words:
#     capitalWords.append(word.capitalize())

# print(" ".join(capitalWords))



# import time

# start_count = int(input("enter countdown: "))
# while start_count>0:
#     print(start_count,end=" ")
#     time.sleep(1)
#     start_count -= 1
# print("Blast off !")


# with open("notes.txt","w") as file:
#     file.write("Hello, this is my first note\n")
#     file.write("Python file handling is simple\n")
#     file.write("“End of file.”")
# with open("notes.txt","r") as file:
#     content = file.read()
#     print(content)
    
# with open("notes.txt","r") as file:
#     data = file.read()
#     words = data.split()
#     count = 0
#     for word in words:
#         count += 1
# print(count)

# import platform
# import datetime

# print(platform.system())
# print(dir(platform))
# print(datetime.datetime.now())

# import re

# txt = "hello world"
# x = re.search("l",txt)
# if x:
#     print("Yes")
# else:
#     print("no")

# class myclass:
#     x = 5

# p = myclass()
# print(p.x)


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
# p = Person("eren",19)
# print(p.age)\



# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def start_engine(self):
#         print(f"The {self.year} {self.model} {self.make} engine is now running!")

# car1 = Car(input("enter make : "),input("enter model: "),input("enter year: "))
# car1.start_engine()




