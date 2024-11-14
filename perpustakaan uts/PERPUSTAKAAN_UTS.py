import datetime

books = [
    {'id': 1, 'judul': 'Buku Sistem Operasi', 'tersedia': True, 'letak': 'Rak 1'},
    {'id': 2, 'judul': 'Buku Pemrograman Berorientasi Objek', 'tersedia': False, 'letak': 'Rak 2'},
    {'id': 3, 'judul': 'Buku Rekayasa Perangkat Lunak', 'tersedia': True, 'letak': 'Rak 3'},
    {'id': 4, 'judul': 'Buku Statistik dan Probobilitas', 'tersedia': True, 'letak': 'Rak 4'},
    {'id': 5, 'judul': 'Buku Basis Data Terapan', 'tersedia': True, 'letak': 'Rak 5'},
]

def lihat_buku():
    print("\nDaftar Buku:")
    for book in books:
        print(f"ID: {book['id']}, Judul: {book['judul']}, Tersedia: {'Ya' if book['tersedia'] else 'Tidak'}, Letak: {book['letak']}")

def pinjam_buku():
    lihat_buku()
    id_buku = int(input("\nMasukkan ID Buku yang ingin dipinjam: "))
    nama = input("Masukkan Nama Anda: ")
    tanggal_pinjam = datetime.date.today().strftime("%Y-%m-%d")
    tanggal_kembali = input("Masukkan Tanggal Pengembalian (YYYY-MM-DD): ")

    for book in books:
        if book['id'] == id_buku and book['tersedia']:
            book['tersedia'] = False
            print("\nPemijaman berhasil!")
            print(f"Nama Perpustakaan: Perpustakaan Unisulla")
            print(f"Nama: {nama}")
            print(f"Tanggal Peminjaman: {tanggal_pinjam}")
            print(f"Tanggal Pengembalian: {tanggal_kembali}")
            print(f"Judul Buku: {book['judul']}")
            print(f"ID Buku: {book['id']}")
            print("Selamat berkunjung kembali!")
            return

    print("Buku tidak tersedia atau ID tidak valid!")

def tambah_buku():
    id_buku = int(input("\nMasukkan ID Buku: "))
    judul_buku = input("Masukkan Judul Buku: ")
    tersedia = input("Tersedia (Ya/Tidak): ").lower() == 'ya'
    letak = input("Masukkan Letak Buku: ")

    books.append({'id': id_buku, 'judul': judul_buku, 'tersedia': tersedia, 'letak': letak})
    print(f"\nBuku '{judul_buku}' berhasil ditambahkan!")

def hapus_buku():
    id_buku = int(input("\nMasukkan ID Buku yang akan dihapus: "))
    global books
    books = [book for book in books if book['id'] != id_buku]
    print(f"Buku dengan ID {id_buku} berhasil dihapus!")

# Menu utama
def main():
    while True:
        print("Selamat datang di Perpustakaan Unisulla--")
        role = input("Pilih login:\n1. User\n2. Admin\nPilih (1/2): ")

        if role == '1':
            while True:
                print("\nMenu User:")
                print("1. Melihat Buku")
                print("2. Meminjam Buku")
                print("3. Selesai")
                action = input("Pilih aksi (1/2/3): ")

                if action == '1':
                    lihat_buku()
                elif action == '2':
                    pinjam_buku()
                elif action == '3':
                    print("Terima kasih, sampai jumpa!")
                    break
                else:
                    print("Pilihan tidak valid!")

        elif role == '2':
            while True:
                print("\nMenu Admin:")
                print("1. Melihat Buku")
                print("2. Menambahkan Buku")
                print("3. Menghapus Buku")
                print("4. Selesai")
                action = input("Pilih aksi (1/2/3/4): ")

                if action == '1':
                    lihat_buku()
                elif action == '2':
                    tambah_buku()
                elif action == '3':
                    hapus_buku()
                elif action == '4':
                    print("Terima kasih, sampai jumpa!")
                    break
                else:
                    print("Pilihan tidak valid!")

        else:
            print("Pilihan tidak valid!")

        kembali = input("\nKembali ke login? (Y/N): ").lower()
        if kembali != 'y':
            print("Terima kasih, program selesai.")
            break

if __name__ == "__main__":
    main()
