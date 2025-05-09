# Data yang dinyatakan ke dalam dictionary
print("chapter 1")
sepatu = {"nama": "Sepatu Niko", "harga": 150000, "diskon": 30000}
baju = {"nama": "Baju Unikloh", "harga": 80000, "diskon": 8000}
celana = {"nama": "Celana Lepis", "harga": 200000, "diskon": 60000}
# Hitunglah harga masing-masing data setelah dikurangi diskon
harga_sepatu = sepatu["harga"] - sepatu["diskon"]
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]
# Hitung harga total
total_harga = harga_sepatu + harga_baju + harga_celana
# Hitung harga kena pajak
total_pajak = total_harga * 0.1
# Cetak total_harga + total_pajak
print(f"Jadi Harga Yang Harus Dibayar Adalah: ", total_harga + total_pajak)


print("Chapter 2")
# OPSI 1
# Kode awal
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1  # pajak dalam persen ~ 10%
harga_bayar = 1 - potongan_harga  # baris pertama,   isi harga_bayar= 0.7
harga_bayar *= total_harga  # baris kedua,   0,7 dikali dengan 150000
# baris ketiga, harga bayar =105000, pajak=0.1, lalu dikali dan hasilnya 10500
pajak_bayar = harga_bayar * pajak
harga_bayar += pajak_bayar  # baris ke-4, 105000 + 10500 = 115500
print("Opsi 1 -harga_bayar =", harga_bayar)  # harga_bayar berisi 115500

# OPSI 2

# Penyederhanaan baris kode dengan menerapkan prioritas operator
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1  # pajak dalam persen ~ 10%
harga_bayar = (1 - potongan_harga) * total_harga  # baris pertama
harga_bayar += harga_bayar * pajak  # baris kedua
print("Opsi 2 -harga_bayar =", harga_bayar)
