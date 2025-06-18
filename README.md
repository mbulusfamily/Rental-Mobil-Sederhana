# Sistem Customer Rental Mobil Sederhana (Console Python)

Aplikasi ini adalah program simulasi rental mobil berbasis terminal menggunakan Python. Sistem ini mendukung dua peran utama (**Admin** dan **Customer**) untuk mengelola armada mobil, melakukan booking, pembayaran, serta administrasi pelanggan secara sederhana. Tampilan tabel menggunakan library [tabulate](https://pypi.org/project/tabulate/) agar output lebih rapi.

---

## Daftar Isi

- [Fitur Aplikasi](#fitur-aplikasi)
- [Struktur Data](#struktur-data)
- [Penjelasan Fungsi](#penjelasan-fungsi)
- [Alur Program](#alur-program)
- [Instalasi & Cara Menjalankan](#instalasi--cara-menjalankan)
- [Contoh Penggunaan](#contoh-penggunaan)
- [Catatan & Pengembangan Lanjut](#catatan--pengembangan-lanjut)

---

## Fitur Aplikasi

### Role & Login
- **Admin**
  - Login dengan username dan password.
  - Mengelola data mobil (tambah, hapus, update harga, recycle bin, cari, cek ketersediaan).
  - Melihat data pelanggan.
- **Customer**
  - Dapat melihat mobil, booking, mengisi identitas, membayar, cek keranjang sewa, dan melihat bukti sewa.

### Manajemen Mobil (Admin)
- Melihat daftar semua mobil (tersedia/tidak).
- Menambah mobil baru.
- Menghapus mobil (soft delete ke recycle bin).
- Mengembalikan mobil dari recycle bin.
- Update harga per hari.
- Cari mobil berdasarkan nama.
- Cek ketersediaan mobil saja.

### Proses Sewa (Customer)
- Lihat daftar mobil tersedia.
- Input identitas (validasi nama, alamat, nomor telepon, NIK).
- Pilih mobil, tanggal sewa, durasi, booking.
- Pembayaran: validasi kurang, pas, lebih.
- Jika batal bayar, booking masuk keranjang sewa.
- Lihat dan bayar keranjang sewa.
- Cek bukti sewa (history).

### Validasi & Antarmuka
- Validasi nomor telepon & NIK.
- Tabel rapi via `tabulate`.
- Menu interaktif, konfirmasi setiap proses penting.

---

## Struktur Data

- **listMobil**: List of dict, data master armada mobil.
- **identitasPelanggan**: List of dict, identitas pelanggan yang booking.
- **keranjangSewaList**: List of dict, booking yang belum dibayar.
- **buktiSewa**: List of dict, booking yang sudah dibayar.
- **recycleMobil**: List of dict, mobil yang dihapus (keranjang sampah).

---

## Penjelasan Fungsi

### Fungsi Customer

- **tampilkanMobil()**: Tabel semua mobil, lanjut ke input identitas & booking.
- **inputIdentitas()**: Input data diri dengan validasi.
- **pilihMobil()**: Pilih mobil, tentukan tanggal, durasi, proses booking & pembayaran.
- **keranjangSewaMenu()**: Tampilkan keranjang booking yang belum dibayar, proses pembayaran.
- **lihatBuktiSewa()**: Cek history/bukti sewa yang sudah dilakukan.
- **menuUtamaCustomer()**: Menu utama customer.

### Fungsi Admin

- **tableDaftarMobilJasa()**: Lihat semua mobil (tersedia/tidak).
- **tambahMobil()**: Tambahkan mobil baru.
- **hapusMobil()**: Soft-delete mobil (masuk recycle bin).
- **kembalikanMobil()**: Restore mobil dari recycle bin.
- **kesediaanMobil()**: Tampilkan hanya mobil yang tersedia.
- **updateHargaMobil()**: Update harga sewa.
- **cariMobil()**: Cari mobil berdasarkan nama.
- **menuUtamaJasa()**: Menu utama admin.

### Fungsi Umum

- **login()**: Menu awal login sebagai admin/customer.
- **if __name__ == "__main__"**: Entry point aplikasi.

---

## Alur Program

1. **Login**  
   - Pilih peran (admin/customer)
   - Admin: Username `SukmaBagusYTTTA`, Password `Sukma123`
   - Customer: Langsung masuk

2. **Admin**
   - Daftar mobil, tambah, hapus, update harga, recycle bin, cari, cek ketersediaan, lihat pelanggan, logout, keluar

3. **Customer**
   - Lihat mobil → input identitas → pilih mobil → booking & bayar atau keranjang sewa
   - Lihat keranjang sewa & bayar
   - Lihat bukti sewa
   - Logout, keluar

---

## Instalasi & Cara Menjalankan

1. **Install library tabulate**
   ```
   pip install tabulate
   ```

2. **Simpan kode ke `main.py`**  
   (copy seluruh kode program ke file `main.py`)

3. **Jalankan aplikasi**
   ```
   python main.py
   ```

---

## Contoh Penggunaan

### 1. Login Customer

```
=== Selamat Datang di Sistem Jasa Rental Mobil ===
1. Masuk sebagai Admin
2. Masuk sebagai Pelanggan
Apakah Anda ingin masuk sebagai (1) Admin atau (2) Pelanggan? (ketik 1 atau 2): 2
```

---

### 2. Daftar Mobil (Customer)

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
Lanjut mengisi identitas dan booking mobil? (ya/tidak): ya
```

---

### 3. Proses Booking & Pembayaran

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

### 4. Keranjang Sewa (Jika Booking Ditunda)

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

### 5. Lihat Bukti Sewa

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

### 6. Login Admin

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

### 7. Tambah Mobil (Admin)

```
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
Pilih mobil yang ingin dihapus (nomor) atau ketik 'keluar' untuk ke menu utama: 10
Apakah Anda yakin ingin menghapus mobil Nissan Livina? (ya/tidak): ya
Mobil Nissan Livina telah dihapus.
Mobil telah dihapus dan dimasukkan ke keranjang sampah.

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

### 12. Validasi Identitas Customer: Error

```
Masukkan Identitas Anda:
Nama: 
Alamat: Jl. Kenangan
Nomor Telepon: 0812345
NIK: 12345678

Semua field harus diisi. Silakan coba lagi.
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

### 15. Admin Logout & Customer Keluar

```
Pilih menu (1-10): 9
Logout berhasil!
=== Selamat Datang di Sistem Jasa Rental Mobil ===
1. Masuk sebagai Admin
2. Masuk sebagai Pelanggan
Apakah Anda ingin masuk sebagai (1) Admin atau (2) Pelanggan? (ketik 1 atau 2):

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

- **Data hanya di memori (RAM), setelah aplikasi ditutup data hilang.**
- **Validasi input sudah lengkap** (NIK, no telepon, pemilihan menu).
- **Pengembangan lebih lanjut:**  
  - Simpan data ke file/database
  - Export bukti sewa ke file
  - Multi-user login
  - Fitur pengelolaan status armada (servis, maintenance, dsb)
  - Filter & pencarian lebih canggih

---

**Aplikasi ini dibuat untuk simulasi, tugas kuliah, dan pembelajaran sistem rental mobil sederhana.**
