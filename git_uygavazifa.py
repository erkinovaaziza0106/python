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
    

# 4 masala...

# def sorted_by_price(products: list) -> list:
#     for i in products:
#         return sorted(i)

    
    
    
# products = [
#     ('Olma', '12000', '50'),
#     ('Banan', '8000', '100'),
#     ('Gilos', '15000', '70'),
#     ('Apelsin', '9000', '80'),
#     ('Anor', '30000', '20'),
#     ('Uzum', '20000', '40'),
#     ('Tarvuz', '25000', '15'),
#     ('Shaftoli', '18000', '60'),
#     ('Qovun', '40000', '25'),
#     ('Qulupnay', '35000', '10')
# ]

# print(sorted_by_price(products))



# 5 misol...

# def are_numbers_ascending(text: str) -> bool:
#     sozlar = text.split()
#     son = -1
    
#     for soz in sozlar:
#         if soz.isdigit():
#             hozirgi_son = int(soz)
            
#             if hozirgi_son <= son:
#                 return False
                
#             son = hozirgi_son
            
#     return True



# print(are_numbers_ascending("1 qutida 5 ta yashil, 9 ta qizil, 12 ta sariq to’p bor edi"))