# Rental Mobil Sederhana

A **simple car rental system** written in Python using the `tabulate` library for pretty terminal tables. This project provides two main interfaces:
- **Admin (Rental Service/Jasa)**: Manage car data, prices, availability, and view customer info.
- **Customer**: Browse, book, and pay for car rentals, view booking cart and rental receipts.

---

## Features and Explanations

### Customer Features

| Feature                | Description                                                                                      | Example / Notes                                                   |
|------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| **View Available Cars**| Shows a table of all cars with status "Available" or "Not Available".                           | User sees car brand, price, type, fuel, transmission, plate, etc. |
| **Input Identity**     | Users must fill in Name, Address, Phone Number (min 10 digits), and valid 16-digit NIK.         | Input is validated for completeness and correctness.              |
| **Book a Car**         | Select a car, enter rental and return date, input rental duration.                              | System calculates total price.                                    |
| **Flexible Payment**   | Option to pay directly after booking or postpone and move order to cart.                        | Useful if user doesn't have enough cash or wants to pay later.    |
| **Cart Management**    | Orders not paid go to "cart". User can pay for all at once from cart.                           | Cart can contain multiple bookings.                               |
| **View Rental Receipt**| Shows proof of completed (paid) rentals, including all details.                                 | Tabulated for clarity.                                            |
| **Input Validation**   | All user inputs are checked. Invalid entries prompt re-input.                                   | E.g. Phone/NIK must be digits.                                    |
| **Logout**             | Exit to login screen.                                                                           |                                                                 |
| **Exit**               | Closes the program.                                                                             |                                                                 |

#### More Customer Flow Examples

1. **Book & Pay Immediately**
    - Select car → Fill identity → Pick car → Set dates → Confirm booking → Pay
2. **Book & Pay Later**
    - Select car → Fill identity → Pick car → Set dates → Confirm booking → Choose "No" at payment
    - Order moves to cart
    - From main menu, select "Keranjang Sewa" and finish payment later

---

### Admin Features

| Feature                   | Description                                                                                   | Example / Notes                                             |
|---------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| **View All Cars**         | Shows all cars, available or not, in a formatted table.                                       | Admin sees everything a customer sees, plus unavailable.    |
| **Search Cars**           | Search by name (partial/full match, case-insensitive).                                        | Typing "toyota" matches all Toyota cars.                    |
| **Update Car Price**      | Select car, enter new price, confirm.                                                         | Price is shown and changed instantly.                       |
| **Add New Car**           | Fill in car details: name, price, type, fuel, transmission, plate number.                     | Confirmation required before adding.                        |
| **Delete Car**            | Remove a car from active list; goes to "recycle bin" (not deleted permanently).               | Can be restored anytime.                                    |
| **Restore Car**           | Return a deleted car from "recycle bin" back to active list.                                  | Ensures accidental deletion is not fatal.                   |
| **View Only Available Cars**| Filter and show only cars with "available" status.                                          | Quick overview for rental stock.                            |
| **View Customer Info**    | See all identities that have booked at least once.                                            | Each entry: name, address, phone, NIK.                      |
| **Logout**                | Return to login screen.                                                                       |                                                           |
| **Exit**                  | Closes the program.                                                                           |                                                           |

#### More Admin Flow Examples

- **Add Car**: Add a new brand or type when the rental business expands.
- **Delete/Restore Car**: Temporarily remove a car for maintenance, then restore it when ready.
- **Update Price**: Adjust prices during high/low season.
- **View Customer Data**: Check identities for reporting or contacting renters.

---

## Data Structures

| Name                  | Type   | Usage                                                    |
|-----------------------|--------|----------------------------------------------------------|
| `listMobil`           | list   | List of all car dictionaries                             |
| `identitasPelanggan`  | list   | Stores dicts of each customer identity                   |
| `keranjangSewaList`   | list   | Stores dicts of pending bookings (cart)                  |
| `buktiSewa`           | list   | Stores dicts of completed/payed bookings                 |
| `recycleMobil`        | list   | Stores dicts of deleted cars (can be restored)           |

---

## Example Usage

### Customer

#### Book & Pay in Full

```
=== Menu Utama Customer ===
1. Daftar Mobil
2. Keranjang Sewa
3. Lihat Bukti Sewa
4. Logout
5. Keluar
Silakan pilih menu (1/2/3/4/5): 1

Daftar Mobil yang Tersedia:
...

Lanjut mengisi identitas dan booking mobil? (ya/tidak): ya

Masukkan Identitas Anda:
Nama: John
Alamat: Jl. Kenanga
Nomor Telepon: 081212345678
NIK: 1234567890123456

...

Pilih nomor mobil yang ingin Anda booking: 1
Masukan hari, tanggal sewa (Hari, 00-00-0000): Selasa, 16-07-2025
Masukan hari, tanggal pengembalian (Hari, 19-07-2025): Jumat, 19-07-2025
Masukkan durasi sewa dalam hari: 3

Total Harga: Rp 600,000

Apakah Anda ingin melanjutkan ke tahap pembayaran? (ya/tidak): ya
Masukkan jumlah uang pembayaran: 650000

Pembayaran lebih. Silakan ambil kembalian anda: Rp 50,000.
Terima kasih telah menyewa mobil kami.
Selamat menikmati perjalanan anda dan tetap berhati-hati dalam berkendara.
```

#### Book Now, Pay Later (Cart)

```
Apakah Anda ingin melanjutkan ke tahap pembayaran? (ya/tidak): tidak
Formulir booking telah dimasukan ke keranjang sewa.
Silakan lanjutkan ke menu utama untuk melihat keranjang sewa.
```

#### Pay for All in Cart

```
=== Keranjang Sewa ===
+--------+--------------+-----------+---------------------+------------------------+
| Nama   | Mobil        | Harga     | Hari Sewa           | Hari Pengembalian      |
+--------+--------------+-----------+---------------------+------------------------+
| John   | Toyota Avanza| Rp 200000 | Selasa, 16-07-2025  | Jumat, 19-07-2025      |
+--------+--------------+-----------+---------------------+------------------------+

Melanjutkan pembayaran? (ya/tidak): ya
Total Harga: Rp 200,000
Masukkan jumlah uang pembayaran: 200000
Pembayaran pas. Terima kasih telah menyewa mobil kami.
Selamat menikmati perjalanan anda dan tetap berhati-hati dalam berkendara.
```

#### View Rental Receipt

```
=== Bukti Sewa ===
+--------+--------------+-----------+---------------------+------------------------+--------+
| Nama   | Mobil        | Harga     | Hari Sewa           | Hari Pengembalian      | Durasi |
+--------+--------------+-----------+---------------------+------------------------+--------+
| John   | Toyota Avanza| 600000    | Selasa, 16-07-2025  | Jumat, 19-07-2025      | 3      |
+--------+--------------+-----------+---------------------+------------------------+--------+
```

---

### Admin

#### Add Car

```
Apakah Anda ingin menambahkan mobil baru? (ya/tidak): ya
Masukkan nama mobil: Nissan Livina
Masukkan harga per hari (dalam Rp): 250000
Masukkan jenis mobil: MPV
Masukkan jenis bahan bakar: Bensin
Masukkan tipe transmisi: Matic
Masukkan plat nomor: B 1123 XY
Ketik 'ya' untuk mengkonfirmasi: ya
Mobil Nissan Livina telah ditambahkan.
```

#### Delete and Restore Car

```
Pilih mobil yang ingin dihapus (nomor): 3
Apakah Anda yakin ingin menghapus mobil Suzuki Ertiga? (ya/tidak): ya
Mobil Suzuki Ertiga telah dihapus dan dimasukkan ke keranjang sampah.

Daftar mobil di keranjang sampah:
+----+---------------+--------------+
| No | Nama Mobil    | Plat Nomor   |
+----+---------------+--------------+
| 1  | Suzuki Ertiga | B 3456 EF    |
+----+---------------+--------------+
Pilih mobil yang ingin dikembalikan (nomor): 1
Mobil Suzuki Ertiga telah dikembalikan.
```

#### Update Price

```
Pilih nomor mobil yang ingin diupdate harganya (atau ketik 'keluar' untuk kembali): 2
Masukkan harga baru untuk Honda Jazz (dalam Rp): 300000
apakah anda yakin ingin mengupdate harga mobil ini? (ya/tidak): ya
Harga mobil Honda Jazz berhasil diupdate menjadi Rp 300,000.
```

#### View Customer Data

```
Informasi Pelanggan:
Nama: John, Alamat: Jl. Kenanga, Nomor Telepon: 081212345678, NIK: 1234567890123456
Nama: Alice, Alamat: Jl. Melati, Nomor Telepon: 085612345678, NIK: 6543210987654321
```

---

## Requirements

- Python 3.x
- `tabulate` library

Install tabulate if needed:
```bash
pip install tabulate
```

---

## Running the Program

```bash
python3 rental_mobil.py
```

---

## Customization

- Change admin username/password in the `login()` function.
- Add/modify cars in the `listMobil` variable.
- Modify/add features as needed!

---

## License

MIT License.  
Feel free to use, modify, or distribute for educational purposes.

---
