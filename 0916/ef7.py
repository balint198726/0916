import math

def hetedik():
        #A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni
        szam = float(input("Kérem adjon meg egy értékét!"))
        if szam<0:
            print("Negatív számból nem lehet gyököt vonni")
        else:
            negyzetgyok = math.sqrt(szam)
            print(negyzetgyok)
