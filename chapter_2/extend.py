#extend
'''
1.有列表    users= ['李忠伟','唐开发']  people = ['李鹏','张师傅']
    users.extend(people)    #users中增加
    people.extend(users)    #people中增加

2.有列表    users= ['李忠伟','唐开发']  元组：people = ('李鹏','张师傅')
    users.extend(people)    #users中增加
    people.extend(users)    #只有列表有extend功能，元组是没有的
'''


for i in range(0,101,2):
    print(i)