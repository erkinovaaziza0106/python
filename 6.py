def harf(a:str) -> dict:
    new = {}
    for i in a:
        new[i]=a.count(i)
    return new

def son(a:int, b:int) -> dict:
    return str(a)+str(b)
    
def matn(a):
    natija=""
    for i in a.split():
        natija+=i[-1]
        natija+=i[1:-1]
        natija+=i[0]
        natija+=" "
    return natija
      
def son(d1:dict,d2:dict):
    for i in d1:
        if i not in d2:
            d2[i]=d1[i]
        else:
            d2[i]+=d1[i]
    return d2


 
        
         
         
         
         
    
    




# natija=harf(input("matn kiriting  "))
# print(natija)



# natija=son(9,6123)
# print(natija)



# natija=matn(input("matn kiriting:  "))
# print(natija)



# d1={"a":100,"b":200,"c":300}
# d2={"a":300,"b":200,"d":400}
# print(son(d1,d2))




