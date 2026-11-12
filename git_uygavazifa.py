# 1 misol...

sonlar = [4, 2, 7, 4, 9, 2, 4, 1, 7]
hisob = {}

for son in sonlar:
    if son in hisob:
        hisob[son] += 1
    else:
        hisob[son] = 1


a = None
takror = 0

for son, miqdor in hisob.items():
    if miqdor > takror:
        takror = miqdor
        a = son

print(f"Eng ko'p uchragan son: {a} (jami {takror} marta)")


# 