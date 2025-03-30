import math as m
i = int(input("Masukkan Angka: "))

if (i == 5):
    print("ini angka 5")
elif (i > 5):
    print("angka ini lebih dari 5")
else:
    print("angka ini kurang dari 5")

# perulangan while
print("perulangan while")
# nilai awal j = 0
j = 0
# ketika j kurang dari 6 lakukan perulangan, jika tidak stop perulangan
while j < 6:
    # lakukan perintah ini keetika perulangan
    print("Ini adalah perulangan ke -", j)
    # setiap kali diakhir perulangan update nilai dengan ditambah 1
    j = j+1

# perulangan for
print("perulangan for 1")
# perulangan for sebagai insisialisasi dari angka 1 hingga angka yang lebih kecil daripada 6.
for i in range(1, 6):
    # perintah jika looping akan tetap berjalan
    print("ini adalah perulangan ke :", i)


# perulangan for 2
print("perulangan for 2")
for i in range(1, 11):
    if (i % 2 == 0):
        print("Angka genap :", i)
    else:
        print("Angka ganjil:", i)
# kenapa ad dua dan nol pada if, karna (%2) berfungsi sebagai pembagi/modulus sedangkan (0) adalah sisa bagi.
# cara kerja adalah apabila sisa bagi nya nol maka program akan stop pada if.
# dan jika sisa bagi bukan nol maka program akan lanjut pada else. dan akan mengulang sebanyak yang diminta pada range.

print("penggunaan def")
# penggunaan def


def luas_segitiga(alas, tinggi):  # alas dan tinggi merupakan parameter yang masuk
    luas = (alas * tinggi) / 2
    print("Luas segitiga: %f" % luas)
    # fungsi %f disini untuk menetukan tipe bila #f akan menjadi float dan ini bisa diganti.
    # apabila diganti %i maka akan menjadi integer dan %s akan menjadi string.


# pemanggilan fungsi
# 4 dan 6 merupakan parameter yang diinputkan kedalam fungsi luas segitiga fungsi luas segitiga
luas_segitiga(4, 6)


print("penggunaan def dan return")
# penggunaan def dan return
# alas dan tinggi merupakan parameter yang masuk


def luas_segitiga(alas, tinggi):
    luas = (alas*tinggi) / 2
    return luas  # return digunakan untuk mengembalikan nilai ke fungsi yang memanggilnya


# pemanggilan fungsi
# 4 dam 6 merupakan parameter yang diinputkan kedalam fungsi luas segitiga
print("Luas segitiga: %d" % luas_segitiga(4, 6))


# PENGGUNAAN LIBRARY
# menggunakan m sebagai module rename atau alias
# (import math as m) contoh penggunaan library math, library harus di taruh di paling atas
# namun apabila ingin menaruh penggunan dari library tsb contoh(print"Nilai pi adalah:", m.pi) bebas boleh di taruh dimana pun

# m.pi merupakan sintak untuk memanggil fungsi
print("Nilai pi adalah:", m.pi)
