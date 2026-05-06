"""
alınan lot sayısı = 45
hissenin adı = AAGYO 
bit lotun satıs fıyatı = 15.50
bıt lotun alıs fıyatı = 10.25
bır lotun gunecl fıyatı = 12.40

"""

hisse_adi = input("hissenin adi : ")
lot_sayisi = int(input("alinan lot sayisi : "))
alis_fiyati = float(input("bir lotun alis fiyati : "))
satis_fiyati = float(input("bir lotun satis fiyati : "))
guncel_fiyati = float(input("bir lotun suan ki güncel fiyati : "))

maliyet = lot_sayisi * alis_fiyati
suankiDeger = lot_sayisi * guncel_fiyati


print("maliyet = ",maliyet)
print("suankiDeger = ",suankiDeger)