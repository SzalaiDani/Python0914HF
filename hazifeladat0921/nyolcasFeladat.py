#függvény meghívása
import beolvas

#rögzítés változóba
szam1 = beolvas.egeszSzamBeolvas()
szam2 = beolvas.egeszSzamBeolvas()

#eredemény tárolása
eredmeny = szam1 * szam2

#eredemény kiíratása
print("A két szám szorzata: "+str(int(eredmeny)))

