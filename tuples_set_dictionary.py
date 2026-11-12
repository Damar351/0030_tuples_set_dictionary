# TUPLE

# A
# MEMBUAT TUPLE BERNAMA MAHASISWA YANG BERISI DATA DIRI(Nama, NIM, Prodi)
mahasiswa = ("Damar Sasongko", 2605060030, "Teknologi Informasi")
print(f"Data mahasiswa = \n{mahasiswa}\n")

# B
# MENAMPILKAN DATA NIM DAN PRODI DENGAN MENGAKSES INSDEKSNYA
print(f"Nim = {mahasiswa[1]}")
print(f"Prodi = {mahasiswa[2]}\n")

# C
# MENJALANKAN KODE mahasiswa[2] = "Teknologi Informasi" DAN MENJELASKAN PESAN ERROR YANG MUNCUL
# mahasiswa[2] = "Teknologi Informasi"
print("Kode tersebut error karena ingin  mengganti index ke-2 dari turples mahasiswa, " \
      "setelah turples dibuat maka tidak bisa menambah ataupun mengganti data di dalamnya.\n")

# D
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)
print("Angka 10 dan 4 yang ditulis dua kali, saat dicetak akan tercetak satu kali karena sifat set yang unik.\n")

# MANIPULASI DICTIONARY

# A
data_mahasiswa = {
    "nim" : "240101",
    "nama" : "Budi Santoso",
    "prodi" : "Teknologi Informasi"
}
print(data_mahasiswa)

# B
data_mahasiswa["prodi"] = "Sastra Mesin"
data_mahasiswa.update({"angkatan" : "2026"})
print(data_mahasiswa)

# C
del data_mahasiswa["nim"]
print(data_mahasiswa)

# PERULANGAN DICTIONARY
# A
harga_buah = {
    "apel" : 5000,
    "pisang" : 3000,
    "jeruk" : 7000,
    "anggur" : 15000
}

# B

for buah,harga in harga_buah.items() :
    print(f"Harga {buah} : Rp{harga}")

# C
total = 0
for harga in harga_buah.values():
    total += harga
print("========================")
print(f"Total belanja = Rp{total}")