# d={}
# for i in range(int(input())):
#     s=input()
#     d[s.lower()]=d.get(s.lower(),[])+[s]
# # print(d)
# ss=input().split()
# mist_count=0
# for c in ss:
#     upper_count=0
#     for cc in c:
#         # print(cc)
#         if cc.isupper():   # считаю количество заглвных букв
#             upper_count+=1
#     # print(upper_count)
#     if upper_count!=1:     # если заглавных не одна + ошибка
#         mist_count+=1
#         continue
#     else:                  # если заглавных одна
#          if c.lower() in d.keys():    # если слово есть в словаре
#              if c in d.get(c.lower()):     # и ударение в нем правильное
#                  continue
#              else:
#                  mist_count+=1
# print(mist_count)

d={}
for i in range(int(input())):
    s=input()
    d[s.lower()]=d.get(s.lower(),[])+[s]
ss=input().split()
mist_count=0
for c in ss:
    if c.lower() in d.keys() and c not in d.get(c.lower()) or len([cc for cc in c if cc.isupper()])!=1:
        mist_count+=1
print(mist_count)