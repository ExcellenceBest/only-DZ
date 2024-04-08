
# from collections import deque
# def window(lst: list, a: int) -> list[int]:
#     from collections import deque
#     dq = deque(maxlen=k)
#     result = []
#     for i in nums:
#         dq.append(i)
#         if len(dq) == k:
#             result.append(max(dq))
#     return result
#
# nums = [6, 2, 3, 7, 0, 1]
# k = 3
# window(nums, k)
# import random
#
# def func(arr: list) -> list:
#     stack = []
#     result = []
#     if len(arr) == 0:
#         return arr
#     else:
#         for i in arr:
#             if len(stack) == 0 or i**2 <= stack[-1]:
#                 stack.append(i**2)
#             elif i ** 2 > stack[-1] or len(stack) == 0:
#                 result.append(stack.pop())
#                 while len(stack) != 0 and i ** 2 > stack[-1]:
#                     result.append(stack.pop())
#                     continue
#                 stack.append(i ** 2)
#     while len(stack) > 0:
#         result.append(stack.pop())
#     return result
# q = sorted([random.randint(-10, 10) for i in range(15)])
# #q = [-8, -8, -6, -5, -4, -2, -2, -1, 1, 3, 5, 6, 8, 9, 10]
# print(q)
# # array = [-5, -3, 1, 2, 4, 6]
# # a = func(array)
# # print(a)
# w = func(q)
# print(w)

arr = [-11, -10, 3, 4, 5, 6, 7, 8, 9]
result = []
count = 0
for i in arr:
		if i < 0:
			result[len(arr)-1-i] = i * i
			count += 1
		else:
			result[i-count] = i * i
print(result)

