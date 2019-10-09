# ##独有功能#
# users = []
# users.append('wcc')
# print(users)
#
# ### 示例一：
# #1. 在列表最后追加一个元素
# users = []
# '''while True:
#     mane = input("请输入姓名：")
#     users.append(mane)
#     print(users)
# '''
# ### 示例二：
# #录入用户名和密码
# for i in range(0, 3):
#     name = input("请输入姓名：")
#     result = users.append(name)
# print(users)
#
# #用户名和密码进行校验
# username = input("请输入用户名：")
# password = input("请输入密码")
# for item in users:
#     result = item.split(',')
#     user = result[0]
#     pwd = result[1]
#     if user == username and pwd == password:
#         print("登录成功")
#         break
#
#
#
# 2. insert -- 在指定索引位置进行插入元素
users = ['李少奇','李启航','张三丰', '李子树']
users.insert(1, 'wcc')
print(users)

#3.remove -- 删除
users = ['李少奇','李启航','张三丰', '李子树']
users.remove('张三丰')
print(users)

#4.pop -- 删除
users = ['李少奇', '张三丰','李启航','张三丰', '李子树']
# users.pop(1)
users.pop() #不加，默认删除最后一个
print(users)

# 5.clear -- 清空
users = ['李少奇', '张三丰','李启航','张三丰', '李子树']
users.clear()
print(users)



