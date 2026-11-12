# 1 misol...

# sonlar = [4, 2, 7, 4, 9, 2, 4, 1, 7]
# hisob = {}

# for son in sonlar:
#     if son in hisob:
#         hisob[son] += 1
#     else:
#         hisob[son] = 1


# a = None
# takror = 0

# for son, miqdor in hisob.items():
#     if miqdor > takror:
#         takror = miqdor
#         a = son

# print(f"Eng ko'p uchragan son: {a} (jami {takror} marta)")


# 2 masala...

# def janr(cinema:list, genre:str)->list:
#     filmlar=[]
    
#     for i in cinema:
#        if  i.get("genre","").lower() ==genre.lower():
#            filmlar.append(cinema)
#     return filmlar


# kino = [
#     {"title": "Avatar", "genre": "Fantastika", "price": 40000},
#     {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
#     {"title": "Oq yo'l", "genre": "Drama", "price": 25000},
#     {"title": "Dune", "genre": "Fantastika", "price": 35000}
# ]

# print(janr(kino, "Drama"))

# 3 masala 


# def merge_unique_ids(active_users: list, new_users: list) -> list:
#     unique = []
    
#     for id in active_users + new_users:
#         if id not in unique:
#             unique.append(id)
            
#     return unique


# active_users = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001'] 
# new_users = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']
# print(merge_unique_ids(active_users, new_users))
    
    
    
    
    

