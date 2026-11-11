# lst = []

# for i in range(int(input("Nechta son: "))):
#     son = int(input(">>> "))
#     lst.append(son)

# for son in lst:
#     if son % 2 == 0:
#         print(son)

# ---------------------------------

# lst = ["Salom", "exam", "chopilasan", "uxlasen", "Baraka", "TOPGUR!"]
# new = []
# for soz in lst:
#     if soz[0].isupper():
#         new.append(soz)
# print(new)

# ---------------------------------

# lst = ["salom", 45, "kiyiK", 12, True, "Olma", "amma", 11, True, 45]
# bool_t = []
# str_t = []
# int_t = []
# for i in lst:
#     if type(i) == str and i not in str_t:
#         str_t.append(i)
#     elif type(i) == int and i not in int_t:
#         int_t.append(i)
#     elif type(i) == bool and i not in bool_t:
#         bool_t.append(i)
# print(bool_t)
# print(int_t)
# print(str_t)


# lst = ["salom", "Maktab"]
# lst.insert(1, "malina")
# print(lst)


# lst = ["salom", "Maktab"]
# lst.extend("abc")
# lst.extend([12,34,10])
# lst.append([12,34,"salom"])
# print(lst)

# ------------------------------

# lst = [23, 12, 10, 23, 9, 7, 6, 23]
# lst.clear()

# for i in range(lst.count(23)):
#     lst.remove(23)
# print(lst)

# for son in lst.copy():
#     if son % 2:
#         lst.remove(son)
# print(lst)


# lst = ["kiyik", "olma", "poliz"]

# for index, soz in enumerate(lst):
#     if soz == soz[::-1]:
#         lst[index] = "polindrom soz bor edi"

# print(lst)

# -------------------------

# lst = [23, 12, 43, 23, True]
# lst.sort()
# lst.sort(reverse=True)

# lst = ["abb", "aaa", "abc", "z", "az"]
# lst.sort()
# print(lst)

# -------------------------

# lst = [23, 12, 4, 64, 7]
# max(lst) # 64
# min(lst) # 4
# sum(lst) # 110


# lst = [[1,5,4], [2,4], [1,1,1]]
# new = []

# for royxat in lst:
#     new.append(sum(royxat))

# print(new)


# lst=[True, "salom", 5, 5.6]

# bool_t = []
# str_t = []
# int_t = []
# float_t=[]
# for i in lst:
#     if type(i) == str:
#         str_t.append(i)
#     elif type(i) == int:
#         int_t.append(i)
#     elif type(i) == bool: 
#         bool_t.append(i)
#     elif type(i)== float:
#         float_t.append(i)
# print(bool_t)
# print(int_t)
# print(str_t)
# print(float_t)


# lst=[1, 23,12,23,9,8,64,57,10]
# new=[]

# for i,son in enumerate(lst):
#     if i % 2==0:
#      lst[i]=son**2
#     else:
#       lst[i]=son**3 
      
# print(lst)
    

# lst=[1,2,0,0,0,3,4,12,34,67,0,0,12,0,56,1,0,9,87,6,5,0,0,0]
# new=[]
# for son in lst.copy():
#     if son==0:
#         lst.remove(0)
#         lst.append(0)
   
# print(lst)


# lst=[2,1,-4,9,0,3,5,8]
# natija=sorted(set(lst))
    
# print(natija[-2])



# lst = [1,4,3,2,1,1,1,2,5,6,3]

# natija = set(lst)
# print(natija)


# 6
# lst = [12,45,6]
# natija = ""
# for son in lst:
#     natija += str(son)
# print(int(natija))


# 7
# a = [12, 4, 3, 2, 1, 10]
# b = [5, 3, 2, 1, 2, 4]
# c = a + b
# print(sum(c) / len(c))


# lst=["ada", 212 , False , 4567 , "aziza"]

# for index, soz in enumerate(lst):
#     if soz == soz[::-1]:
#         print(f"{soz} POLINDROM")
#     else :
#         print(f"{soz} POLINDROM EMAS")

# print(lst)
       
       
       
      