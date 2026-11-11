def toliq_sana(sana:str):
    kun = sana.split('.')[0]
    oy = sana.split('.')[1]
    yil = sana.split('.')[2]
    
    if oy == '01' and 1<=int(kun)<31:
        print(f"{kun} yanvar {yil} yil.")
    elif oy == '02' and 1<=int(kun)<28:
        print(f"{kun} fevral {yil} yil.")
    elif oy == '03' and 1<=int(kun)<31:
        print(f"{kun} mart {yil} yil.")
    elif oy == '04' and 1<=int(kun)<30:
        print(f"{kun} aprel {yil} yil.")
    elif oy == '05' and 1<=int(kun)<31:
        print(f"{kun} may {yil} yil.")
    elif oy == '06' and 1<=int(kun)<30:
        print(f"{kun} iyun {yil} yil.")
    elif oy == '07' and 1<=int(kun)<31:
        print(f"{kun} iyul {yil} yil.")
    elif oy == '08' and 1<=int(kun)<31:
        print(f"{kun} avgust {yil} yil.")
    elif oy == '09' and 1<=int(kun)<30:
        print(f"{kun} sentabr {yil} yil.")
    elif oy == '10' and 1<=int(kun)<31:
        print(f"{kun} oktabr {yil} yil.")
    elif oy == '11' and 1<=int(kun)<30:
        print(f"{kun} noyabr {yil} yil.")
    elif oy == '12' and 1<=int(kun)<31:
        print(f"{kun} dekabr {yil} yil.")
    else:
        print("Bu formatdagi sana yo'q.")

   
def user(data: list) -> str:
    scores = {}
    
    for id, score in data:
        scores[id] = scores.get(id, 0) + score
    
    
    top_user = None
    max_score = float()  
    
    for id, total_score in scores.items():
        if total_score > max_score:
            max_score = total_score
            top_user = id
            
    return top_user



def calculate_class_averages(scores: dict) -> dict: 
    result={}

    for id, score in scores.items():
        if not score:
            result[id] = 0
            continue
        
        ortacha=sum(score)/len(score)
        butun_qism = int(ortacha)
        kasr_qism = ortacha - butun_qism
    
        if round(kasr_qism, 4) <= 0.50:
            result[id] = butun_qism
        else:
            result[id] = butun_qism + 1
            
    return result
        


def max_movies_to_watch(movies:list[tuple[int,int]]):
    natija = []
    for index, movie in enumerate(movies):
        test = [movie]
        for kino in movies[index+1:]:
            if test[-1][1] <= kino[0]:
                test.append(kino)
        if len(test) > len(natija):
            natija = test.copy()
            
    return len(natija), natija


        
 

   
    