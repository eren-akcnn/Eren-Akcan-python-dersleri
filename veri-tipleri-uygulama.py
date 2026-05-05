"""
uygulama 1 : yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız 

dairenin alanı : πr²
dairenin çevresi : 2πr

uygulama 2 : klavyeden girilen km bilgisini mil cinsinden giriniz

mil = km / 1.609344

"""

#uygulama 1 


pi = 3.14

r = float(input("Yarı Çap : "))

alan = pi * r ** 2
cevre = 2 * pi * r 

print(("Alan : ")+ str(alan))

print(("Cevre : ") + str(cevre)) 

# uygulama 2 

mesafeKm = input("km : ")
mesafeMil = float(mesafeKm) / 1.609344

print(mesafeKm + " km =  " + str(mesafeMil)  +  " mil ")