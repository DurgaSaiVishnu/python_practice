# nums = [8]
# print(len(nums) == 0)

# nums = [2,3,5,7]
# print(max(nums))
# print(min(nums))
# sum = 0
# for i in nums:
#     sum+=i

# print(sum(nums))
# print(sum/len(nums))

# p = 1

# for num in nums:
#     p *= num

# print(p)

# numbers = [10, 21, 4, 45, 66, 93, 11]
# even_nums = [n for n in numbers if n%2==0]
# odd_nums = [n for n in numbers if n%2!=0]
# print("even numbers: ",len(even_nums))
# print("odd numbers: ",len(odd_nums))

# a =  [56, 12, 89, 3, 22]
# a.sort()
# print(a)

# ListA = ["Physics", "Chemistry"]
# ListB = ["Maths", "Biology"]
# ListA.extend(ListB)
# print(ListA)
# print(ListA+ListB)

# lst = [23,65,19,90]
# lst[0],lst[2] = lst[2],lst[0]
# print(lst)

# nestedlst = [[1, 2], [3, 4, 5], [6, 7]]
# print(nestedlst[1][2])

# inventory = ["Laptop", "Mouse", "Monitor", "Keyboard"]
# target = input("enter a target: ")
# for item in inventory:
#     if item.lower() in target:
#         print(item," is available")
#         break
# else:
#     print(target,"not avaiable")

# words = ["PHP", "Exercises", "Backend", "Python"]
# longest = ""
# for word in words:
#     if len(longest)<len(word):
#         longest = word

# print(longest)

# nums = [1, 2, 3, 4, 5]
# sq_nums = [num**2 for num in nums]
# print(sq_nums)
# print(nums.count(3))

# nums = [5, 20, 15, 20, 25, 50, 20]
# cleanedlst = [num for num in nums if num != 20]
# print(cleanedlst)

# names = ["Mike", "", "Emma", "Kelly", "", "Brad",None]
# filtered = list(filter(None,names))
# print(filtered)

# duplicates = [10, 20, 10, 30, 40, 40, 20, 50]

# unique_list = list(dict.fromkeys(duplicates))

# print(f"Unique List: {unique_list}")

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evennums = list(filter(lambda x: x%2==0,nums))
# print(evennums)

# a = ["Py", "is", "awes"]
# b = ["thon", " ", "ome"]
# new = [i+j for i,j in zip(a,b)]
# print(new)

# a = [10, 20, 30]
# b =  [100, 200, 300]
# for i , j in zip(a,b):
#     print(i,j)

# lst = [10, 20, 30, 40, 50]
# target = 30
# lst.index(target)
# lst.insert(target+1,35)
# print(lst)



# lst = [5, 10, 15, 20, 25]

# target = int(input())

# lst[lst.index(target)] = 200
# print(lst)


# nums = [12, 35, 1, 10, 34, 1, 35]
# st = set(nums)
# print(list(st)[1])



# def get_mode(nums):
#     dic = {}
#     for num in nums:
#         if num in dic:
#             dic[num] += 1
#         else:
#             dic[num] = 1
#     mode = max(dic.values())
#     maxkey =  [key for key,value in dic.items() if value == mode]
#     return maxkey

# print(get_mode([1,2,3,2,1,1,4,3,3,3])


# def skip(lst,n):
#     newlst =  lst[::n]
#     return newlst

# print(skip(['a', 'b', 'c', 'd', 'e', 'f', 'g'],3))

# def list_palindrome(lst):
#     if lst[::1] == lst[::-1]:
#         print("palindrome")
#     else:
#         print("not palindorme")

# list_palindrome([1, 2, 3, 5, 1])


# def intersection(lst1,lst2,lst3):
#    return  set(lst1) & set(lst2) & set(lst3)

# print(intersection([1, 5, 10, 20],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80]))


# def check_sorted(nums):
#     nums = list(nums)
#     return nums == nums.sort()

# print(check_sorted([10,20,30,25,40]))



# def check_sorted(nums):
#     nums = list(nums)
#     for i in range(len(nums)-1):
#         if nums[i] > nums[i+1]:
#             return False
#             break
#     else:
#         return True

# print(check_sorted([10, 20, 30, 35 ,40,40]))


# keys =  ["name", "age", "city"]
# values =  ["Alice", 25, "New York"]
# dic = {}

# for key,value in zip(keys,values):
#     dic[key] = value

# print(dic)


# def list_diff(a,b):
#     return set(a) - set(b)

# print(list_diff([1, 2, 3, 4, 5],[2,4,6]))


# def get_diff(a,b):
#     return [num for num in a if num not in b]

# print(get_diff([1, 2, 3, 4, 5],[2, 4, 6]))


# def rmvngtv(nums):
#     return [num for num in nums if num>=0]

# print(rmvngtv([10, -5, 20, -1, 0, -8]))

# def nestappend(lst):
#     for i in range(len(lst)):
#         lst[i].append("elderberry")
#     return lst

# print(nestappend([['apple', 'banana'], ['cherry', 'date']]))



# def mixlist(a,b):
#     mixedlist =  [x+y for x in a for y in b]
#     return mixedlist

# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# flattened_list = []

# for sublist in nested_list:
#     for num in sublist:
#         flattened_list.append(num)

# print(flattened_list)

# def flatten_list(nestedlist):
#     flattenedList = []
#     for sublist in nestedlist:
#         if type(sublist) is list:
#             flattenedList.extend(flatten_list(sublist))
#         else:
#             flattenedList.append(sublist)
#     return flattenedList

# print(flatten_list([1, [2, [3, 4], 5], 6, [7, 8]]))

# def cumulativesum(nums):
#     newlst = []
#     current_sum = 0
#     for num in nums:
#         current_sum += num
#         newlst.append(current_sum)
#     return newlst

# print(cumulativesum([10,20,30,40]))




# def rotate_list(lst,k):
#     k = k%len(lst)
#     return lst[k:] + lst[:k]

# print(rotate_list([1,2,3,4,5],3))


# def chunkify(nums,n):
#     newlst = [nums[i:i+n] for i in range(0,len(nums),n)]
#     return newlst


# print(chunkify([1,2,3,4,5,6,7,8,9,10,11],2))


# lst = [0,1,0,3,12]
# for num in lst:
#     if num == 0:
#        value = lst.pop(lst.index(num))
#        lst.append(value)
# print(lst)


# def primenums(n):
#     primenums = [num for num in range(2,n) if all (num%i != 0 for i in range(2,num))]
#     return set(primenums)

# print(primenums(20))


    
