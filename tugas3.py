from module import Karyawan

while True:
    nama = input("Masukkan nama karyawan : ")
    position = input("Masukkan posisi bagian kerja : ")
    salary = int(input("Masukkan nominal gaji : "))
    
    aku = Karyawan(nama, position, salary)
    
    aku.info()
    print(f"Gaji saat ini => {aku.get_salary()}")
    
    new_salary = int(input("Masukkan nominal gaji terbaru : "))
    aku.set_salary(new_salary)
    aku.info()
    
    aku.salary_up()
    aku.info()
    
    print("\n")
