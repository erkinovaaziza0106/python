# lst = [1, 2, 33, 5, 6, 7, 7]
# n =int(input("son kiriting: "))
# sum=0

# for i in range(len(lst)):
#     for x in range(i+1,len(lst)):
#         if lst[i] + lst[x] == n:
#                 print(f"{i}, {x}")





# lst = [1, 4, 6, 8]
# new=[]

# for i in lst:
#     new.append(i*2)
# print(new)
    
    
    
# lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# result = [i[:-1] + (100,) for i in lst]
# print(result)       
    
    

# lst = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d',)]
# result = [i for i in lst if i]

# print(result)



# lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# result=sorted(lst, key=lambda x: x[1], reverse=True)
# print(result)


# lst = "python 3.0"
# result= tuple(lst)
# print(result)



# lst = [1, 2, 3, 4]
# prefix = "emp"
# result=[f"{prefix}{item}" for item in lst]
# print(result)



# gap = "salom aziz qalaysan"
# result= sorted(gap.split(),key=len)
# print(result)


# lst = [12, 'salom', 4.5, 'dunyo', True]
# new = [i for i in lst if isinstance(i, str)]


# result = sorted(new)

# print(result)



# t = (-3, 5, 0, 9, -1, 4)
# musbat=[i for i in t if i>0]
# print(musbat)



# lst = ['salom', 23, 'dunyo', 5, 100, 'python']
# new = sorted([i for i in lst if isinstance(i, str)])
# raqam= sorted([i for i in lst if isinstance(i,int) ], reverse=True)
# print(f"raqam: {raqam}")
# print(f"string : {new}")



# lst = [(3, 10), (1, 20), (2, 30)]
# new=sorted(lst, key=lambda x: x[0])
# print(new)



# lst = [1, 2, 3, 4]
# new=[]

# for i in lst:
#     new.append(i**2)
# print(new)



# lst = ['salom', 'dunyo', 'python']

# result = [i.capitalize() for i in lst]

# print(result)


# t = (1, 2, 3, 4, 5)
# result=sum([i for i in t ])
# print(result)



