import sys
d = {}
for i in sys.stdin:
    name, good, count = i.split()
    d[name][good] = d.setdefault(name, {}).setdefault(good, 0) + int(count)
for a in sorted(d):
    print(a + ':')
    for b in sorted(d[a].items()):
        print(*b)

# import sys
# d={}
# for c in sys.stdin:
#     name, good, count=input().split()
#     count=int(count)
#     if name not in d:
#         d[name]={good: count}
#     else:
#         if good not in d[name]:
#             d[name][good]=count
#         else:
#             d[name][good]+=count
#         print(d)
# print(d)
# for key in sorted(d):
#     print(key,':',sep='')
#     for k in sorted(d[key].items()):
#         print(*k)

# d={}
# while True:
#     s=input().split()
#     if s:
#         if s[0] not in d:
#             d[s[0]]={}
#             d[s[0]][s[1]]=[int(s[2])]
#         else:
#             if s[1] not in d[s[0]]:
#                 d[s[0]][s[1]]=[int(s[2])]
#             else:
#                 d[s[0]][s[1]]+=[int(s[2])]
#         print(d)
#     else:
#         break
# print(d)
# for key in sorted(d):
#     print(key,':',sep='')
#     for k in sorted(d[key]):
#         print(k, sum(d[key][k]))

# import sys
# sd = {}
#
# for i in sys.stdin:
#     k, t, v = i.split()
#     sd[k][t] = sd.setdefault(k, {}).setdefault(t, 0) + int(v)
#
# for a in sorted(sd):
#     print(a + ':')
#     for b in sorted(sd[a].items()):
#         print(*b)
