"""
asagıda musterının bılgılerını ve satın aldıgı urun bılgılerını degıskenler ıcerısınde saklayınız 

Toplam odenen ucret nedir?
Odenen miktarin kdv orani nedir? (%18)

eren akcan
05354804534
akcaneren18@gmail.com
KONYA

Satin alinan urunler 

Urun adı : kablosuz mouse
Fiyati : 550 TL

Urun adı : kablosuz klavye
Fiyati : 650

Urun adı : diz ustu bilgisayar
Fiyati : 55.000

"""
urun1 = "kablosuz mouse"
urun2 = "kablosuz klavye"
urun3 = "diz_ustu bilgisayar"

urun1Fiyat = 550 
urun2Fiyat = 650
urun3Fiyat = 55000

print(urun1Fiyat + urun2Fiyat + urun3Fiyat)

urunlerToplami = 56200

kdvOrani = 0.18 # %18 kdv icin 

kdvTutari = urunlerToplami * kdvOrani

toplamFiyat = urunlerToplami + kdvTutari

print("KDV tutarı :",kdvTutari)
print("KDV dahil toplam :",toplamFiyat)

musteriAdi = "eren" 
musteriSoyadi = "akcan"
musteriTelefon = "05354804534"
musteriGmail = "akcaneren18@gmail.com"
musteriKonum = "KONYA"

print(musteriAdi)
print(musteriSoyadi)
print(musteriTelefon)
print(musteriGmail)
print(musteriKonum)


