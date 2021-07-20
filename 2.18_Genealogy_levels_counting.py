# def level(name):
#     if name not in d:
#         return 0        # если имени нет в детях - вернуть 0
#     return 1 + level(d[name])    # иначе: вернуть 1+функция от родителя имени
# d = {}
# S=set()
# for i in range(int(input()) - 1):
#     s = input().split()
#     d[s[0]] = s[1]       # ребенок - родитель
#     S.update(s)
# # print(d)
# # print(S)
# # for i in sorted(set(d.keys()) | set(d.values())):
# for name in sorted(S):
#     print(name, level(name))

# d, s = {}, set()
# for _ in range(int(input())-1):
#     child, parent = input().split()
#     d[child] = d.get(child, '') + parent
#     s.add(parent)
#     s.add(child)
# # print(d)
# for c in sorted(list(s)):
#     count=0
#     child=c
#     while child in d.keys():
#         child=d[child]
#         count+=1
#     print(c, count)

d = {}
for _ in range(int(input()) - 1):
    child, parent = input().split()
    d.setdefault(parent, '')
    d[child] = parent
print(d)
for child in sorted(d):
    parent = d[child]
    level = 0
    while parent:
        level += 1
        parent = d[parent]
    print(child, level)