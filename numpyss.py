import numpy as np

# arr = np.arange(10)
# print(arr)

# arr = np.arange(6)
# print(arr.reshape(2,3))

# my_array = np.array([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=np.uint16)

# print(f"The shape of the array is: {my_array.shape}")
# print(f"The number of dimensions is: {my_array.ndim}")
# print(f"The size of each element in bytes is: {my_array.itemsize}")

# arr = np.ones((3,3))
# print(arr==1)

# arr = np.zeros((3,3),dtype=bool)
# print(arr)

# print(np.info(arange))

# print(np.zeros((1,5)))
# print(np.ones((1,5)))

# print(np.linspace(5,50,5))

# py_list = [1, 2, 3, 4, 5]

# print(np.array(py_list))

# arr = np.arange(10)
# # print(arr.nbytes)
# print(arr[::-1])

# print(np.eye(3))

# arr = np.array([[ 1,  2,  3,  4],
#                         [ 5,  6,  7,  8],
#                         [ 9, 10, 11, 12],
#                         [13, 14, 15, 16]])

# print(arr[0])
# print(arr[:,-1])


# sampleArray = np.array([
#     [3,  6,   9 ,12], 
#     [15, 18, 21, 24], 
#     [27, 30, 33, 36], 
#     [39, 42, 45, 48], 
#     [51, 54, 57, 60]
# ])

# # odd_rows = []
# # even_columns = []


# # for i in range(len(sampleArray)):
# #     if i%2 != 0:
# #         odd_rows.append(i)
    
# # for j in range(sampleArray.shape[1]):
# #     if j%2 ==0:
# #         even_columns.append(j)


# newArray = sampleArray[1::2,::2]
# print(newArray)\


# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# stack = np.hstack((a,b))
# print(stack)

# Array =np.array([
# [ 1,  2,  3,  4],
# [ 5,  6,  7,  8],
# [ 9, 10, 11, 12],
# [ 13, 14, 15, 16]        ])


# print(Array[0:2,0:2])
# print(Array.reshape(8,2))


# arr = np.arange(1, 17)
# print(arr.reshape(4,4)[0:2,0:2])


# arr = np.arange(1,11)
# arr[arr%2 != 0] = -1
# print(arr)


# arr = np.array([1, 0, 2, 0, 3, 0, 4])

# indices = np.nonzero(arr)
# print(indices)


# a = np.array([1, 2, 3, 2, 8, 4, 2, 4])
# b = np.array([2, 4, 5, 6, 8])
# print(np.intersect1d(a,b))


# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(np.add(a,b))
# print(np.subtract(a,b))
# print(np.multiply(a,b))


# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(np.dot(a,b))


# arr = np.array([10, 20, 30, 100, 200, 300])

# print(np.mean(arr))
# print(np.median(arr))
# print(np.std(arr))


# arr = np.arange(10,60,10)

# arr = np.array([10, 20, 30, 40, 50])
# normalized = (arr - arr.min()) / (arr.max() - arr.min())
# print(normalized)



# a = np.array([1, 2, 3, 4, 5])
# b = np.array([1, 4, 3, 7, 8])


# print(np.where(a==b))

# arr = np.arange(20)
# print(arr[(arr>=5)&(arr<=10)])


# arr = np.array([[0.9 ,0.05],
#                           [0.7 ,0.2],
#                           [0.4 ,0.6]])
# print(arr.max())
# print(arr.min())





A = np.array([[1, 2], [3, 4]])

b = np.array([8, 18])

# Solve for x and y
solution = np.linalg.solve(A, b)
print(solution)