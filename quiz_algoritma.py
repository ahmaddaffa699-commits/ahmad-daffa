
# Program Remedial Ujian Matematika

# Input data mahasiswa
nama = input("Masukkan nama mahasiswa: ")

# Menentukan target nilai berdasarkan nama
if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    target = int(input("Masukkan target nilai: "))

print("\nNama Mahasiswa :", nama)
print("Target Nilai   :", target)

# Proses ujian dan remedial
percobaan = 1
lulus = False

while percobaan <= 3:
    nilai = int(input(f"Masukkan nilai ujian ke-{percobaan}: "))

    if nilai >= target:
        lulus = True
        print("\nSelamat!", nama, "dinyatakan LULUS.")
        print("Nilai yang diperoleh:", nilai)
        break
    else:
        print("Nilai belum mencapai target.")

        if percobaan < 3:
            print("Silakan mengikuti remedial.")
        percobaan += 1

# Hasil akhir
if lulus:
    print(f"{nama} berhasil lulus dalam {percobaan} kali percobaan.")
else:
    print(f"\nMaaf, {nama} dinyatakan TIDAK LULUS.")
    print("Sudah mengikuti 3 kali percobaan.")
