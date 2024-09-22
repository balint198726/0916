def tizenot():
   # A program olvasson be a konzolról két valós számot! Ha mindkét szám pozitív, akkor legyenek a beolvasott számok egy téglalap oldalai. A program számítsa ki a téglalap kerületét, területét, és írja ki két tizedesre kerekítve az eredményeket a konzolra! Hiba esetén írja ki: "Hiba: a téglalap oldalai nem pozitívak!"!

   szam1 = float(input("Kérem adja meg az a oldal értékét!"))
   szam2 = float(input("Kérem adja meg a b oldal értékét!"))

   if (szam1 >= 0) and (szam2 >= 0):
       kerulet = (szam1+szam2)*2
       terulet = (szam1*szam2)
       print("A téglalap kerülete ",kerulet,"\nA téglalap területe ",terulet)
   else:
       print("Hiba: a téglalap oldalai nem pozitívak!")



