# def gen(n):
#     for i in range(n):
#         yield i
#
# for i in gen(5):
#     print(i)

# def func(num):
#     return num+10
# def my_map(func,iterable):
#     for i in iterable:
#         yield func(i)
# print(list(my_map(func,[1,2,3,4,5,6])))

l=(i for i in range(10))
print(tuple(l))