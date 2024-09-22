def hatodik():

#A program  kérjen be a konzolról egy valós számot! Ha ez a szám 0 és 360 közé esik, akkor legyen egy szög mértéke (pl. 60 fok), egyébként a program adjon hibaüzenetet! Ha lehet, a program írja ki a szög mértéke alapján a szög típusát (pl.: 60 -> hegyesszög)!
    szam = float(input("Kérem adjon meg egy fok értékét!"))
    if (szam>=0) and (szam<=360):
        if szam == 0:
            print(szam,"fok azaz nullszög")
        elif (szam>0) and (szam<90):
            print(szam,"fok azaz hegyesszög")
        elif szam==90:
            print(szam,"fok azaz derékszög")
        elif  (szam>90) and (szam<180):
            print(szam,"fok azaz tompaszög")
        elif  szam==180:
            print(szam,"fok azaz egyenesszög")
        elif  (szam>180) and (szam<360):
            print(szam,"fok azaz homorúszög")
        else:
            print(szam,"fok azaz teljesszög")
    else:
        print("Nem konvertálható szöggé")
