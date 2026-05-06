# NOT HESAPLAMA UYGULAMASI

ders = input(str("Dersin Adı : "))
vize = float(input("Vize notu : "))
ödev = float(input("ödev notu : "))
final = float(input("Final Notu : "))

vize_notu = vize * 0.375
odev_notu = ödev * 0.125
final_notu = final * 0.50

toplam_ortalama = vize_notu + odev_notu + final_notu

print(toplam_ortalama)