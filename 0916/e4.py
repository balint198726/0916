def negy():
    # 4. Osztályzat2: A program beolvas a konzolról egy egész számot!
    # Ha a szám 1 és 5 közötti, akkor legyen a beolvasott szám egy osztályzat!
    # A program írja ki a konzolra a számmal megadott osztályzatot szövegesen (1=elégtelen, …, 5=jeles)!
    # Ha a szám nem 1 és 5 közötti, akkor a program írja ki konzolra, hogy „érvénytelen osztályzat”!
    szam = int(input("Kérem adjon meg egész számot!"))
    if (szam >= 1) and (szam <= 5):
        if szam == 1:
            print("elégtelen")
        elif szam == 2:
            print("elégséges")
        elif szam == 3:
            print("közepes")
        elif szam == 4:
            print("jó")
        else:
            print("jeles")
    else:
        print("Érvénytelen osztályzat.")
