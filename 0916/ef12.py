def ftizenkettedik():
    #12. feladat – KisebbNagyobbEgyenlőReláció. A program két beolvasott számot összehasonlítva írja közéjük a megfelelő relációs jelet (<, >, =)!
    szam1 = float(input("Kérem adjon meg egész számot!"))
    szam2 = float(input("Kérem adjon meg még egy egész számot!"))
    if szam1 == szam2:
        print(str(szam1)+"="+str(szam2))
    elif szam1 < szam2:
        print(str(szam1) + "<" + str(szam2))
    else:
        print(str(szam1) + ">" + str(szam2))

