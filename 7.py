# def 
#     ko'p qatorli 
#     Ko'p martali 
#     nomi bor 
#     return ishlatsa bo'ladi 
#     ()

# lambda 
#     bir qatorli 
#     bir martali 
#     nomi yo'q 
#     return ishlatilmiydi 
#     ()()


# natija = (lambda: 5+5)()
# natija = (lambda a,b: a*b)("salom",5)
# natija = (lambda x: [soz for soz in x if soz==soz[::-1]])(["salom", "dunyo", 'kiyik'])
# (lambda x: print("JUFT") if x%2==0 else print("TOQ"))(5)
# print(natija)


# natija = list(filter(lambda x: x%2==0, [1,12,34,9,0,3,2]))
# natija = list(filter(lambda x: x, [0,1,12,34,9,0,3,2]))
# natija = list(filter(lambda x: x in "aueio", "salom bolalar"))
# natija = list(filter(lambda x: x>7, [78, 5, 14, 0, 23, 3]))
# print(natija)


# natija = list(map(lambda x: x*2, [2,3,4,1]))
# natija = list(map(lambda x: int(x), input().split()))
# natija = list(map(lambda x: x%2==0, [2,1,3,4,5]))
# natija = "".join(list(map(lambda x: x.lower(), "assaLOM")))
# print(natija)





# natija=list(map(lambda x:(x*0.12)+x,[10000, 25000, 5000]))
# print("yakuniy narx: ",natija)


# natija=list(map(lambda x: x.split()[1],["Ali, ali@gmail.com", "Vali, vali123@mail.ru", "Aziza, aziza@outlook.com"]))
# print(natija)


# natija=list(map(lambda x:x[0],(list(filter(lambda x: x[1],[("Burger", False), ("Salad", True), ("Soup", True), ("Steak", False)])))))
# print(natija)


# natija=list(filter(lambda x: x>=60 , [55, 60, 75, 90, 45]))
# print(natija)


# natija=list(filter(lambda x:"+998" in x ,["+998901234567", "+375291234567", "+998991112233", "0901234567"] ))
# print(natija)

# natija=list(map(lambda x: round(x/30, 2) ,[120, 350, 210, 500, 90]))
# print(natija)


# natija=list(map(lambda x: str(x)[:-3] + "." + str(x)[-3:]+"so'm", [15000, 23000, 5000, 125000]))
# print(natija)


# natija=list(map(lambda x: x[0],(list(filter(lambda x: "IT" in x , [("Ali", "IT"), ("Vali", "HR"), ("Aziza", "IT"), ("Nodir", "Finance")])))))
# print(natija)



from lib import *

sana = "30.02.2025"
toliq_sana(sana)


