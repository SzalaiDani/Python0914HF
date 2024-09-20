#függvény meghívása
import beolvas

#rögzítés változóba
szam1 = beolvas.egeszSzamBeolvas()
szam2 = beolvas.egeszSzamBeolvas()

#számítás
eredmeny = szam1 % szam2

#eredemény kiíratása
print("Osztási maradék: "+str(int(eredmeny)))