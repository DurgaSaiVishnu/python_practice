# i = 1

# while i<11:
#     print(i)
#     i+=1


# for i in range(-10,0,1):
#     print(i)


# for i in range(5):
#         print(i)
#         if i == 3:
#             break
# else:
#     print("Done!")


# try:
#     n = int(input("enter a num: "))
# except ValueError:
#     print("enter valid number")

# k = 0

# for i in range(n+1):
#     k += i
# print(k)    



# try:
#     n = int(input("enter a num: "))
# except ValueError:
#     print("enter valid number")

# for i in range(1,11):
#     print(i*n)



# try:
#     n = int(input("enter a num: "))
# except ValueError:
#     print("enter valid number")

# for i in range(1,n+1):
#     print(f"current Number is : {i} and the cube is {i**3}")


# numbers = [12, 75, 150, 180, 145, 525, 50]

# for num in numbers:
#     if num>500:
#         break
#     elif num>150:
#         continue
#     elif num%5 == 0:
#         print(num)


# list1 = [10, 20, 10, 30, 10, 40, 50]
# target = int(input("enter your target: "))
# frequency = 0
# for num in list1:
#     if num == target:
#         frequency+=1
# print(f"frequency of {target} is {frequency}")



# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# s = []
# for num in range(1,len(my_list),2):
#     s.append(my_list[num])
# print(s)


# list1 = [10, 20, 30, 40, 50]

# print(list(reversed(list1)))


# string = "python"
# for i in range(len(string)-1,0,-1):
#     print(string[i],end="")


# sentence = input("enter a sentence: ")
# vowels = ['a','e','i','o','u']
# vowel = 0
# consonants = 0
# for word in sentence:
#     if word  in vowels:
#         vowel += 1
#     else:
#         consonants += 1

# print(f"vowels: {vowel} and consonats: {consonants}")

# largest = 0
# minimum = 9
# num = int(input("enter a num: "))
# while num>0:
#     digit = num%10
#     num //= 10
#     largest = max(largest,digit)
#     minimum = min(minimum,digit)

# print(f"{largest} is the largest number and smallest number is {minimum}")

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
    
# for i in range(1,21,2):
#     print(i,end=" ")

# num = int(input("enter a num: "))
# reversedNum = 0
# while num>0:
#     digit = num%10
#     reversedNum = reversedNum*10 + digit
#     num //=10
# print(reversedNum)




# from time import sleep

# n = int(input("enter a num: "))
# print(n,end=" ")
# while n!=1:
#     if n%2 == 0:
#         n = n//2
#         sleep(2)
#         print(n,end=" ")
#     elif n%2 != 0:
#         n = n*3+1
#         sleep(2)
#         print(n,end=" ")

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()


# for i in range(5):
#     for j in range(i+1):
#         print(chr(65+i),end=" ")
#     print()


# n = int(input("enter num: "))

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n = int(input("enter num: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# for i in range(n-1,0,-1):
#     for j in range(0,i):
#         print("*",end=" ")
#     print()

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end=" ")
#      print()

# currentsum = 0
# cumulative_sum = []
# list1 = list(map(int,input("enter nums: ").split()))
# for num in list1:
#     currentsum += num
#     cumulative_sum.append(currentsum)

# # print(cumulative_sum)


# text = input("enter string of chars: ")
# l = list(text)
# for t in range(len(l)-1,0,-2):
#     l[t] = l[t].capitalize()

# print(" ".join(l))

# scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60}
# passing_students = {}
# threshold = 75
# for name,score in scores.items():
#     if score>threshold:
#         passing_student = {name:score}
#         passing_students.update(passing_student)
    
# print(passing_students)



# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6, 7, 8]

# common_elements = []

# for i in a and b:
#     common_elements.append(i)
# print(common_elements)

# a = [1, 2, 2, 3, 4, 4, 4, 5]

# unique = []
 
# for num in a:
#     if num not in unique:
#         unique.append(num)
# print(unique)

# nums = [1,2,3,4,5,6]
# evens = []
# odds= []
# for num in nums:
#     if num%2==0:
#         evens.append(num)
#     else:
#         odds.append(num)

# total = evens+odds  
# print(total)

# nums = [1, 2, 3, 4, 5]
# k = 2

# for i in range(k):
#     temp = nums.pop(0)
#     nums.append(temp)
# print(nums)


# text = "apple banana apple orange banana apple"
# s = text.split()
# dic = {}
# count = 0
# for word in s:
#         if word in dic:
#             dic[word] += 1
#         else:
#             dic[word] = 1
# print(dic)


# num1 = 0
# num2 = 1
# n = 10
# for i in range(10):
#     print(num1,end=" ")
#     res = num1+num2
#     num1= num2
#     num2 = res

# print(res)


# num = 6
# divisorr_sum = 0
# for i in range(1,num//2+1):
#     if num%i == 0:
#         divisorr_sum += i
# if divisorr_sum == num:
#     print(f"{num} is perfect")
# else:
#     print(f"{num} is not perfect")


# sum = 0
# binary_str = "1111"
# s = list(map(int,binary_str))
# for i  in range(len(s)):
#     sum += (2**i)*(s[len(s)-1-i])
# print(sum)


# start = int(input("enter start num: "))
# end = int(input("enter end num: "))
# primes = []
# for i in range(start,end//2 + 1):
#     if i<2:
#         continue
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         primes.append(i)
# print(set(primes))


# num = 2
# sum = 0
# n = int(input("enter a num: "))
# for i in range(n):
#     sum += num
#     num = num*10 + 2
# print(sum)

# nested_list = [[10, 20], [30, 40], [50, 60]]
# lista = []
# for lists in  nested_list:
#     for j in lists:
#         lista.append(j)
# print(lista)


# matrix = [[10, 20], [30, 40], [50, 60]]
# target = int(input("enter num to find: "))

# for sublist in matrix:
#     for i in sublist:
#         if i == target:
#             print("row: ",matrix.index(sublist), "column: ",sublist.index(i))

