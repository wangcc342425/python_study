## 1. for循环
users = ['李少奇','李启航','张三丰', '李子树']
'''
for i in users:
    print(i)

for i in users:
    for ele in i :
        print(ele, end= ' ')
    print(' ')
'''

#练习题： 请通过for循环和数字计数器实现：users = ['李少奇','李启航','张三丰', '李子树']
'''
    0 李少奇
    1 李启航
    2 张三丰
    3 李子树
'''
#方式一
count = 0
for i in users:
    print(count , i)
    count += 1

#方式二
users_len = len(users)
for index in range(0, users_len):
    print(index, users[index])

