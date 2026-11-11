# def price(son: int, mahsulotlar: list) -> list:
#     mahsulot = sorted(mahsulotlar, key=lambda x: x['price'], reverse=True)
#     return mahsulot[:son]
# 
# son = int(input("Nechta  mahsulot: "))
# numbers = int(input("Jami: "))
# royxat = []
# 
# for i in range(numbers):
#         print(f"\n{i+1}-mahsulot ma'lumotlari:")
#         nomi = input("Nomi: ")
#         narxi = float(input("Narxi: "))
#         royxat.append({"name": nomi, "price": narxi})
        
# def mahsulot (a:int, b:int):
#     count=0
#     while a/2>b:
#         count+=1
#         a=a/b
#     return count
        
# def CashMachine(user_harakat:list[str], user2_harakat:list[str]):
#     user, user2 = 3, 3
#     for i in range(len(user_harakat)):
#         if user_harakat[i] == "share":
#             user -= 1 
#             user2 += 3 

#         if user2_harakat[i] == "share":
#             user2 -= 1
#             user += 3
#     return user, user2       



# 1 misol...

# natija = price(son, royxat)
    
# print("\nNatija (Output):")
# print(natija)

# 2 misol...

# x=int(input())
# y=int(input())
# natija=mahsulot(x,y)
# print(natija)


# 3 misol....

# lst = input().split()
# lst2 = input().split()
# natija = CashMachine(lst, lst2)
# print(natija)



 
    
    
