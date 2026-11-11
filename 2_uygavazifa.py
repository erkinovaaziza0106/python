# n=int(input())

# i=1
# sum=0
# while i<=n:
#     print(f"{i*i}")
#     sum+=i
#     i+=1 

#  print(sum)

# import random 

# a=random.randint(1,200)


# while a<=200:
#     b=int(input("yoshingizni kiriting"))
#     if(a==b):
#         print("Bu sizning yoshingiz!")




# for i in range(100, 1000):
#     y = i // 100
#     o = i //10%10
#     b = i % 10
#     if (y == o and y != b) or (o == b and o != y) or (y == b and y != o):
#         print(i, end=" ")
# print()


# import random 

# n=int(input())
# a=random.randint(1,n)
# for i in range(1,4):
#     b=int(input("son kiriting: "))
#     if b==a:
#         print("WINNER")
#         break
#     else:
#         print("LOOSER")

# a=int(input("yoshingiz: "))
# b=int(input("necha yil obuna boldingiz: "))

# print("asosiy reja oyligi $15")
# sum=0
# if a>50 :
#     print("20 % li chegirma")
#     sum=15**0.80
# if b>3:
#     print("3 yildan ortiq obuna bolganga 10 % li chegirma")
#     sum=15**0.9
# if b>5:
#     print("5 yildan ortiq obuna bo'lsa, 15 %  chegirma beriladi.")
#     sum=15**0.85

# print("{sum} yakuniy narx")


   
#    while True:    
#     C = input("C: ")

#     if C == "exit":
#         exit()

#     F = float(C) * (9/5) + 32

#     if F <= 32:
#         print("Muzlash")
#     elif F>=85:
#         print("Issiq kun")
#     else:
#         print("Yaxshi kun")
 
    
    
   # while True: 
#     parol = input(">>> ")
#     raqam, k_harf, belgi = False, False, False
#     for i in parol:
#         if i.isupper():
#             k_harf = True
#         elif i.isdigit():
#             raqam = True
#         elif i in "@#$":
#             belgi = True
#     if raqam and k_harf and belgi and len(parol) >= 8:
#         print("Parol kuchli")
#         break

#     if len(parol) < 8:
#         print("Parol uzunligi kamida 8ta elementdan tashkil topishi kerak")

#     if not raqam:
#         print("Parolda 1ta raqam ishtirok etishi kerak")

#     if not belgi:
#         print("Parolda @#$ lardan kamida bitta ishtirok etishi kerak")

#     if not k_harf:
#         print("Prolda kamida bitta katta harf bo'lishi kerak")
     
     
     
     
# for i in range(3):
#     name = input("Aktsiya nomi: ")
#     narx = int(input("Aktsiya narxi: "))
#     if narx > 100:
#         print("Qimmat aktsiya")
#     elif narx < 50:
#         print("Arzon aktsiya")
#     else:
#         print("Aktsiya o'rtacha")

