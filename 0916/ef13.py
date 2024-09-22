def tizenharom():

    # A program olvassa be a konzolról egy kör sugarát! Ha a sugár nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kör sugara nem pozitív!"; egyébként a program számítsa ki és írja ki a kör kerületét, területét a konzolra!

    sugar = float(input("Kérem adjon meg egy sugar értékét!"))
    kerulet = 2*sugar*3.14159
    terulet = sugar**2*3.14159

    if sugar >= 0:
        print("Kör kerülete: ",kerulet,"\nKör területe: ",terulet)
    else:
        print("Hiba: a kör sugara nem pozitív!")



