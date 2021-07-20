# d = dict(input().split() for _ in range(int(input()) - 1))
# # print(d)
# for _ in range(int(input())):
#     a,b=input().split()
#     l_a,l_b=[a],[b]
#     while a in d:
#         a=d[a]
#         l_a.append(a)
#     # print(1,l_a)
#     while b in d:
#         b = d[b]
#         l_b.append(b)
#     # print(2, l_b)
#     for c in l_a:
#         if c in l_b:
#             print(c)
#             break

h = dict(input().split() for _ in range(int(input()) - 1))
for _ in range(int(input())):
    e = []
    a, b = input().split()
    while a in h and a not in e:
        e.append(a)
        a = h[a]
    while b in h and b not in e:
        e.append(b)
        b = h[b]
    print(b)