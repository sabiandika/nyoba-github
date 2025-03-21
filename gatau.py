i = 5

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
