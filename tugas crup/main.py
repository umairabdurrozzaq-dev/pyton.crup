from prettytable import PrettyTable

# data awal sudah ada
data = [
    {"id": 1, "nama": "Ujang", "kelas": "X-A"},
    {"id": 2, "nama": "Asep", "kelas": "X-B"},
    {"id": 3, "nama": "Budi", "kelas": "X-C"}
]

def tambah_data():
    id_data = int(input("Masukkan ID: "))
    nama = input("Masukkan Nama: ")
    kelas = input("Masukkan Kelas: ")

    item = {
        "id": id_data,
        "nama": nama,
        "kelas": kelas
    }

    data.append(item)
    print("✅ Data berhasil ditambahkan!")

def tampil_data():
    if len(data) == 0:
        print("⚠️ Data masih kosong.")
    else:
        table = PrettyTable()
        table.field_names = ["Index", "ID", "Nama", "Kelas"]

        for i in range(len(data)):
            table.add_row([i, data[i]["id"], data[i]["nama"], data[i]["kelas"]])

        print(table)

def ubah_data():
    tampil_data()
    if len(data) > 0:
        index = int(input("Masukkan index data yang mau diubah: "))
        if index >= 0 and index < len(data):
            data[index]["id"] = int(input("Masukkan ID baru: "))
            data[index]["nama"] = input("Masukkan Nama baru: ")
            data[index]["kelas"] = input("Masukkan Kelas baru: ")
            print("✅ Data berhasil diubah!")
        else:
            print("❌ Index tidak valid.")

def hapus_data():
    tampil_data()
    if len(data) > 0:
        index = int(input("Masukkan index data yang mau dihapus: "))
        if index >= 0 and index < len(data):
            data.pop(index)
            print("✅ Data berhasil dihapus!")
        else:
            print("❌ Index tidak valid.")

# PROGRAM UTAMA
while True:
    print("\n=== MENU ===")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampil_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "0":
        print("👋 Program selesai.")
        break
    else:
        print("❌ Menu tidak tersedia.")
