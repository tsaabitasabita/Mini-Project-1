# Mini Project 1

Praktikum = "Dasar - dasar Pemograman"
print ("Praktikum", Praktikum)
Nama =  input("Nama : ")
Nim = input("NIM : ")
kelas = input("Kelas : ")

print ()

print("====================================")
print(" PROGRAM PERHITUNGAN GAJI KARYAWAN ")
print("====================================")


print("Selamat Datang " , Nama)
print("Silahkan mengisi format dibawah ini untuk mengetahui gaji anda")
print("=========================================================")

nama_karyawan = ("Nama Karyawan: ")
jam_kerja = ("Jam kerja : ")
tarif_kerja = ("Tarif kerja : ")

def hitung_gaji(nama_karyawan,jam_kerja,tarif_kerja):
    jam_kerja = int(jam_kerja)
    tarif_kerja = int(tarif_kerja)

    if jam_kerja >= 160:
        bonus = tarif_kerja * 10/100 # 10% bonus
        gaji = tarif_kerja + bonus
        print("Karyawan atas nama" , nama_karyawan)
        print("Dengan jumlah jam kerja" , jam_kerja)
        print("Anda mendapat bonus gaji sebesar 10%")
        print("Gaji anda adalah Rp" , gaji)

    else:
        print("Gaji anda adalah Rp", tarif_kerja)

    

while True :
    nama_karyawan =input("Nama Karyawan: ") 
    jam_kerja=input("Jumlah Jam Kerja: ")
    tarif_kerja=input("Tarif Kerja: ")

    hitung_gaji(nama_karyawan,jam_kerja,tarif_kerja)

    selesai = input("Ingin menghitung gaji anda lagi? (ya/tidak)")
    if selesai.lower() == "tidak":
        print("Terima Kasih telah menggunakan proram")
        break










 


    


