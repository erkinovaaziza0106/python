# ptr=open("karta.txt")

# data=ptr.read().split("\n")
# dct={}
# for shahar in data:
#     bolak=shahar.split(",")
#     qator=bolak[-1]
#     if qator not in dct:
#         dct[qator]=1
#     else:
#         dct[qator]+=1 
# print(dct)


# data=ptr.read().split("\n")
# st=set()
# for i in data:
#     bolak=i.split(",")
#     if  "visa" in bolak[1]:
#      st.add(f"{bolak[-1]}")
# print(st)



# data=ptr.read().split("\n")
# for i in data:
#     bolak=i.split(",")
#     if len(set(bolak[0]))==10:
#      print(f"{bolak[0]} {bolak[2]}  {bolak[-1]} {bolak[-2]}")
        
# ptr.close()



# ptr=open("internet.txt")

# data=ptr.read().split()

# for i in data:
#     bolak=i.split(",")
#     qator=bolak[-2].split("-")
#     for x in qator:
#         if x.isdigit() :
#             break
#     else:
#         print( bolak[0], bolak[1] ,bolak[-2])

# ptr.close()


ptr=open("internet.txt")

data=ptr.read().split("\n")
dct={}
for i in data:
    bolak=i.split(",")
    email=bolak[0].split(".")
    if email not in bolak:
        dct[email]=email
    
            
        
    


ptr.close()

