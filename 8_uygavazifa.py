with open("moshina.txt") as ptr:
brendlar_royxati = []
brend_davlatlari = {}

with open(fayl_nomi, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for qator in reader:
        brand = qator["brand"]
        country = qator["country"]
        
        brendlar_royxati.append(brand)
        
        # Har bir brend qaysi davlatlarda borligini saqlab boramiz
        if brand not in brend_davlatlari:
            brend_davlatlari[brand] = []
        brend_davlatlari[brand].append(country)

# 2. Eng ko'p uchragan brendni aniqlaymiz
brend_soni = Counter(brendlar_royxati)
eng_kop_brend, jami_soni = brend_soni.most_common(1)[0]

# 3. Shu brendning davlatlar bo'yicha taqsimotini hisoblaymiz
davlat_soni = Counter(brend_davlatlari[eng_kop_brend])

# Eng ko'p va eng kam uchragan davlatlarni topamiz
eng_kop_davlat, max_son = davlat_soni.most_common(1)[0]
eng_kam_davlat, min_son = davlat_soni.most_common()[-1]

# 4. Natijalarni ekranga chiqaramiz
print(f"1. Eng ko'p mashinaga ega brend: {eng_kop_brend} (jami {jami_soni} ta)")
print(f"2. Ushbu brend eng ko'p bo'lgan davlat: {eng_kop_davlat} ({max_son} ta)")
print(f"3. Ushbu brend eng kam bo'lgan davlat: {eng_kam_davlat} ({min_son} ta)")