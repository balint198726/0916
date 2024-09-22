def masodik():
    # 2.	MegelőzőKövetkezőSzám: A program kérjen be a konzolról egy egész számot! Ha a szám egyjegyű, akkor a program írja ki a konzolra a számot megelőző és követő egész számot, egyébként ne írjon ki semmit
    szam1 = int(input("Kérem adjon meg egy egész számot "))
    if 10 > szam1 > -10:
        megelezo = szam1 - 1
        rakovetkezo = szam1 + 1
        print("A(z) " + str(szam1) + " megelőző és rákövetkező egész értékei " + str(megelezo) + ", " + str(
            rakovetkezo) + ".")
