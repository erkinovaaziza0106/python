# tpl = (12, "salom", 45)

# print(tpl[0])
# tpl[0] = 100

# for i in tpl:
#     print(i)

# tpl = list(tpl)
# tpl[0] = "Karam"
# tpl = tuple(tpl)
# print(tpl)

# -----------------------------

# lst = [(12, 45, 2), (2,3), (6,5,2)]
# for index, tpl in enumerate(lst):
#     tpl = list(tpl)
#     tpl.append(15)
#     tpl = tuple(tpl)
#     lst[index] = tpl
# print(lst)






# .....................



# lst=[(2,3,5,8,9,10,12),(1,2),(4,7,10),(2,5,7,9,10)]
# new=[]

# for  tpl in lst:
#     tpl=list(tpl)
#     tpl = tuple(tpl)
#     if len(tpl)>=5:
#      new.append(tpl)
     
# print(new)
    
    

# lst=[(1,3), (0,2,0),(1,1,1), (0,4), (1,9)]
# new=[]
# for i in lst:
#     i=list(i)
#     i=tuple(i)
#     new.append((sum(i)))
# print(new)


# lst=[(1,2),(2,3),(3,4)]
# new=[]

# for i in lst:
#     i=list(i)
#     i=tuple(i)
#     new.append(i)
# print(new)


# lst=["ada", 212, False, 4567, "aziza"]

# for index,i in enumerate(lst):
#     if str(i) == str(i)[::-1]:
#         print(f"{i}  polindrom")
#     else:
#         print(f"{i}  polindrom emas")
    
    
    
# lst=[(1,2,3), (2,2), (3,0,0)]
# lst.sort(lst, key=lambda x: sum([int(i) for i in x]))
# print(lst)



# lst = [(1,2), (3,4), (8,9)]
# t1 = []
# t2 = []
# for i in lst:
#     t1.append(i[0])
#     t2.append(i[1])
    
# print([tuple(t1), tuple(t2)])


# lst = [(0,2,0,0), (0,3,2,2), (1,3,2,4,3), (4,1,2,4)]
# new = []

# for i in lst:
#     temp = []
#     for x in i:
#         temp.append(i.count(x))
        
#     new.append(tuple(temp))
    
# print(new)

