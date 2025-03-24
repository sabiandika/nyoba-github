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

# import pandas as pd
# import numpy as np  (harusnya gausah pake #, # disini fungsinya supaya import ini gak naik ke atas)
# import matplotlib.pyplot as plt

# kalo mau pake library kaya panda , numpy, matplotlib, dll, harus diimport dulu/ download dulu baru bisa di run

# table = pd.read_csv( "https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")  #{pd.read csv untuk membaca csv menggunakan pandas}
# table.head()
# x_label = table['NAMA KELURAHAN']    #{x_label mengambil data dari tabel dari kolom 'NAMA KELURAHAN'}
# plt.bar(x=np.arange(len(x_label)), height=table['LAKI-LAKI WNI'])
# plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=90)   #{buat ngambil NAMA KELURAHAN di bawah chart}
# plt.xlabel('Kelurahan di Jakarta Pusat')     #{x sebelum label berfungsi menaruh label(perintahnya label) sesuai sumbu x}
# plt.ylabel('Jumlah Penduduk Laki - Laki')     #{y sebelum label berfungsi menaruh label(perintahnya label) sesuai sumbu y}
# plt.title('Persebaran Jumlah Penduduk Laki- Laki di Jakarta Pusat')    #{sedangkan label berfungsi menaruh label di atas chart}

# plt.show() #{show berguna untuk menampilkan chart}

# (harusnya gausah pake #, # disini fungsinya supaya import ini gak naik ke atas)
