#függvény meghívása
import beolvas

#rögzítés változóba
szam1 = beolvas.egeszSzamBeolvas()
szam2 = beolvas.egeszSzamBeolvas()
szam3 = beolvas.egeszSzamBeolvas()

#középső szám megtalálása
szamok = [szam1, szam2, szam3]
szamok.sort()
kozepsoszam = szamok[1]

#eredemény kiíratása
print("A középső szám: "+str(int(kozepsoszam)))