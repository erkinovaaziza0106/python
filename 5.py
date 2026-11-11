# grades = {
#     "Ali": 85,
#     "Vali": 78,
#     "Hasan": 90
# }
# a=input("ism kiriting")
# b=int(input("bal kiriting: "))
# if a in grades:
#     grades[key]=b
# else:
#     print("bunday talaba yoq")
        
# print(grades)    


# 2 m

# store = {
#     "olma": 5000,
#     "banan": 7000
# }

# a=input("mahsulot nomi  ")
# b=int(input("narx: "))


# if a in store:
#     print("bunday mahsulot mavjud")
# else:
#     store[a]=b
# print(store)


# 3.m

# employees = {
#     "101": "Ali",
#     "102": "Bobur",
#     "103": "Madina"
# }

# a=input("ID kiriting:  ")
 
# if a in employees.copy():
#     employees.pop(a)
#     print("ochirilib tshlandi")
# else:
#     print("bunday xodim yoq")
# print(employees)
    
    
    # 4.m


# prices = {
#     "Laptop": 700,
#     "Phone": 350,
#     "Camera": 500
# }


# print(max(prices, key=prices.get))
# print(max(prices.items(),key=lambda x:x[1]))


# 5 m

# cart = {
#     "olma": 3,
#     "banan": 5,
#     "uzum": 2
# }

# print(f"Jami mahsulotlar soni: {sum(cart.values())}")


# 6 m

# student = {
#     "name": "Aziz",
#     "age": 20,
#     "contact": {
#         "phone": "+998971234567",
#         "email": "aziz@mail.com"
#     }
# }

# print("tel raqami", student["contact"]["phone"])


# 7 m

# d1 = {"olma": 5000, "banan": 7000}
# d2 = {"shaftoli": 8000, "olcha": 10000}

# result=d1|d2
# print(result)


# 8 m

# orders = [
#     {"customer": "Ali", "amount": 15000},
#     {"customer": "Vali", "amount": 22000},
#     {"customer": "Ali", "amount": 8000}
# ]
# new={}

# for dct in orders:
#     if dct["customer"] not in new:
#         new[dct["customer"]]=dct["amount"]
#     else:
#         new[dct["customer"]]+=dct["amount"]
# print(new)
        
    

# 9 m

# n=input("matn kiriting:   ")
# dct={}

# for i in n.split():
#     if i not in dct:
#         dct[i]=1
#     else:
#         dct[i]+=1
# print(dct)



        
# 10m...

# products = {
#     "Laptop": 700,
#     "Mouse": 25,
#     "Phone": 350,
#     "Camera": 500,
#     "Keyboard": 45
# }


