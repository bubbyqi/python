# def move(n,a,b,c):
#     if n == 1:
#         print('move',a,'-->',c)
#     else:
#         move(n-1,a,c,b)
#         move(1,a,b,c)
#         move(n-1,b,a,c)
# move(4,'A','B')

# def f(n):
#     if n == 0:
#         return 0
#     else:
#         return 2*f(n-1)+1
# x = int(input('请输入片的个数：'))
# print('需要移动',f(x),'次')
# 阶乘
def fact(n):
    if n == 1:
        return 1
    return  n *  fact(n-1)
print('fact(1)',fact(1))
print('fact(5)',fact(5))
print('fact(10)',fact(10))