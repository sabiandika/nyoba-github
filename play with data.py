import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
from contextlib import closing
import csv

# tentukan lokasi file, nama file, dan inisialisasi csv atu bisa juga diambil dari link seperti di bawah ini.
url = 'https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv'

# baca file csv secara streaming
with closing(requests.get(url, stream=True)) as r:
    # with closing(requests.get(url,stream=True)) as r:`: Membuka koneksi ke URL yang diberikan dengan menggunakan metode `GET` dan mode streaming.
    f = (line.decode('utf-8') for line in r.iter_lines())
# `f = (line.decode('utf-8') for line in r.iter_lines())`: Membaca data baris per baris dari respons HTTP dan mendekodekannya ke dalam format UTF-8.
    reader = csv.reader(f, delimiter=',')
# (reader =)Membuat objek `reader` dari modul `csv` dengan menggunakan delimiter koma (`,`).
    # membaca baris per baris
    for row in reader:
        print(row)


# BUAT BAR CHART PAKE LIBRARY PANDAS, MATPLOTLIB DAN NUMPY

# {pd.read csv untuk membaca csv menggunakan pandas}
table = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
# {x_label mengambil data dari tabel dari kolom 'NAMA KELURAHAN'}
x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)), height=table['LAKI-LAKI WNI'])
# {buat ngambil NAMA KELURAHAN di bawah chart}
plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=90)
# {x sebelum label berfungsi menaruh label(perintahnya label) sesuai sumbu x}
plt.xlabel('Kelurahan di Jakarta Pusat')
# {y sebelum label berfungsi menaruh label(perintahnya label) sesuai sumbu y}
plt.ylabel('Jumlah Penduduk Laki - Laki')
# {sedangkan label berfungsi menaruh label di atas chart}
plt.title('Persebaran Jumlah Penduduk Laki- Laki di Jakarta Pusat')

plt.show()  # {show berguna untuk menampilkan chart}

# (harusnya gausah pake #, # disini fungsinya supaya import ini gak naik ke atas)


# MENGUBAH NILAI
print("MENGUBAH NILAI")

# {Mengatur opsi pandas untuk menampilkan maksimal 10 kolom.}
pd.set_option("display.max_column", 10)

# Membaca dataset
# {Membaca dataset credit_scoring dari file Excel yang di-host di URL tertentu.}
dataset_credit_scoring = pd.read_excel(
    'https://storage.googleapis.com/dqlab-dataset/credit_scoring_dqlab.xlsx')

# Membuat dataset
# { Membuat dataset baru yang hanya berisi kolom-kolom tertentu dari dataset_credit_scoring,}
dataset = dataset_credit_scoring[['pendapatan_setahun_juta', 'kpr_aktif',
                                  'durasi_pinjaman_bulan', 'jumlah_tanggungan', 'rata_rata_overdue', 'risk_rating']]
# {Menampilkan lima baris pertama dari dataset yang baru dibuat.}
print(dataset.head())

# Mengubah data kpr_aktif menjadi tipe integer: 'YA' = 1 dan 'TIDAK' = 0
# {Mengubah data pada kolom 'kpr_aktif' menjadi tipe integer, di mana 'YA' akan diubah menjadi 1 dan 'TIDAK' akan diubah menjadi 0.}
dataset['kpr_aktif'] = dataset['kpr_aktif'].replace(['YA', 'TIDAK'], [1, 0])
print("\ndataset setelah kpr_aktif menjadi kolom numerik")
# {Menampilkan lima baris pertama dari dataset yang baru dibuat.}
print(dataset.head())
