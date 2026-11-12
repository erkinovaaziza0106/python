# 1 misol

import json 

# with open("orders.json") as ptr:
#     data = json.load(ptr)
#     new = []
#     for zakaz in data:
#         sum = 0
#         for mahsulot in zakaz['items']:
#             sum += mahsulot['price'] * mahsulot['quantity']
#         new.append(f"{zakaz['customer_name']} -> ${sum}")
#     print(max(new, key=lambda x: int(x.split("$")[1])))


# 2 misol..

# with open("menu.json") as ptr:
#     data = json.load(ptr)
#     for i in data:
#         if i["category"]=="Pizza":
#             print(f"{i["name"]} {i["category"]}")
       
# print(min(data, key=lambda x: x["price"]))
# print(max(data, key=lambda x: x["price"]))
        


# 3 misol...
# with open("tickets.json") as ptr:
#     data = json.load(ptr)
    
#     for i in data:
#         sum=0
#         sum+=i["seats"]
#         if i["from"]=="Tashkent":
#             print(f"{i["flight"]} {i["from"]}")
            
# print(sum)
# print(f"eng arzon:  {min(data, key=lambda x: x["price"])}")
# print(f"eng qimmat: {max(data, key=lambda x: x["price"])}") 


# 4 misol... 

# with open("weather.json") as ptr:
#     data = json.load(ptr)
#     print(max(data, key=lambda x: x['temperature']))
#     print(min(data, key=lambda x: x['temperature']))
#     print(sum([city['temperature'] for city in data])/len(data))


# 5 misol...

 

# with open("students.json") as ptr:
#     data = json.load(ptr)
#     dct = {}
#     for inson in data:
#          if "Python" in inson['courses']:
#              print(f"{inson['name']} {inson['age']}")
#         for fan in inson['courses']:
#             if fan not in dct:
#                 dct[fan] = 1 
#             else:
#                 dct[fan] += 1
#     print(dct)
