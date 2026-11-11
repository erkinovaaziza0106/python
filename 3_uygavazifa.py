# lst=[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

# count=0
# for i in lst:
#     if type(i)==int:
#         count+=1

# print(count)



# lst=[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

# max=0
# for i in lst:
#     if type(i)==int:
#         if max is None or i>max:
#             max=i 
            
# print(max)



# lst=['abc', 'xyz', "bo'lib", 'aba', '1221']
# count=0

# for i in lst:
#     if len(i)>=2 and i[0]==i[-1]:
#       count+=1
      
# print(count)  



# lst=[True, "Salom", 5, 5.6]
# bool_t = []
# str_t = []
# int_t = []
# float_t=[]
# for i in lst:
#     if type(i)==str:
#         str_t.append(i)
#     elif type(i) == int : 
#         int_t.append(i)
#     elif type(i) == bool:
#         bool_t.append(i)
#     elif type(i)==float :
#         float_t.append(i)
        
# print(bool_t)
# print(int_t)
# print(str_t)
# print(float_t)





# lst=[7, 8, 1, 3, 4, 6, 7, 5]

# juft_t=[]
# toq_t=[]

# for i in lst:
#     if i % 2==0:
#         juft_t.append(i**2)
#     else:
#         toq_t.append(i**3)

# print(juft_t)
# print(toq_t)




# lst=[2, 1, -4, -9, 0, -5, 8, 3]

# natija=sorted(set(lst))
    
# print(natija[-2])


# lst=[1, 1, 3, 4, 4, 5, 6, 7]
# lst1=[0, 1, 2, 3, 4, 4, 5, 7, 8]
# natija=lst+lst1

# print(sum(natija) // len(natija))
        


# lst=["ada", 212, False, 4567, "aziza"]

# for index, soz in enumerate(lst):
#     if soz == soz[::-1]:
#         print(f"{soz} POLINDROM")
#     else :
#         print(f"{soz} POLINDROM EMAS")

# print(lst)




# lst=['p', 'q'] 
# n = 5
# natija=[]
# for i in range(1,n+1):
#     for x in lst:
#         natija.append(f"{x}{i}")
        
# print(natija)



# lst=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 9, 10, 7, 3, 0, 0, 2, 9, 7, 1]
        
# new=[]
# for son in lst.copy():
#     if son==0:
#         lst.remove(0)
#         lst.append(0)
# print(lst)
    
    
    

# lst = [[2, 15, 4], [19, 24, 11], [7, 9, 5], [10, 3, 1]]

# for i in range(len(lst)):          
#     for j in range(len(lst[i])):   
#         if j % 2 != 0:
            
#             lst[i][j] = lst[i][j] ** 2


# print(lst)





# lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# lst[2][2].append(7000)

# print(lst)



# 10 misol 

# lst = [4,5,6,8,1,40]
# if lst == sorted(lst):
#     print("O'sish")
# elif lst == sorted(lst, reverse=True):
#     print("Kamayish")
# else:
#     print("Tartibsiz")




