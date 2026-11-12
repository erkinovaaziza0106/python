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