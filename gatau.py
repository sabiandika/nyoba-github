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
