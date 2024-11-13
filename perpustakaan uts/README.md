Sistem Manajemen Perpustakaan
Ini adalah Sistem Manajemen Perpustakaan sederhana yang memungkinkan pengguna untuk melihat, meminjam, menambah, dan menghapus buku dari perpustakaan. Sistem ini dirancang menggunakan konsep Pemrograman Berorientasi Objek (OOP) seperti Enkapsulasi , Abstraksi , Pewarisan , dan Polimorfisme .

Fitur
Enkapsulasi : Buku memiliki properti seperti ID, judul, ketersediaan, dan lokasi, serta metode untuk meminjam dan mengembalikan buku.
Abstraksi : LibraryKelas mengabstraksikan rincian pengelolaan koleksi buku dan memungkinkan tindakan seperti meminjam atau melihat buku.
Pewarisan : AdminKelas memperluas Userkelas, yang memungkinkan admin untuk menambah dan menghapus buku.
Polimorfisme : UserKelas dan Adminkelas keduanya dapat melihat buku, tetapi hanya Admindapat menambah atau menghapus buku.
Kelas dan Metode
1. BookKelas
Mewakili sebuah buku di perpustakaan.

Properti:
id: Pengenal unik untuk buku tersebut.
title: Judul buku.
available: Boolean yang menunjukkan apakah buku tersedia untuk dipinjam ( True) atau tidak ( False).
location: Lokasi rak buku.
Metode:
borrow(): Menandai buku sebagai dipinjam dan mengembalikan Truejika berhasil dipinjam.
return_book(): Menandai buku sebagai tersedia lagi.
2. LibraryKelas
Mewakili perpustakaan yang mengelola koleksi buku.

Properti:
books: Daftar yang menyimpan semua buku di perpustakaan.
Metode:
show_books(): Menampilkan daftar semua buku dengan ID, judul, status ketersediaan, dan lokasinya.
borrow_book(book_id): Memungkinkan pengguna untuk meminjam buku dengan ID-nya.
find_book(book_id): Mencari buku berdasarkan ID-nya dan mengembalikan buku jika ditemukan, jika tidak None.
3. UserKelas
Mewakili pengguna perpustakaan umum.

Properti:
name: Nama pengguna.
id: Pengenal unik pengguna.
Metode:
view_books(library): Memungkinkan
4. AdminClUser)
Mewakili pengguna admin dengan hak istimewa tambahan.

Metamfetamin
add_book(library, book): Halo
remove_book(library, book_id):# perpustakaan-uts
