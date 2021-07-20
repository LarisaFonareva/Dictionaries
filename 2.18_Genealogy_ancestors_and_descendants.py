def func(child, parent):
    if child==parent:   # если дошла до первого предка
        return True
    while child in d:
        child=d[child]      # ребенком делаю родителя, ищу его родителя
        if child==parent:     # если дошла до первого предка
            return True
    return False
d={}
for _ in range(int(input())-1):
    child, parent=input().split()
    d[child]=parent
print(d)
for _ in range(int(input())):
    person1, person2 = input().split()
    if func(person1,person2):
        print(2, end=' ')
    elif func(person2,person1):
        print(1,end=' ')
    else:
        print(0,end=' ')

# def func(c, p):
#     while c in d:
#         c = d[c]
#         if c==p:
#             return True
#     return False
# d = {}
# for _ in range(int(input()) - 1):
#     child, parent = input().split()
#     d[child] = d.get(child, '') + parent
# # for c in d:
# #     print(c,'   ', d[c])
# for _ in range(int(input())):
#     x1, x2 = input().split()
#     if func(x1, x2):
#         print(2, end=' ')
#     elif func(x2, x1):
#         print(1, end=' ')
#     else:
#         print(0, end=' ')