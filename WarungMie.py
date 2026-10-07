print("Selamat datang di Warung Mie pak Bambang")
print("Berikut daftar menu yang tersedia di Warung Mie pak Bambang")
daftar = {
    "Mie Original"          : 7000,
    "Mie Goreng + telur"    : 11000,
    "Mie Nyemek Original"   : 10000,
    "Mie Nyemek + Telur"    : 13000
}
for menu in daftar:
    print(f"{menu} : Rp. {daftar[menu]}")

pesanan_list = []
jumlah_list = []

pesan = str(input("Masukkan pesanan anda : "))
jumlah = int(input("Masukkan jumlah pesanan : "))

pesanan_list.append(pesan)
jumlah_list.append(jumlah)

def tambah():
    pesanan_baru = str(input("Masukkan pesanan anda: "))
    jumlah_baru = int(input("Masukkan jumlah pesanan: "))

    if pesanan_baru in daftar:
        total_baru = daftar[pesanan_baru] * jumlah_baru
        print(f"Harga total pesanan {pesanan_baru} sebanyak {jumlah_baru} dengan harga Rp. {total_baru}")
        pesanan_list.append(pesanan_baru)
        jumlah_list.append(jumlah_baru)
    else:
        print("Maaf, menu tidak ada di daftar")
    
def lihat():
    print("===== Pesanan Anda =====")
    for i in range(len(pesanan_list)):
        print(f"Pesanan anda {pesanan_list[i]} dengan jumlah : {jumlah_list[i]}")
        print(f"Dengan total semuanya Rp. {daftar[pesanan_list[i]] * jumlah_list[i]}")

def bayar():
    print("===== Total Pesanan Anda =====")
    total = 0
    for i in range(len(pesanan_list)):
        total += daftar[pesanan_list[i]] * jumlah_list[i]
    print(f"Total harga yang harus dibayar adalah Rp. {total}")

def keluar():
    print("Apakah anda yakin ingin keluar? (y/n)")
    pilihan = input("Masukkan pilihan anda: ")
    if pilihan.lower() == "y":
        print("Terima kasih telah berbelanja di Warung Mie pak Bambang")
        return True
    else:
        print("Kembali ke menu utama")
        return False

while True:
    print("Menu")
    print("1. Tambah")
    print("2. Lihat Pesanan")
    print("3. Bayar")
    print("4. Keluar")
    
    pilihan = input("Masukkan pilihan anda: ")
    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        lihat()
    elif pilihan == "3":
        bayar()
    elif pilihan == "4":
        if keluar():
            break
    else:
        print("Pilihan tidak ada di menu silahkan pilih menu yang ada")