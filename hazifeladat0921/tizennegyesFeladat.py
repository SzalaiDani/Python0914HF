#függvény meghívása
import beolvas

#rögzítés változóba
szam1 = beolvas.egeszSzamBeolvas()
szam2 = beolvas.egeszSzamBeolvas()

#eredemény tárolása
eredmeny = (szam1 + szam2) / 2

#eredemény kiíratása
print("Az eredemény: "+str(int(eredmeny)))