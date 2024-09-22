def fhuszonkettedik():
    # A program oldja meg az a*x+b=0 alakú egyenletet! Kérje be a konzolról az a és b valós típusú változókat! Ha az a értéke nem nulla, akkor a program számítsa ki és írja ki a megoldást (x=-b/a) a konzolra, egyébként írjon ki hibaüzenetet!
    a = float(input("Kérem adjon meg a értékét!"))
    b = float(input("Kérem adjon meg még b értékét!"))
    if a != 0:
        x = (-1 * b) / a
        print(x)
    else:
        print("HIBA: nem megoldható elsőfokű egyenlet!")
