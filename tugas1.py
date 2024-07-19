# Input data dari User
nama = input("Masukkan nama Anda: ")
pekerjaan = input("Masukkan pekerjaan Anda: ")
gaji = int(input("Masukkan gaji Anda: "))

# Perhitungan gaji dan pajak
pajak = (5/100) * gaji # pajak diambil 5% dari gaji
gaji = int(gaji - pajak) # gaji dipotong pajak 5%

# Data result
data = {"nama":nama,
        "pekerjaan":pekerjaan,
        "gaji":gaji}
print(data)