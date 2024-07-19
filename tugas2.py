def input_user():
    """fungsi untuk menerima input dari user"""

    while True:
        try:
            print("="*50)
            angka = input("Silahkan masukkan angka yang Anda inginkan: ") # input dari user
            if angka.isnumeric(): # input user harus angka
                angka = int(angka) # casting data type ke integer
                return angka # mengembalikan nilai variabel angka
            
            else:
                print("Data yang Anda masukkan salah, harus bilangan bulat bernilai positif, silahkan coba lagi...!!!")
        except:
            print("Data yang Anda masukkan salah, harus bilangan bulat bernilai positif, silahkan coba lagi...!!!")
            
def is_prima(angka):
    """fungsi untuk mengecek apakah argument termasuk bilangan prima atau bukan"""
    
    jenis = ""
    result = "dan bilangan prima"
    
    if (angka == 0 or angka == 1): # jika angka sama dengan 0 atau angka sama dengan 1, maka
        result = "bukan bilangan prima" # value string di assignment ke variabel result 
    
    elif angka == 2: # jika angka sama dengan 2 maka,
        result = "merupakan bilangan prima special karena satu-satunya bilangan genap dan prima" # value string di assignment ke variabel result

    for x in range(2, angka): # untuk setiap  perulangan x di dalam range yang dimulai dari index ke-2 dan berakhir sesuai dengan value di variabel "angka", maka
        if angka % x == 0: # jika sisa hasil angka dibagi x sama dengan 0, maka
            result = "dan bukan bilangan prima" # result memiliki value bukan bilangan prima
            
        elif angka % 2 == 0: # jika sisa hasil angka dibagi 2 sama dengan 0, maka
                jenis = "bilangan genap" # jenis memiliki value bilangan genap
        else: # jika kondisi diatas tidak terpenuhi, maka
                jenis = "bilangan ganjil" # jenis memiliki value bilangan ganjil
    print(f"Angka {angka} adalah {jenis} {result}") # fungsi menampilkan value hasil operasi program
    
while True: # Program akan running infinite
    angka = input_user()
    is_prima(angka)