# a = ["apple", "bat", "cherry", "dog", "elderberry"]   
# FilteredWords = [i.upper() for i in a if len(i)>=4]
# print(FilteredWords)


# def merge(d1,d2):
#     for key,value in d2.items():
#         d1[key] = d1.get(key,0) + value
#     return d1

# dict_a = {'a': 10, 'b': 20}
# dict_b = {'b': 5, 'c': 15}

# merged = merge(dict_a,dict_b)
# print(merged)

# def count():
#     import collections
#     s = list(input("enter a string: ").lower())
#     print(collections.Counter(s))

# count()



# def check_anagram():
#     word1 = list("listejen")
#     word2 = list("silejnt")
#     if len(word1) != word2:
#         print("not an anagram")
#         return

#     for word in word1:
#         if word in word2:
#             continue
#         else:
#             print("not an Anagram")
#             break
#     else:
#         print("anagram")

# check_anagram()



# def flatten(nested_list):
#     flat = []
#     for sublist in nested_list:
#         if isinstance(sublist,list):
#             flat.extend(flatten(sublist))
#         else:
#             flat.append(sublist)
#     return flat
# nested_list = [1, [2, 3], [4, [5, 6]], 7]
# print(flatten(nested_list))

# text = "Python is awesome"
# reversed = []
# r = list(text.split())
# for word in r:
#     reversed.append(word[::-1])

# print(" ".join(reversed))


# def palindrome(string):
#     s = "".join(char.lower() for char in string if char.isalnum())
    
#     return s == s[::-1]

# print(palindrome("A man, a plan, a canal: Panama"))

# a = ["apple", "education", "ice", "ocean", "python", "umbrella"]
# vowels = ['a','e','i','o','u']
# b = []
# for string in a:
#     if len(list(string))>5 and string[0] in vowels:
#         b.append(string)
# print(b)


# def detect(lst):
#     a = []
#     for i in lst:
#         if i not in a:
#             a.append(i)
#     return a
# print(detect([1,2,2,3,1,4,2]))

# reversed_num = 0
# n = int(input("enter a num: "))
# while True:
#     temp = n
#     reversed_num = 0
#     while temp>0:
#         digit = temp%10
#         reversed_num = reversed_num*10 + digit
#         temp//=10
#     if reversed_num == n:
#         print(f"\npalindrome found:{reversed_num}")
#         break
#     else:
#         print(f"{n}+{reversed_num}=",end=" ")
#         n = n+reversed_num


# n = int(input("enter a num: "))
# odd = []
# sum = 0
# for i in range(n+1):
#     if i%2!=0:
#         odd.append(str(i))
#         sum+=(i)
# print(" + ".join(odd),end=" ",flush=True)
# print(f"= {sum} = {sum**0.5:.0f}^2")


# def rotate_list(lst, n,direction):
#     if direction.lower() == "left":
#         for i in range(n):
#                 value = lst.pop(0)
#                 lst.append(value)
#                 print(lst)
#     else:
#         for i in range(n):
#                 value = lst.pop()
#                 lst.insert(0,value)
#                 print(lst)
# rotate_list([1,2,3,4],1,"right")

