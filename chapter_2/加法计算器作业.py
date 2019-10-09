'''
实现一个整数加法计算器（两个数相加）
如：content = input （“请输入内容”），用户输入5+9或5+ 9，或5 + 9，然后进行分割转换最终进行整数的计算得到结果
'''

content = input('请输入：') # 5+9或5+ 9，或5 + 9
'''
# 思路一：
content = content.strip()
v1 = int(content[0])
v2 = int(content[-1])
v3 = v1 + v2

#思路二：
content_len = len(content)
index = 0
total = 0
while True:
    char = content[index]
    if char.isdigit():
        total += int(char)
    index += 1
    if index == content_len:
        break
print(total)'''

#思路三：
result = content.split()
print(result)   #['55', '+99']
v1 = int(result[0])
print(v1)# 55
v2 = int(result[-1])
print(v2)   # 99
v3 = v1 + v2
print(v3)


