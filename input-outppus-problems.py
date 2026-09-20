# a = int(input("enter a num: "))
# b = int(input("enter a num: "))
# print(f"the  multiplication is {a*b}")\

# print("name","is","james",sep="***")

# a = int(input("enter a num: "))
# print('%o' %a)

# a = int(input("enter a num: "))
# print(bin(a))
# print(f"{a:b}")

# str1 ,str2,str3 = input("enter ur name: ").split()
# print('name1: ',str1)
# print('name2: ',str2)
# print('name3: ',str3)

# a = int(input("enter a num: "))
# print(f"{a:x}")

# a = float(input("enter a num: "))
# print(f"{a:.2f}")

# a = float(input("enter a numerator: "))
# b = float(input("enter a denominator: "))
# print(f"{(a/b)*100:.2f}%")

# word = input("Enter a word: ")
# version = input("Enter a version number: ")

# print(f"{word:>10} {version}")


# title = input("title: ")
# print(f"{title:-^40}")
# word = input("Enter a word: ")
# version = input("Enter a version number: ")


# a = input("enter a num: ")
# print(a.zfill(5))

# quantity = 3
# totalMoney = 450
# price = 150
# statement = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."

# print(statement.format(quantity, totalMoney, price))


# amount = 1250500.7
# print(f"{amount:.2f}")


# f = []
# for i in range(5):
#     a = float(input("enter a num: "))
#     f.append(a)

# print(f)

# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]
# print("Name     Score")
# print("*"*15)
# for name , score in zip(names,scores):
#     print(f"{name:<10}{score}")




# import sys

# while True:
#     try:
#         a = int(input("enter num 1-3: "))
#         if a == 1:
#             print("hello")
#             break
#         elif a == 2:
#             b = int(input("enter a num to square: "))
#             print(b**2)
#             break
#         elif a == 3:
#             sys.exit()
#         else:
#             print("enter a valid number from the given options")
#     except ValueError:
#         print("enter a valid number from the given options")


# import getpass

# user = input("Enter Username: ")
# pwd = getpass.getpass("Password: ")

# if user == "admin" and pwd == "SecretPassword123":
#     print(f"Login successful for {user}!")
# else:
#     print("Access Denied.")

# q = []
# with open("test.txt","r") as f:

#     s = f.readlines()
#     q.extend(i.strip() for i in s)
    
#  print(q)


# fruit_list = ["Apple", "Banana", "Cherry", "Date"]
# with open("fruits.txt","w") as f:
#     f.writelines(f"{fruit}\n" for fruit in fruit_list)

# lineC = 0
# with open("fruits.txt","r") as f:
#     for line in f:
#         lineC +=1

# print(lineC)


# import os

# filename = "test.txt"
# if os.path.exists(filename):
#     file_info = os.stat(filename)
#     if file_info.st_size == 0:
#         print(f"Status: {filename} is empty.")
#     else:
#         print(f"Status: {filename} size is {file_info.st_size} bytes.")
# else:
#     print("File not found.")

# import os

# file = os.stat("fruits.txt")
# print(file.st_size)


# import os

# user = input("enter file you want to delete: ")
# if os.path.exists(user):
#     os.remove(user)
# else:
#     print("file not found")



