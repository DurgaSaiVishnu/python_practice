# str1 = input("enter a string: ")
# middle = (len(str1)-1)//2
# print(str1[0],str1[middle],str1[len(str1)-1])

# str1 = input("enter a string: ")
# middle = (len(str1)-1)//2
# print(str1[middle-1],str1[middle],str1[middle+1])

# def append_middle(s1,s2):
#     s3 = list(s1)
#     middle = (len(s1))//2
#     s3.insert(middle,s2)
#     print("".join(s3))


# append_middle("Ault","Kelly")


# def name(s1,s2):
#     s3 = list(s1)
#     s4 = list(s2)
#     s5 = []
#     middle1 = len(s3)//2
#     middle2 = len(s4)//2
#     s5.append(s3[0])
#     s5.append(s4[0])
#     s5.append(s3[middle1])
#     s5.append(s4[middle2])
#     s5.append(s3[len(s3)-1])
#     s5.append(s4[len(s4)-1])

#     return s5

# k = name("America","Japan")
# print("".join(k))


# str1 = "pynative"
# print(str1[::-1])

# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# print(str1.rfind("Emma"))

# str1 = "Emma-is-a-data-scientist"
# print(str1.split("-"))
# print("displaying every substring: ")
# for s in str1.split("-"):
#     print(s)


# str1 = "Welcome to USA. usa awesome, isn't it?"
# k = str1.lower()
# print(k.count("usa"))

# str1 = "Welcome to USA. usa awesome, isn't usa it?"
# lowercase = str1.lower().split()
# count = 0
# substring = "usa"
# for i in lowercase:
#     cleanword = "".join(char for char in i if char.isalnum())
#     if cleanword == substring:
#         count+=1
# print(count)

# s1 = "ynd"
# s2 = "PyNative"
# balanced = True
# for i in s1.lower():
#     if i in s2.lower():
#         continue
#     else:
#         balanced = False
#         break

# if balanced:
#     print("balanced")
# else:
#     print("not balanced")

# def vowel_counter(s1):
#     count = 0
#     vowels = ['a','e','i','o','u']
#     for word in s1.lower():
#         if word in vowels:
#             count+=1
#     print(count)

# vowel_counter("hello wOrld")

# def url_checker(s1):
#     valid = False
#     if s1.startswith("https") and s1.endswith(".com"):
#         valid = True
#     return valid
    
# print(url_checker("htptps:/google.com"))


# def transform(str1):
#     res = str1.swapcase()

# def name(s1,s2):
#     firstchar = s1[0]
#     middlechar = s1[len(s1)//2]
#     lastchar = s1[len(s1)-1]
#     secondchar = s2[0]
#     middle2ndchar = s2[len(s2)//2]
#     last2ndchar = s2[len(s2)-1]
#     res = firstchar + secondchar + middlechar + middle2ndchar + lastchar + last2ndchar
#     print(res)

# name("America","Japan")
#     return res

# print(transform("hKl"))

# def swap(str1):
#     s = list(str1)
#     swapped = []
#     for word in s:
#         if word.isupper():
#             swapped.append(word.lower())
#         else:
#             swapped.append(word.upper())
#     return "".join(swapped)

 # print(swap("hellOKK"))

# def remove_spaces(str1):
#     s = str1.replace(" ","")
#     return s

# print(remove_spaces("P Y T H O N"))

# def remove_index(str1,index):
#     s = list(str1)
#     s.pop(index)
#     return s

# r = remove_index("Python",2)
# print("".join(r))


# str1 = "usernamecompany.com"
# res = str1.partition("@")
# print(res)

# file_name = "report_final_v2.pdf"
# extension =  []
# name = list(file_name)
# dot = "."
# s = file_name.rfind(".")
# # print(file_name[s+1:])


# str1 = "PyNaTive"

# lower = []
# upper = []

# for word in str1:
#     if word.isupper():
#         upper.append(word)
#     else:
#         lower.append(word)

# res = lower+upper
# print("".join(res))


# str1 = "P@#yn26at^&i5ve"

# chars = 0
# Digits = 0
# symbol = 0

# for char in str1:
#     if char.isdigit():
#         Digits+=1
#     elif char.isalpha():
#         chars +=1
#     else:
#         symbol +=1

# print(f"total counts of chars digits and symbols : {chars},{Digits},{symbol}")


# s1 = "AAAbccc"
# s2 = "Xyz"
# s3 = []
# length = s1 if len(s1)>len(s2) else s2
# for i in range(len(length)):
#         if i<len(s1):
#             s3.append(s1[i])
#         if i<len(s2):
#             s3.append(s2[len(s2)-1-i])


# print("".join(s3))

# str1 = "PYnative29@#8496"
# nums = []
# for char in str1:
#     if char.isdigit():
#         nums.append(char)
# print(sum(map(int,nums)))
# print(f"{sum(map(int,nums))/len(nums):.2f}")


# str1 = "apple"
# d = {}
# for char in str1:
#     d.setdefault(char,1)

# print(d)

# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]


# for char in str_list:
#     if char == None or char == "":
#         str_list.pop(str_list.index(char))

# print(str_list)


# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# newlst = list(filter(None,str_list))
# print(newlst)


# str1 = "/*Jon is @developer & musician!!"
# cleanedword = ""
# for char in str1:
#     if char.isalnum() or char.isspace():
#         cleanedword += char
# print("".join(cleanedword))


# str1 = "I am 25 years and 10 months old"

# digits = ""

# for char in str1:
#     if char.isdigit():
#         digits += char

# print(digits)

# str1 = "I am 25 years and 10 months old"

# digits = [char for char in str1 if char.isdigit()]
# print("".join(digits))


# str1 = "Emma25 is Data scientist50 and AI Expert"

# numwords = []

# for word in str1.split():
#         if any(char.isalpha() for char in word ) and any(char.isdigit() for char in word):
#             numwords.append(word)
# print(" ".join(numwords))



# str1 = "/*Jon is @developer & musician!!"

# changedsentence = []

# for char in str1:
#     if char.isalnum() or char.isspace():
#         changedsentence.append(char)
#     else:
#         changedsentence.append("#")
# print("".join(changedsentence))


# import string

# str1 = "/*Jon is @developer & musician!!"

# lst = string.punctuation

# for char in lst:
#     str1 = str1.replace(char,"#")

# print(str1)

# str1 = "apple"
# dic = {}
# for char in str1:
#     if char in dic:
#         dic[char] += 1
#     else:
#         dic[char] = 1
# print(dic)


# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# filtered_list = list(filter(None,str_list))
# print(filtered_list)



# file_name = "report_final_v2.pdf"

# extension = file_name.split(".")[-1]

# print("File Name:", file_name)
# print("Extension:", extension)


# str1 = input("enter a word: ")

# if len(set(str1)) == len(str1):
#     print("unique")
# else:
#     print("not unique")



# str1 = "hello world from python"
# newstr = ""
# for word in str1.split():
#     newstr += word[0].capitalize()+word[1:]


# print(newstr)


# str1 = "google"

# noduplicate = []

# for letter in str1:
#     if letter not in noduplicate:
#         noduplicate.append(letter)
# print("".join(noduplicate))


# str1 = "python is fun"
# newstr = []
# for word in str1.split():
#     newstr.append(word)

# print(" ".join(newstr[::-1]))



# s1 = "ABC"
# s2 = "xyz"
# newword = []

# for l1,l2 in zip(s1,s2):
#     newword.append(l1)
#     newword.append(l2)

# print("".join(newword))


# str1 = "The quick brown fox jumps over the lazy dog"
# longest = ""
# for word in str1.split():
#     if len(longest)<len(word):
#         longest = word

# print(longest)


# str1 = "Random Access Memory"

# shortform = ""

# for word in str1.split():
#     shortform += word[0]

# print(shortform)


# str1 = "apple banana apple cherry banana hello hello apple"

# dic = {}

# for word in str1.split():
#     if word in dic:
#         dic[word] += 1
#     else:
#         dic[word] = 1


# print(dic)


# str1 = "swiss"

# dups = {}

# for letter in str1:
#     if letter in dups:
#         dups[letter] += 1
#     else:
#         dups[letter] = 1

# for key in dups:
#     if dups[key] == 1:
#         print(key)
#         break


