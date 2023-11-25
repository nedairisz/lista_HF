# 1. Nézzük meg a lottószámok átlagát
def feladat1(lottoszamok):
    gyujto:int = 0
    atlag:int =0
    db: int=0
    i:int =0
    while i<len(lottoszamok):
        gyujto+=lottoszamok[i]
        db+=1
        i+=1
    atlag=gyujto/db
    return atlag

# Hány 50-nél nagyobb szám van közte?
def feladat2(lottoszamok):
    i:int =0
    db:int =0
    while i<len(lottoszamok):
        if lottoszamok[i]<50:
            db+=1
        i+=1
    return db

# Melyik a legnagyobb szám? 
def feladat3(lottoszamok):
    max = lottoszamok[0]
    i=0
    while i<len(lottoszamok):
        if max<lottoszamok[i]:
            max=lottoszamok[i]
        i+=1
    return max

# Hányadiknak generáltuk a a legnagyobb számot?
def feladat4(lottoszamok):
    max = lottoszamok[0]
    hanyadik:int=0
    i=0
    while i<len(lottoszamok):
        if max<lottoszamok[i]:
            max=lottoszamok[i]
        i+=1
        hanyadik = lottoszamok.index(max)+1
    print(f"{hanyadik}. helyen áll {max} a listában.")

# Melyik a legkisebb szám? 
def feladat5(lottoszamok):
    min = lottoszamok[0]
    i=0
    while i<len(lottoszamok):
        if min>lottoszamok[i]:
            min=lottoszamok[i]
        i+=1
    return min

# A legkisebb és a legnagyobb szám közti különbség? 
def feladat6(lottoszamok):
    kulonbseg = feladat3(lottoszamok)-feladat5(lottoszamok)
    return kulonbseg

# Kérj be a felhasználótól egy számot, és döntsd el, hogy szerepel -e a szám a húzott számok között? 
def feladat7(lottoszamok):
    szam:int= int(input("Adj meg egy számot!: "))
    i:int =0
    szerepel:int=0
    while i<len(lottoszamok):
        if lottoszamok[i] == szam:
            szerepel = 1
            break
        i += 1

    if szerepel:
        print(f"{szam} szerepel a listában!")
    else:
        print(f"{szam} nem szerepel a listában!")

# Kérj be a felhasználótól 5 számot, és döntsd el, hogy van-e találata? 
# Kérj be a felhasználótól 5 számot, és a program mondja meg, hány találata van az illetőnek? 
def feladat8(lottoszamok):
    i:int =0
    talalatok = 0
    while i<5:
        megadott_szam= int(input("Adj meg egy számot: "))
        if megadott_szam in lottoszamok:
            print("Talált!")
            talalatok+=1
        else:
            print("Nem talált")
        i+=1
    return talalatok

# A húzott véletlen számok ne lehessenek azonosak!
# A felhasználótól addig kérd be a számokat, amíg 5 különbözőt ad meg!
def feladat9():
    i = 0
    gyujto = set()
    while i < 5:
        megadott_szam = int(input("Adj meg egy számot: "))
        if megadott_szam in gyujto:
            print("Már volt ez a szám. Adj meg egy új számot!")
        else:
            gyujto.add(megadott_szam)
            i += 1