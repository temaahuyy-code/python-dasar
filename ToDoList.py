print("To Do List Sederhana")

tugas = str(input("Masukkan tugas anda : "))

list_tugas = []

list_tugas.append(tugas)

def tambah():
    tugas_baru = str(input("Masukkan tugas baru : "))
    list_tugas.append(tugas_baru)

def lihat():
    for i in range(len(list_tugas)):
        print(f"Tugas anda {i+1} : {list_tugas[i]}")

def hapus():
    hapus = str(input("Masukkan tugas yang ingin dihapus : "))
    if hapus in list_tugas:
        list_tugas.remove(hapus)
        print(f"Tugas {hapus} berhasil dihapus")
    else:
        print("Tugas tidak ditemukan")

def keluar():
    print("Apakah anda ingin keluar? (y/n)")
    pilih = input("= ")
    if pilih.lower() == "y":
        print("Terima kasih")
        return True
    else:
        print("Kembali ke utama")
        return False

print()

while True:
    print("Menu")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

    pilihan = input("Masukkan menu yang ingin dipilih : ")
    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        lihat()
    elif pilihan == "3":
        hapus()
    elif pilihan == "4":
        if keluar():
            break
    else:
        print("Menu tidak ada") 
print()