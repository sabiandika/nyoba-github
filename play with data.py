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

# BUAT BAR CHART PAKE LIBRARY PANDAS

# import pandas as pd
# import numpy as np  (harusnya gausah pake #, # disini fungsinya supaya import ini gak naik ke atas)
# import matplotlib.pyplot as plt

# [kalo mau pake library kaya panda , numpy, matplotlib, dll, harus diimport dulu/ download dulu baru bisa di run]

# table = pd.read_csv( "https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
# table.head()
# x_label = table['NAMA KELURAHAN']
# plt.bar(x=np.arange(len(x_label)), height=table['LAKI-LAKI WNI'])
# plt.show()


# (harusnya gausah pake #, # disini fungsinya supaya import ini gak naik ke atas)
