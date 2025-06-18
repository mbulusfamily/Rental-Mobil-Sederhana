# Aplikasi Rental Mobil Sederhana (Console Python)

Aplikasi ini merupakan sistem simulasi jasa rental mobil berbasis terminal, dibuat dengan bahasa Python. Sistem ini mendukung dua peran utama: **Admin** (pengelola rental) dan **Customer** (pelanggan), serta menyediakan fitur manajemen armada mobil dan proses rental end-to-end.

Aplikasi ini sangat cocok untuk latihan logika pemrograman, studi kasus, tugas akhir, atau pembelajaran pemrograman Python berbasis konsol.

---

## Daftar Isi

- [Fitur Aplikasi](#fitur-aplikasi)
  - [Fitur Login dan Role](#fitur-login-dan-role)
  - [Fitur untuk Admin (Jasa Rental)](#fitur-untuk-admin-jasa-rental)
    - [Manajemen Mobil](#manajemen-mobil)
    - [Manajemen Harga Mobil](#manajemen-harga-mobil)
    - [Manajemen Data Pelanggan](#manajemen-data-pelanggan)
    - [Menu dan Navigasi Admin](#menu-dan-navigasi-admin)
  - [Fitur untuk Customer (Pelanggan)](#fitur-untuk-customer-pelanggan)
    - [Proses Sewa Mobil](#proses-sewa-mobil)
    - [Keranjang Sewa dan Pembayaran](#keranjang-sewa-dan-pembayaran)
    - [Bukti Sewa](#bukti-sewa)
    - [Menu dan Navigasi Customer](#menu-dan-navigasi-customer)
- [Struktur Data](#struktur-data)
- [Penjelasan Fungsi](#penjelasan-fungsi)
  - [Fungsi-fungsi Utama](#fungsi-fungsi-utama)
  - [Fungsi Customer](#fungsi-customer)
  - [Fungsi Admin](#fungsi-admin)
- [Alur Program](#alur-program)
- [Instalasi & Cara Menjalankan](#instalasi--cara-menjalankan)
- [Contoh Penggunaan](#contoh-penggunaan)
- [Catatan & Pengembangan Lanjut](#catatan--pengembangan-lanjut)

---

## Fitur Aplikasi

### Fitur Login dan Role

- **Login dengan Role:**  
  - Admin (pengelola rental)
  - Customer (pelanggan)
- **Admin** harus memasukkan username dan password:
  - Username: `SukmaBagusYTTTA`
  - Password: `Sukma123`
- **Customer** langsung masuk ke menu pelanggan tanpa password.

---

### Fitur untuk Admin (Jasa Rental)

#### Manajemen Mobil

- **Lihat Daftar Mobil:**  
  Melihat seluruh mobil beserta detail (nama, harga, jenis, bahan bakar, transmisi, plat, status).
- **Tambah Mobil:**  
  Menambah mobil baru ke daftar rental, dengan input detail dan konfirmasi.
- **Hapus Mobil:**  
  Menghapus mobil dari daftar aktif (soft delete, masuk ke recycle bin/keranjang sampah).
- **Kembalikan Mobil:**  
  Mengembalikan mobil dari keranjang sampah ke daftar aktif.
- **Cari Mobil:**  
  Mencari mobil berdasarkan nama (case-insensitive).
- **Cek Ketersediaan Mobil:**  
  Melihat hanya mobil yang tersedia untuk disewa.

#### Manajemen Harga Mobil

- **Update Harga Mobil:**  
  Mengubah harga sewa per hari pada mobil tertentu.

#### Manajemen Data Pelanggan

- **Lihat Informasi Pelanggan:**  
  Menampilkan data pelanggan yang pernah melakukan booking atau sewa.

#### Menu dan Navigasi Admin

- **Menu interaktif** dengan opsi:
  - Daftar Mobil
  - Cari Mobil
  - Update Harga Mobil
  - Tambah Mobil
  - Hapus Mobil
  - Kembalikan Mobil (dari recycle bin)
  - Informasi Pelanggan
  - Kesediaan Mobil
  - Logout
  - Keluar dari aplikasi

---

### Fitur untuk Customer (Pelanggan)

#### Proses Sewa Mobil

- **Lihat Mobil:**  
  Menampilkan seluruh mobil yang tersedia.
- **Input Identitas:**  
  Mengisi data diri (nama, alamat, no telepon, NIK), dengan validasi.
- **Pilih Mobil dan Booking:**  
  Memilih mobil, memasukkan tanggal sewa dan pengembalian, serta durasi sewa.
- **Pembayaran:**  
  Menghitung total harga dan memproses pembayaran. Jika batal/lupa membayar, booking masuk ke keranjang sewa.

#### Keranjang Sewa dan Pembayaran

- **Cek Keranjang Sewa:**  
  Melihat daftar booking yang belum dibayar dan melakukan pembayaran.

#### Bukti Sewa

- **Lihat Bukti Sewa:**  
  Menampilkan riwayat/bukti sewa yang sudah dibayar.

#### Menu dan Navigasi Customer

- **Menu interaktif** dengan opsi:
  - Daftar Mobil
  - Keranjang Sewa
  - Lihat Bukti Sewa
  - Logout
  - Keluar dari aplikasi

---

## Struktur Data

- **listMobil, listHarga, jenisMobil, jenisBahanBakar, typeTransmisi, platNomor, ketersediaan**  
  Menyimpan data master armada mobil.
- **identitasPelanggan**  
  List of dict, menyimpan identitas pelanggan yang sudah booking.
- **keranjangSewaList**  
  List of dict, booking yang belum dibayar.
- **buktiSewa**  
  List of dict, booking yang sudah dibayar.
- **recycleMobil**  
  List of dict, mobil yang sudah dihapus (keranjang sampah).

---

## Penjelasan Fungsi

### Fungsi-fungsi Utama

| Nama Fungsi         | Deskripsi Singkat                                                                                 |
|---------------------|--------------------------------------------------------------------------------------------------|
| login               | Menu login awal, untuk memilih admin/customer dan verifikasi admin                                |
| menuUtamaCustomer   | Menu utama customer: daftar mobil, keranjang sewa, bukti sewa, logout, keluar                    |
| menuUtamaJasa       | Menu utama admin: kelola mobil, pelanggan, harga, recycle bin, logout, keluar                    |

---

### Fungsi Customer

| Nama Fungsi         | Deskripsi                                                                                         |
|---------------------|--------------------------------------------------------------------------------------------------|
| tampilkanMobil      | Menampilkan tabel mobil yang tersedia, lanjut ke input identitas atau kembali                    |
| inputIdentitas      | Input identitas pelanggan dengan validasi, lanjut ke pilih mobil                                 |
| pilihMobil          | Memilih mobil, memasukkan tanggal sewa, pembayaran, atau masukkan ke keranjang sewa              |
| keranjangSewaMenu   | Menampilkan keranjang booking yang belum dibayar, proses pembayaran                              |
| lihatBuktiSewa      | Menampilkan riwayat/bukti sewa yang sudah dibayar                                                |

---

### Fungsi Admin

| Nama Fungsi           | Deskripsi                                                                                       |
|-----------------------|------------------------------------------------------------------------------------------------|
| tableDaftarMobilJasa  | Menampilkan seluruh mobil beserta detail untuk admin                                           |
| tambahMobil           | Menambah mobil baru ke daftar, dengan detail lengkap dan konfirmasi                            |
| hapusMobil            | Menghapus mobil (soft delete, masuk recycle bin)                                               |
| kembalikanMobil       | Mengembalikan mobil dari recycle bin ke daftar aktif                                           |
| kesediaanMobil        | Menampilkan hanya mobil yang berstatus tersedia                                                |
| updateHargaMobil      | Mengubah harga sewa per hari pada mobil tertentu                                               |
| cariMobil             | Mencari mobil berdasarkan nama                                                                 |

---

## Alur Program

1. **Login:**
   - Pilih peran (admin/customer)
   - Jika admin: input username dan password
2. **Admin:**
   - Kelola mobil (lihat, tambah, hapus, kembalikan, cari, update harga, cek tersedia)
   - Lihat info pelanggan
   - Keluar/logout
3. **Customer:**
   - Lihat mobil → input identitas → pilih mobil → booking & bayar atau masukkan keranjang sewa
   - Lihat keranjang sewa & proses pembayaran
   - Lihat bukti sewa
   - Keluar/logout

---

## Instalasi & Cara Menjalankan

1. **Install Library [tabulate](https://pypi.org/project/tabulate/):**
   ```bash
   pip install tabulate
   ```

2. **Save kode ke file, misal `main.py` dan jalankan:**
   ```bash
   python main.py
   ```

---

## Contoh Penggunaan

### 1. Login Sebagai Customer

```
=== Selamat Datang di Sistem Jasa Rental Mobil ===
1. Masuk sebagai Admin
2. Masuk sebagai Pelanggan
Apakah Anda ingin masuk sebagai (1) Admin atau (2) Pelanggan? (ketik 1 atau 2): 2
```

---

### 2. Melihat Daftar Mobil (Customer)

```
=== Menu Utama Customer ===
1. Daftar Mobil
2. Keranjang Sewa
3. Lihat Bukti Sewa
4. Logout
5. Keluar
Silakan pilih menu (1/2/3/4/5): 1

Daftar Mobil yang Tersedia:
╔════╤═════════════════╤═════════════════╤═════════════╤══════════════════╤════════════════╤═════════════╤═════════════════╗
│ No │ Nama Mobil      │ Harga Per Hari  │ Jenis Mobil │ Jenis Bahan Bakar│ Tipe Transmisi │ Plat Nomor  │ Ketersediaan   │
╟────┼─────────────────┼─────────────────┼─────────────┼──────────────────┼────────────────┼─────────────┼───────────────╢
│ 1  │ Toyota Avanza   │ Rp 200,000      │ MPV         │ Bensin           │ Manual         │ B 1234 AB   │ Tersedia      │
│ ...│ ...             │ ...             │ ...         │ ...              │ ...            │ ...         │ ...           │
╚════╧═════════════════╧═════════════════╧═════════════╧══════════════════╧════════════════╧═════════════╧═════════════════╝
Lanjut mengisi identitas dan booking mobil? (ya/tidak):
```

---

### 3. Proses Booking & Pembayaran (Customer)

```
Masukkan Identitas Anda:
Nama: Ahmad
Alamat: Jl. Melati No. 10
Nomor Telepon: 081234567890
NIK: 1234567890123456

Identitas Anda:
Nama: Ahmad
Alamat: Jl. Melati No. 10
Nomor Telepon: 081234567890
NIK: 1234567890123456
apakah identitas anda sudah benar? (ya/tidak): ya

Mobil yang tersedia untuk booking:
╔════╤═════════════════╤═════════════════╤══════════════╗
│ No │ Nama Mobil      │ Harga Per Hari  │ Ketersediaan │
╟────┼─────────────────┼─────────────────┼──────────────╢
│ 1  │ Toyota Avanza   │ Rp 200,000      │ Tersedia     │
│ 2  │ Honda Jazz      │ Rp 250,000      │ Tersedia     │
╚════╧═════════════════╧═════════════════╧══════════════╝

Pilih nomor mobil yang ingin Anda booking (atau ketik 'kembali' untuk kembali ke menu utama): 2

Detail Mobil yang Dipilih:
╔═══════════════╤═══════════════╤════════════╤══════════════════╤════════════════╤═════════════╗
│ Nama Mobil    │ Harga Per Hari│ Jenis Mobil│ Jenis Bahan Bakar│ Tipe Transmisi │ Plat Nomor  │
╟───────────────┼───────────────┼────────────┼──────────────────┼────────────────┼─────────────╢
│ Honda Jazz    │ Rp 250,000    │ Hatchback  │ Bensin           │ matic          │ B 2345 CD   │
╚═══════════════╧═══════════════╧════════════╧══════════════════╧════════════════╧═════════════╝

Masukan hari, tanggal sewa (Hari, 00-00-0000): Senin, 10-07-2025
Masukan hari, tanggal pengembalian (Hari, 00-00-0000): Kamis, 13-07-2025
Masukkan durasi sewa dalam hari: 3

Total Harga: Rp 750,000

Apakah Anda ingin melanjutkan ke tahap pembayaran? (ya/tidak): ya

Masukkan jumlah uang pembayaran: 800000
Pembayaran lebih. Silakan ambil kembalian anda: Rp 50,000. Terima kasih telah menyewa mobil kami.
Selamat menikmati perjalanan anda dan tetap berhati-hati dalam berkendara.
```

---

### 4. Cek Keranjang Sewa (Jika Booking Ditunda)

```
=== Menu Utama Customer ===
1. Daftar Mobil
2. Keranjang Sewa
3. Lihat Bukti Sewa
4. Logout
5. Keluar
Silakan pilih menu (1/2/3/4/5): 2

=== Keranjang Sewa ===
╔═════╤═══════════════╤═══════════════╤═════════════════════╤═════════════════════╗
│ Nama│ Mobil         │ Harga         │ Hari Sewa          │ Hari Pengembalian   │
╟─────┼───────────────┼───────────────┼────────────────────┼─────────────────────╢
│ Ahmad│ Honda Jazz   │ Rp 250,000    │ Senin, 10-07-2025  │ Kamis, 13-07-2025   │
╚═════╧═══════════════╧═══════════════╧═════════════════════╧═════════════════════╝

Melanjutkan pembayaran? (ya/tidak): ya
Masukkan jumlah uang pembayaran: 750000
Pembayaran pas. Terima kasih telah menyewa mobil kami.
Selamat menikmati perjalanan anda dan tetap berhati-hati dalam berkendara.
```

---

### 5. Melihat Bukti Sewa

```
=== Menu Utama Customer ===
1. Daftar Mobil
2. Keranjang Sewa
3. Lihat Bukti Sewa
4. Logout
5. Keluar
Silakan pilih menu (1/2/3/4/5): 3

=== Bukti Sewa ===
╔═════╤══════════════╤══════════════╤═════════════════════╤═════════════════════╤════════════╗
│ Nama│ Mobil        │ Harga        │ Hari Sewa          │ Hari Pengembalian   │ Durasi     │
╟─────┼──────────────┼──────────────┼────────────────────┼─────────────────────┼────────────╢
│ Ahmad│ Honda Jazz  │ Rp 750,000   │ Senin, 10-07-2025  │ Kamis, 13-07-2025   │ 3          │
╚═════╧══════════════╧══════════════╧═════════════════════╧═════════════════════╧════════════╝
```

---

### 6. Login Sebagai Admin

```
=== Selamat Datang di Sistem Jasa Rental Mobil ===
1. Masuk sebagai Admin
2. Masuk sebagai Pelanggan
Apakah Anda ingin masuk sebagai (1) Admin atau (2) Pelanggan? (ketik 1 atau 2): 1
Masukkan username admin: SukmaBagusYTTTA
Masukkan password admin: Sukma123
Login berhasil!
```

---

### 7. Daftar Mobil & Tambah Mobil (Admin)

```
=== Menu Rental Mobil ===
1. Daftar Mobil
2. Cari Mobil
3. Update Harga Mobil
4. Tambah Mobil
5. Hapus Mobil
6. Kembalikan mobil dari keranjang sampah
7. Informasi Pelanggan
8. Kesediaan Mobil
9. Logout
10. Keluar

Pilih menu (1-10): 4

Apakah Anda ingin menambahkan mobil baru? (ya/tidak): ya
Masukkan nama mobil: Nissan Livina
Masukkan harga per hari (dalam Rp): 210000
Masukkan jenis mobil: MPV
Masukkan jenis bahan bakar: Bensin
Masukkan tipe transmisi: Manual
Masukkan plat nomor: B 3456 ZX

Apakah anda yakin ingin menambahkan mobil ini?
╔═══════════════╤═══════════════╤════════════╤══════════════════╤════════════════╤═════════════╗
│ Nama Mobil    │ Harga Per Hari│ Jenis Mobil│ Jenis Bahan Bakar│ Tipe Transmisi │ Plat Nomor  │
╟───────────────┼───────────────┼────────────┼──────────────────┼────────────────┼─────────────╢
│ Nissan Livina │ Rp 210,000    │ MPV        │ Bensin           │ Manual         │ B 3456 ZX   │
╚═══════════════╧═══════════════╧════════════╧══════════════════╧════════════════╧═════════════╝
Ketik 'ya' untuk mengkonfirmasi: ya
Mobil Nissan Livina telah ditambahkan.
```

---

### 8. Hapus & Kembalikan Mobil (Admin)

```
Pilih menu (1-10): 5

╔════╤═════════════════╤═══════════════╤═════════════╤══════════════════╤════════════════╤═════════════╤═══════════════╗
│ No │ Nama Mobil      │ Harga Per Hari│ Jenis Mobil │ Jenis Bahan Bakar│ Tipe Transmisi │ Plat Nomor  │ Ketersediaan │
╟────┼─────────────────┼───────────────┼─────────────┼──────────────────┼────────────────┼─────────────┼──────────────╢
│ 10 │ Nissan Livina   │ Rp 210,000    │ MPV         │ Bensin           │ Manual         │ B 3456 ZX   │ Tersedia     │
╚════╧═════════════════╧═══════════════╧═════════════╧══════════════════╧════════════════╧═════════════╧═══════════════╝
Pilih mobil yang ingin dihapus (nomor) atau ketik 'keluar' untuk ke menu utama: 10
Apakah Anda yakin ingin menghapus mobil Nissan Livina? (ya/tidak): ya
Mobil Nissan Livina telah dihapus.
Mobil telah dihapus dan dimasukkan ke keranjang sampah.
```

```
Pilih menu (1-10): 6

Daftar mobil di keranjang sampah:
╔════╤═══════════════╤═════════════╗
│ No │ Nama Mobil    │ Plat Nomor  │
╟────┼───────────────┼─────────────╢
│ 1  │ Nissan Livina │ B 3456 ZX   │
╚════╧═══════════════╧═════════════╝
Pilih mobil yang ingin dikembalikan (nomor) atau ketik 'keluar' untuk ke menu utama: 1
Mobil Nissan Livina telah dikembalikan.
```

---

### 9. Update Harga Mobil (Admin)

```
Pilih menu (1-10): 3

╔════╤═════════════════╤═══════════════╗
│ No │ Nama Mobil      │ Harga Per Hari│
╟────┼─────────────────┼───────────────╢
│ 1  │ Toyota Avanza   │ Rp 200,000    │
│ 2  │ Honda Jazz      │ Rp 250,000    │
│ ...│ ...             │ ...           │
╚════╧═════════════════╧═══════════════╝
Pilih nomor mobil yang ingin diupdate harganya (atau ketik 'keluar' untuk kembali): 2
Masukkan harga baru untuk Honda Jazz (dalam Rp): 275000
apakah anda yakin ingin mengupdate harga mobil ini? (ya/tidak): ya
Harga mobil Honda Jazz berhasil diupdate menjadi Rp 275,000.
```

---

### 10. Cari Mobil (Admin)

```
Pilih menu (1-10): 2
Masukkan nama mobil yang ingin dicari: jazz

╔════╤═════════════════╤═══════════════╤═════════════╤══════════════════╤════════════════╤═════════════╤═══════════════╗
│ No │ Nama Mobil      │ Harga Per Hari│ Jenis Mobil │ Jenis Bahan Bakar│ Tipe Transmisi │ Plat Nomor  │ Ketersediaan │
╟────┼─────────────────┼───────────────┼─────────────┼──────────────────┼────────────────┼─────────────┼──────────────╢
│ 2  │ Honda Jazz      │ Rp 275,000    │ Hatchback   │ Bensin           │ matic          │ B 2345 CD   │ Tersedia     │
╚════╧═════════════════╧═══════════════╧═════════════╧══════════════════╧════════════════╧═════════════╧═══════════════╝
```

---

### 11. Lihat Informasi Pelanggan (Admin)

```
Pilih menu (1-10): 7

Informasi Pelanggan:
Nama: Ahmad, Alamat: Jl. Melati No. 10, Nomor Telepon: 081234567890, NIK: 1234567890123456
```

---

### 12. Input Identitas Customer: Validasi Error

```
Masukkan Identitas Anda:
Nama: 
Alamat: Jl. Kenangan
Nomor Telepon: 0812345
NIK: 12345678

Semua field harus diisi. Silakan coba lagi.

Masukkan Identitas Anda:
Nama: Budi
Alamat: Jl. Kenangan
Nomor Telepon: abcdefghij
NIK: 123456789012345

Nomor telepon harus berupa angka dan minimal 10 digit. Silakan coba lagi.

Masukkan Identitas Anda:
Nama: Budi
Alamat: Jl. Kenangan
Nomor Telepon: 08123456789
NIK: 123456789012345

NIK harus berupa angka dan memiliki panjang 16 digit. Silakan coba lagi.

Masukkan Identitas Anda:
Nama: Budi
Alamat: Jl. Kenangan
Nomor Telepon: 081234567890
NIK: 1234567890123456

Identitas Anda:
Nama: Budi
Alamat: Jl. Kenangan
Nomor Telepon: 081234567890
NIK: 1234567890123456
apakah identitas anda sudah benar? (ya/tidak): ya
Identitas Anda sudah benar.
Identitas berhasil disimpan.
```

---

### 13. Pembayaran Kurang (Customer)

```
Total Harga: Rp 600,000

Apakah Anda ingin melanjutkan ke tahap pembayaran? (ya/tidak): ya
Booking untuk Suzuki Ertiga berhasil!
Silakan lakukan pembayaran.
Masukkan jumlah uang pembayaran: 500000
Pembayaran kurang. Silakan masukkan jumlah uang lagi sebesar Rp 100,000.
Masukkan jumlah uang pembayaran: 100000
Pembayaran berhasil. Terima kasih telah menyewa mobil kami.
Selamat menikmati perjalanan anda dan tetap berhati-hati dalam berkendara.
```

---

### 14. Pilihan Menu Tidak Valid

```
=== Menu Utama Customer ===
1. Daftar Mobil
2. Keranjang Sewa
3. Lihat Bukti Sewa
4. Logout
5. Keluar
Silakan pilih menu (1/2/3/4/5): 7
Pilihan tidak valid. Silakan coba lagi.
```

---

### 15. Hapus Mobil dengan Pembatalan

```
Pilih menu (1-10): 5

╔════╤═════════════════╤═══════════════╤═════════════╤══════════════════╤════════════════╤═════════════╤═══════════════╗
│ No │ Nama Mobil      │ Harga Per Hari│ Jenis Mobil │ Jenis Bahan Bakar│ Tipe Transmisi │ Plat Nomor  │ Ketersediaan │
╟────┼─────────────────┼───────────────┼─────────────┼──────────────────┼────────────────┼─────────────┼──────────────╢
│ 2  │ Honda Jazz      │ Rp 250,000    │ Hatchback   │ Bensin           │ matic          │ B 2345 CD   │ Tersedia     │
╚════╧═════════════════╧═══════════════╧═════════════╧══════════════════╧════════════════╧═════════════╧═══════════════╝
Pilih mobil yang ingin dihapus (nomor) atau ketik 'keluar' untuk ke menu utama: 2
Apakah Anda yakin ingin menghapus mobil Honda Jazz? (ya/tidak): tidak
Penghapusan dibatalkan.
```

---

### 16. Update Harga Mobil dengan Input Salah

```
Pilih menu (1-10): 3

╔════╤═════════════════╤═══════════════╗
│ No │ Nama Mobil      │ Harga Per Hari│
╟────┼─────────────────┼───────────────╢
│ 2  │ Honda Jazz      │ Rp 250,000    │
╚════╧═════════════════╧═══════════════╝
Pilih nomor mobil yang ingin diupdate harganya (atau ketik 'keluar' untuk kembali): 2
Masukkan harga baru untuk Honda Jazz (dalam Rp): dua ratus ribu
Input harga tidak valid.
```

---

### 17. Kembalikan Mobil dari Keranjang Sampah

```
Pilih menu (1-10): 6

Daftar mobil di keranjang sampah:
╔════╤═══════════════╤═════════════╗
│ No │ Nama Mobil    │ Plat Nomor  │
╟────┼───────────────┼─────────────╢
│ 1  │ Nissan Livina │ B 3456 ZX   │
╚════╧═══════════════╧═════════════╝
Pilih mobil yang ingin dikembalikan (nomor) atau ketik 'keluar' untuk ke menu utama: keluar
```

---

### 18. Customer Membatalkan Booking

```
Mobil yang tersedia untuk booking:
...
Pilih nomor mobil yang ingin Anda booking (atau ketik 'kembali' untuk kembali ke menu utama): kembali
```

---

### 19. Admin Logout

```
Pilih menu (1-10): 9
Logout berhasil!
=== Selamat Datang di Sistem Jasa Rental Mobil ===
1. Masuk sebagai Admin
2. Masuk sebagai Pelanggan
Apakah Anda ingin masuk sebagai (1) Admin atau (2) Pelanggan? (ketik 1 atau 2):
```

---

### 20. Customer Keluar

```
=== Menu Utama Customer ===
1. Daftar Mobil
2. Keranjang Sewa
3. Lihat Bukti Sewa
4. Logout
5. Keluar
Silakan pilih menu (1/2/3/4/5): 5
Terima kasih telah menggunakan layanan kami.
```

---

## Catatan & Pengembangan Lanjut

- **Data Tidak Persisten:**  
  Semua data hanya disimpan di RAM. Setelah aplikasi ditutup, data hilang.
- **Validasi Input Lengkap:**  
  NIK, nomor telepon, angka, dan pilihan menu sudah divalidasi.
- **Pengembangan Lebih Lanjut:**  
  - Simpan data ke file (CSV/JSON) atau database.
  - Export bukti sewa ke file.
  - Multi-user/pelanggan.
  - Pengelolaan status armada: servis/maintenance.
  - Filter dan pencarian lebih canggih.

---

**Aplikasi ini dibuat untuk simulasi, tugas, dan pembelajaran sistem rental mobil sederhana.**
