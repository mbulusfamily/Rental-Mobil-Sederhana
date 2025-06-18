################################### SYSTEM CUSTOMER RENTAL MOBIL ############################
from tabulate import tabulate

identitasPelanggan = [] # penyimpanan identitas pelanggan yang akan disewa mobil
keranjangSewaList = [] # penyimpanan keranjang sewa mobil yang akan dibooking
buktiSewa = [] # penyimpanan bukti sewa mobil yang telah dibooking
recycleMobil = [] # penyimpanan mobil yang telah dihapus dan dimasukkan ke keranjang sampah
informasiPelanggan = [] # penyimpanan informasi pelanggan yang akan disewa mobil

list_mobil = [
    {
        "nama": "Toyota Avanza",
        "harga": 200000,
        "jenis": "MPV",
        "bahan_bakar": "Bensin",
        "transmisi": "Manual",
        "plat_nomor": "B 1234 AB",
        "ketersediaan": True
    },
    {
        "nama": "Honda Jazz",
        "harga": 250000,
        "jenis": "Hatchback",
        "bahan_bakar": "Bensin",
        "transmisi": "Matic",
        "plat_nomor": "B 2345 CD",
        "ketersediaan": True
    },
    {
        "nama": "Suzuki Ertiga",
        "harga": 220000,
        "jenis": "MPV",
        "bahan_bakar": "Bensin",
        "transmisi": "Manual",
        "plat_nomor": "B 3456 EF",
        "ketersediaan": True
    },
    {
        "nama": "Daihatsu Xenia",
        "harga": 210000,
        "jenis": "MPV",
        "bahan_bakar": "Bensin",
        "transmisi": "Manual",
        "plat_nomor": "B 4567 GH",
        "ketersediaan": True
    },
    {
        "nama": "Toyota Calya",
        "harga": 180000,
        "jenis": "MPV",
        "bahan_bakar": "Bensin",
        "transmisi": "Manual",
        "plat_nomor": "B 5678 IJ",
        "ketersediaan": True
    },
    {
        "nama": "Mitsubishi Xpander",
        "harga": 300000,
        "jenis": "MPV",
        "bahan_bakar": "Bensin",
        "transmisi": "Matic",
        "plat_nomor": "B 6789 KL",
        "ketersediaan": True
    },
    {
        "nama": "Daihatsu Sigra",
        "harga": 170000,
        "jenis": "MPV",
        "bahan_bakar": "Bensin",
        "transmisi": "Manual",
        "plat_nomor": "B 7890 MN",
        "ketersediaan": True
    },
    {
        "nama": "Toyota Rush",
        "harga": 320000,
        "jenis": "SUV",
        "bahan_bakar": "Solar",
        "transmisi": "Matic",
        "plat_nomor": "B 8901 OP",
        "ketersediaan": True
    },
    {
        "nama": "Honda BR-V",
        "harga": 280000,
        "jenis": "SUV",
        "bahan_bakar": "Solar",
        "transmisi": "Matic",
        "plat_nomor": "B 9012 QR",
        "ketersediaan": True
    },
    {
        "nama": "Suzuki XL7",
        "harga": 350000,
        "jenis": "SUV",
        "bahan_bakar": "Solar",
        "transmisi": "Matic",
        "plat_nomor": "B 0123 ST",
        "ketersediaan": True
    }
]

def tampilkanMobil(): #fungsi untuk menampilkan daftar mobil yang tersedia
    print("\nDaftar Mobil yang Tersedia:")
    header = ["No", "Nama Mobil", "Harga Per Hari", "Jenis Mobil", "Jenis Bahan Bakar", "Tipe Transmisi", "Plat Nomor", "Ketersediaan"]
    table = []
    for i in range(len(listMobil)):
        mobil = listMobil[i]
        table.append([
            i + 1,
            mobil["nama"],
            f"Rp {mobil['harga']:,}",
            mobil["jenis"],
            mobil["bahan_bakar"],
            mobil["transmisi"],
            mobil["plat_nomor"],
            "Tersedia" if mobil["ketersediaan"] else "Tidak Tersedia"
        ])
    print(tabulate(table, headers=header, tablefmt="simple_grid")) # Untuk menampilkan tabel dengan format yang rapi secara berurutan dari 1 sampai set mobil yang tersedia
    while True:    # while loop untuk memastikan apakah user ingin melanjutkan mengisi identitas dan booking mobil atau tidak
        lanjut = input("Lanjut mengisi identitas dan booking mobil? (ya/tidak): ").lower()
        if lanjut == "ya":
            inputIdentitas()
            break
        elif lanjut == "tidak":
            menuUtamaCustomer()
            break
        else:
            print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")

def inputIdentitas(): #fungsi untuk menginput identitas pelanggan
    while True:
        print("\nMasukkan Identitas Anda:")
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        noTelp = input("Nomor Telepon: ")
        NIK = input("NIK: ")
        if not nama or not alamat or not noTelp or not NIK: # Memastikan semua field diisi
            print("Semua field harus diisi. Silakan coba lagi.")
            continue
        if not noTelp.isdigit() or len(noTelp) < 10: # Memastikan nomor telepon hanya berisi angka dan minimal 10 digit
            print("Nomor telepon harus berupa angka dan minimal 10 digit. Silakan coba lagi.")
            continue
        if not NIK.isdigit() or len(NIK) != 16: # Memastikan NIK hanya berisi angka dan memiliki panjang 16 digit
            print("NIK harus berupa angka dan memiliki panjang 16 digit. Silakan coba lagi.")
            continue

        print("\nIdentitas Anda:")
        print(f"Nama: {nama}")
        print(f"Alamat: {alamat}")
        print(f"Nomor Telepon: {noTelp}")
        print(f"NIK: {NIK}")

        konfirmasiIdentitas = input("apakah identitas anda sudah benar? (ya/tidak): ").lower() # Memastikan apakah identitas yang diinput sudah benar
        if konfirmasiIdentitas == "ya": # Jika identitas sudah benar, maka identitas pelanggan akan disimpan di identitasPelanggan
            print("Identitas Anda sudah benar.")
            identitasPelanggan.append({
                "Nama": nama,
                "Alamat": alamat,
                "Nomor Telepon": noTelp,
                "NIK": NIK
            })
            print("Identitas berhasil disimpan.")
            pilihMobil() # Melanjutkan ke pemilihan mobil
        elif konfirmasiIdentitas == "tidak": # Jika identitas tidak benar, maka akan meminta pelanggan untuk menginput identitas kembali
            print("Silakan masukkan identitas Anda kembali.")
            continue
        else: # Jika input tidak valid, maka akan meminta pelanggan untuk menginput identitas kembali
            print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
            continue

def pilihMobil(): #fungsi untuk memilih mobil yang ingin di booking
    print("\nMobil yang tersedia untuk booking:")
    header = ["No", "Nama Mobil", "Harga Per Hari", "Ketersediaan"]
    table = []
    for i, mobil in enumerate(listMobil): # Looping untuk menampilkan daftar mobil yang tersedia
        if mobil["ketersediaan"]:
            table.append([i + 1, mobil["nama"], f"Rp {mobil['harga']:,}", "Tersedia"])
    if not table: # Jika tidak ada mobil yang tersedia, maka akan menampilkan pesan bahwa semua mobil sedang tidak tersedia (telah dibooking semua)
        print("Maaf, semua mobil sedang tidak tersedia.")
        menuUtamaCustomer()
        return
    print(tabulate(table, headers=header, tablefmt="simple_grid")) # Menampilkan tabel dengan format yang rapi secara berurutan dari 1 sampai set mobil yang tersedia
    while True:   # Looping untuk memastikan apakah user ingin memilih mobil yang ingin di booking atau tidak
        pilihNomor = input("Pilih nomor mobil yang ingin Anda booking (atau ketik 'kembali' untuk kembali ke menu utama): ")
        if pilihNomor.lower() == "kembali": # Jika user memilih untuk kembali ke menu utama, maka akan kembali ke menu utama customer
            menuUtamaCustomer()
            return
        if pilihNomor.isdigit() and 1 <= int(pilihNomor) <= len(listMobil): # jika input adalah angka dan berada dalam rentang nomor mobil yang tersedia
            nomorMobil = int(pilihNomor) - 1 
            mobil = listMobil[nomorMobil]
            if mobil["ketersediaan"]: # Jika mobil yang dipilih tersedia
                print("\nDetail Mobil yang Dipilih:")
                print(tabulate([[mobil["nama"], f"Rp {mobil['harga']:,}", mobil["jenis"], mobil["bahan_bakar"], mobil["transmisi"], mobil["plat_nomor"]]],
                             headers=["Nama Mobil", "Harga Per Hari", "Jenis Mobil", "Jenis Bahan Bakar", "Tipe Transmisi", "Plat Nomor"], tablefmt="simple_grid"))
                hariSewa = input("Masukan hari, tanggal sewa (Hari, 00-00-0000): ")
                hariPengembalian = input("Masukan hari, tanggal pengembalian (Hari, 00-00-0000): ")
                durasi = int(input("Masukkan durasi sewa dalam hari: "))
                totalHarga = mobil["harga"] * durasi
                print(f"\nTotal Harga: Rp {totalHarga:,}\n")
                konfirmasiBooking = input("Apakah Anda ingin melanjutkan ke tahap pembayaran? (ya/tidak): ").lower() # Memastikan apakah user ingin melanjutkan ke tahap pembayaran atau tidak
                if konfirmasiBooking == "ya": # Jika user ingin melanjutkan ke tahap pembayaran, maka akan melakukan booking mobil
                    mobil["ketersediaan"] = False
                    print(f"Booking untuk {mobil['nama']} berhasil!")
                    print("Silakan lakukan pembayaran.")
                    while True: 
                        global nama, alamat, noTelp, NIK
                        uangMasuk = []
                        try: # Memastikan input pembayaran adalah angka
                            pembayaran = int(input("Masukkan jumlah uang pembayaran: "))
                        except ValueError:
                            print("Input harus berupa angka.")
                            continue
                        if pembayaran == totalHarga: # Jika pembayaran pas dengan total harga
                            print("Pembayaran berhasil. Terima kasih telah menyewa mobil kami.\nSelamat menikmati perjalanan anda dan tetap berhati-hati dalam berkendara.")
                            buktiSewa.append({
                                "Nama": identitasPelanggan[-1]["Nama"],
                                "Mobil": mobil["nama"],
                                "Harga": totalHarga,
                                "Hari Sewa": hariSewa,
                                "Hari Pengembalian": hariPengembalian,
                                "Durasi": durasi
                            })
                            menuUtamaCustomer()
                        elif pembayaran < totalHarga: # Jika pembayaran kurang dari total harga
                            pembayaranKurang = totalHarga - pembayaran
                            uangMasuk.append(pembayaran)
                            print(f"Pembayaran kurang. Silakan masukkan jumlah uang lagi sebesar Rp {pembayaranKurang:,}.")
                            continue
                        else: # Jika pembayaran lebih dari total harga
                            print(f"Pembayaran lebih. Silakan ambil kembalian anda: Rp {pembayaran - totalHarga:,}. Terima kasih telah menyewa mobil kami.\nSelamat menikmati perjalanan anda dan tetap berhati-hati dalam berkendara.")
                            buktiSewa.append({
                                "Nama": identitasPelanggan[-1]["Nama"],
                                "Mobil": mobil["nama"],
                                "Harga": totalHarga,
                                "Hari Sewa": hariSewa,
                                "Hari Pengembalian": hariPengembalian,
                                "Durasi": durasi
                            })
                            menuUtamaCustomer()
                elif konfirmasiBooking == "tidak": # Jika user tidak ingin melanjutkan ke tahap pembayaran, maka akan kembali ke menu utama customer
                    print("Formulir booking telah dimasukan ke keranjang sewa.\nSilakan lanjutkan ke menu utama untuk melihat keranjang sewa.")
                    keranjangSewaList.append({
                        "Nama": identitasPelanggan[-1]["Nama"],
                        "Mobil": mobil["nama"],
                        "Harga": mobil["harga"],
                        "Hari Sewa": hariSewa,
                        "Hari Pengembalian": hariPengembalian
                    })
                    identitasPelanggan.pop()
                    menuUtamaCustomer()
                    return
                else:
                    print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
            else:
                print("Maaf, mobil ini sudah tidak tersedia.")
        else:
            print("Input tidak valid. Silakan masukkan nomor mobil yang benar.")

def keranjangSewaMenu(): #fungsi untuk menampilkan keranjang sewa (jika tadi sudah booking mobil, lalu tidak melanjutkan pembayaran)
    if not keranjangSewaList: # Jika keranjang sewa kosong, maka akan menampilkan pesan bahwa keranjang sewa kosong
        print("Keranjang sewa Anda kosong.")
        menuUtamaCustomer()
        return
    print("\n=== Keranjang Sewa ===")
    header = ["Nama", "Mobil", "Harga", "Hari Sewa", "Hari Pengembalian"]
    table = []
    for sewa in keranjangSewaList: # Looping untuk menampilkan daftar keranjang sewa
        table.append([sewa["Nama"], sewa["Mobil"], f"Rp {sewa['Harga Per Hari']:,}", sewa["Hari Sewa"], sewa["Hari Pengembalian"]])
    print(tabulate(table, headers=header, tablefmt="simple_grid"))
    while True: # Looping untuk memastikan apakah user ingin melanjutkan ke tahap pembayaran atau tidak
        konfirmasi = input("Melanjutkan pembayaran? (ya/tidak): ").lower()
        if konfirmasi == "ya": # Jika user ingin melanjutkan ke tahap pembayaran, maka akan melakukan pembayaran
            print("\n=== Pembayaran ===")
            totalHarga = sum(sewa["Harga"] for sewa in keranjangSewaList) # Menghitung total harga dari semua mobil yang ada di keranjang sewa
            print(f"Total Harga: Rp {totalHarga:,}")
            while True: #looping untuk mengulangi jika pembayaran kurang dari total harga
                uangMasuk = []
                masukanUang = int(input("Masukkan jumlah uang pembayaran: "))
                if masukanUang < totalHarga: # Jika pembayaran kurang dari total harga  
                    uangMasuk.append(masukanUang) #maka uang yang dimasukkan akan disimpan di list uangMasuk sampai pembayaran pas dengan total harga
                    pembayaranKurang = totalHarga - masukanUang
                    print(f"Pembayaran kurang. Silakan masukkan jumlah yang tepat. Anda masih perlu membayar Rp {pembayaranKurang}.")
                    continue
                elif masukanUang == totalHarga: # Jika pembayaran pas dengan total harga
                    print("Pembayaran pas. Terima kasih telah menyewa mobil kami.\nSelamat menikmati perjalanan anda dan tetap berhati-hati dalam berkendara.")
                    buktiSewa.append({
                        "Nama": keranjangSewaList[0]["Nama"],
                        "Mobil": keranjangSewaList[0]["Mobil"],
                        "Harga": totalHarga,
                        "Hari Sewa": keranjangSewaList[0]["Hari Sewa"],
                        "Hari Pengembalian": keranjangSewaList[0]["Hari Pengembalian"],
                        "Durasi": keranjangSewaList[0]["Durasi"]
                    })
                else: # Jika pembayaran lebih dari total harga maka mendapatkan kembalian
                    kembalian = masukanUang - totalHarga
                    print(f"Pembayaran lebih. Kembalian Anda: Rp {kembalian:,}. Terima kasih telah menyewa mobil kami.\nSelamat menikmati perjalanan anda dan tetap berhati-hati dalam berkendara.")
                    buktiSewa.append({
                        "Nama": keranjangSewaList[0]["Nama"],
                        "Mobil": keranjangSewaList[0]["Mobil"],
                        "Harga": totalHarga,
                        "Hari Sewa": keranjangSewaList[0]["Hari Sewa"],
                        "Hari Pengembalian": keranjangSewaList[0]["Hari Pengembalian"],
                        "Durasi": keranjangSewaList[0]["Durasi"]
                    })
        elif konfirmasi == "tidak": # Jika user tidak ingin melanjutkan ke tahap pembayaran, maka akan kembali ke menu utama customer
            print("Pembayaran dibatalkan.")
            menuUtamaCustomer()
        else: # Jika input tidak valid, maka akan meminta user untuk menginput kembali
            print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
            return konfirmasi

def lihatBuktiSewa(): #fungsi untuk melihat bukti sewa mobil
    if not buktiSewa: # Jika bukti sewa kosong, maka akan menampilkan pesan bahwa belum ada sewa mobil
        print("Anda belum melakukan sewa mobil.")
        menuUtamaCustomer()
        return
    print("\n=== Bukti Sewa ===")
    header = ["Nama", "Mobil", "Harga", "Hari Sewa", "Hari Pengembalian", "Durasi"]
    table = []
    for sewa in buktiSewa:
        table.append([
            sewa["Nama"], sewa["Mobil"], f"Rp {sewa['Harga']:,}", sewa["Hari Sewa"],
            sewa["Hari Pengembalian"], sewa["Durasi"]
        ])
    print(tabulate(table, headers=header, tablefmt="simple_grid")) #menampilkan tabel bukti sewa dengan format yang rapi
    menuUtamaCustomer() #lalu kembali ke menu utama customer

def menuUtamaCustomer(): #fungsi untuk menampilkan menu utama customer
    print("\n=== Menu Utama Customer ===")
    print("1. Daftar Mobil")
    print("2. Keranjang Sewa")
    print("3. Lihat Bukti Sewa")
    print("4. Logout")
    print("5. Keluar")
    pilihan = input("Silakan pilih menu (1/2/3/4/5): ")
    if pilihan == "1": # Jika user memilih untuk melihat daftar mobil, maka akan menampilkan daftar mobil yang tersedia
        tampilkanMobil()
    elif pilihan == "2": # Jika user memilih untuk melihat keranjang sewa, maka akan menampilkan keranjang sewa
        keranjangSewaMenu()
    elif pilihan == "3": # Jika user memilih untuk melihat bukti sewa, maka akan menampilkan bukti sewa mobil
        lihatBuktiSewa()
    elif pilihan == "4": # Jika user memilih untuk logout, maka akan kembali ke menu login
        print("Logout berhasil!")
        login()
    elif pilihan == "5": # Jika user memilih untuk keluar, maka akan keluar dari program
        print("Terima kasih telah menggunakan layanan kami.")
        exit()
    else: # Jika input tidak valid, maka akan meminta user untuk menginput kembali
        print("Pilihan tidak valid. Silakan coba lagi.")
        menuUtamaCustomer()

################################ SYSTEM JASA RENTAL MOBIL ############################
# Gabungkan semua atribut mobil menjadi satu list of dicts bernama listMobil
listMobil = [
    {
        "nama": "Toyota Avanza",
        "harga": 200000,
        "jenis": "MPV",
        "bahan_bakar": "Bensin",
        "transmisi": "Manual",
        "plat_nomor": "B 1234 AB",
        "ketersediaan": True
    },
    {
        "nama": "Honda Jazz",
        "harga": 250000,
        "jenis": "Hatchback",
        "bahan_bakar": "Bensin",
        "transmisi": "Matic",
        "plat_nomor": "B 2345 CD",
        "ketersediaan": True
    },
    {
        "nama": "Suzuki Ertiga",
        "harga": 220000,
        "jenis": "MPV",
        "bahan_bakar": "Bensin",
        "transmisi": "Manual",
        "plat_nomor": "B 3456 EF",
        "ketersediaan": True
    },
    {
        "nama": "Daihatsu Xenia",
        "harga": 210000,
        "jenis": "MPV",
        "bahan_bakar": "Bensin",
        "transmisi": "Manual",
        "plat_nomor": "B 4567 GH",
        "ketersediaan": True
    },
    {
        "nama": "Toyota Calya",
        "harga": 180000,
        "jenis": "MPV",
        "bahan_bakar": "Bensin",
        "transmisi": "Manual",
        "plat_nomor": "B 5678 IJ",
        "ketersediaan": True
    },
    {
        "nama": "Mitsubishi Xpander",
        "harga": 300000,
        "jenis": "MPV",
        "bahan_bakar": "Bensin",
        "transmisi": "Matic",
        "plat_nomor": "B 6789 KL",
        "ketersediaan": True
    },
    {
        "nama": "Daihatsu Sigra",
        "harga": 170000,
        "jenis": "MPV",
        "bahan_bakar": "Bensin",
        "transmisi": "Manual",
        "plat_nomor": "B 7890 MN",
        "ketersediaan": True
    },
    {
        "nama": "Toyota Rush",
        "harga": 320000,
        "jenis": "SUV",
        "bahan_bakar": "Solar",
        "transmisi": "Matic",
        "plat_nomor": "B 8901 OP",
        "ketersediaan": True
    },
    {
        "nama": "Honda BR-V",
        "harga": 280000,
        "jenis": "SUV",
        "bahan_bakar": "Solar",
        "transmisi": "Matic",
        "plat_nomor": "B 9012 QR",
        "ketersediaan": True
    },
    {
        "nama": "Suzuki XL7",
        "harga": 350000,
        "jenis": "SUV",
        "bahan_bakar": "Solar",
        "transmisi": "Matic",
        "plat_nomor": "B 0123 ST",
        "ketersediaan": True
    }
]

def tableDaftarMobilJasa(): #fungsi untuk menampilkan daftar mobil yang tersedia dan sama seperti fungsi tampilkanMobil pada sistem customer
    header = ["No", "Nama Mobil", "Harga Per Hari", "Jenis Mobil", "Jenis Bahan Bakar", "Tipe Transmisi", "Plat Nomor", "Ketersediaan"]
    table = [] # list untuk menyimpan data mobil yang akan ditampilkan dalam tabel
    for i, mobil in enumerate(listMobil): # Looping untuk menampilkan daftar mobil yang tersedia dan tidak tersedia
        table.append([
            i + 1,
            mobil["nama"],
            f"Rp {mobil['harga']:,}",
            mobil["jenis"],
            mobil["bahan_bakar"],
            mobil["transmisi"],
            mobil["plat_nomor"],
            "Tersedia" if mobil["ketersediaan"] else "Tidak Tersedia"
        ])
    print(tabulate(table, headers=header, tablefmt="simple_grid")) # Menampilkan tabel dengan format yang rapi secara berurutan dari 1 sampai set mobil yang tersedia
    menuUtamaJasa()

def tambahMobil(): #fungsi untuk menambahkan mobil baru ke daftar mobil yang tersedia
    while True: # looping untuk memastikan apakah user ingin menambahkan mobil baru atau tidak
        if input("Apakah Anda ingin menambahkan mobil baru? (ya/tidak): ").lower() != "ya": # Jika user tidak ingin menambahkan mobil baru, maka akan kembali ke menu utama jasa dan jika ya maka akan menampilkan daftar mobil yang tersedia
            print("Penambahan mobil dibatalkan.")
            menuUtamaJasa()
            return
        header = ["No", "Nama Mobil", "Harga Per Hari", "Jenis Mobil", "Jenis Bahan Bakar", "Tipe Transmisi", "Plat Nomor", "Ketersediaan"]
        table = []
        for i, mobil in enumerate(listMobil):
            table.append([
                i + 1,
                mobil["nama"],
                f"Rp {mobil['harga']:,}",
                mobil["jenis"],
                mobil["bahan_bakar"],
                mobil["transmisi"],
                mobil["plat_nomor"],
                "Tersedia" if mobil["ketersediaan"] else "Tidak Tersedia"
            ])
        print(tabulate(table, headers=header, tablefmt="simple_grid")) # Menampilkan tabel dengan format yang rapi secara berurutan dari 1 sampai set mobil yang tersedia

        nama = input("Masukkan nama mobil: ") 
        harga = int(input("Masukkan harga per hari (dalam Rp): "))
        jenis = input("Masukkan jenis mobil: ")
        bahan_bakar = input("Masukkan jenis bahan bakar: ")
        transmisi = input("Masukkan tipe transmisi: ")
        plat_nomor = input("Masukkan plat nomor: ") # memasukan semua data mobil yang akan ditambahkan
        
        print("Apakah anda yakin ingin menambahkan mobil ini?")
        print(tabulate([[nama, f"Rp {harga:,}", jenis, bahan_bakar, transmisi, plat_nomor]], headers=["Nama Mobil", "Harga Per Hari", "Jenis Mobil", "Jenis Bahan Bakar", "Tipe Transmisi", "Plat Nomor"], tablefmt="simple_grid"))
        if input("Ketik 'ya' untuk mengkonfirmasi: ").lower() == "ya": # validasi untuk memastikan apakah user yakin ingin menambahkan mobil baru, jika ya maka akan menambahkan mobil baru ke daftar mobil yang tersedia
            listMobil.append({
                "nama": nama,
                "harga": harga,
                "jenis": jenis,
                "bahan_bakar": bahan_bakar,
                "transmisi": transmisi,
                "plat_nomor": plat_nomor,
                "ketersediaan": True
            })
            print(f"Mobil {nama} telah ditambahkan.")
            header = ["No", "Nama Mobil", "Harga Per Hari", "Jenis Mobil", "Jenis Bahan Bakar", "Tipe Transmisi", "Plat Nomor", "Ketersediaan"]
            table = []
            for i, mobil in enumerate(listMobil):
                table.append([
                    i + 1,
                    mobil["nama"],
                    f"Rp {mobil['harga']:,}",
                    mobil["jenis"],
                    mobil["bahan_bakar"],
                    mobil["transmisi"],
                    mobil["plat_nomor"],
                    "Tersedia" if mobil["ketersediaan"] else "Tidak Tersedia"
                ])
            print(tabulate(table, headers=header, tablefmt="simple_grid")) # Menampilkan tabel dengan format yang rapi secara berurutan dari 1 sampai set mobil yang tersedia
            menuUtamaJasa() #kembali ke menu utama jasa setelah menambahkan mobil baru
        else: # Jika user tidak yakin ingin menambahkan mobil baru, maka akan membatalkan penambahan mobil baru dan kembali ke menu tambah mobil dan kembali ke awal fungsi tambahMobil
            print("Penambahan mobil dibatalkan.")
            tambahMobil()

def hapusMobil(): # fungsi untuk menghapus mobil dari daftar mobil yang tersedia
    header = ["No", "Nama Mobil", "Harga Per Hari", "Jenis Mobil", "Jenis Bahan Bakar", "Tipe Transmisi", "Plat Nomor", "Ketersediaan"]
    table = []
    for i, mobil in enumerate(listMobil):
        table.append([
            i + 1,
            mobil["nama"],
            f"Rp {mobil['harga']:,}",
            mobil["jenis"],
            mobil["bahan_bakar"],
            mobil["transmisi"],
            mobil["plat_nomor"],
            "Tersedia" if mobil["ketersediaan"] else "Tidak Tersedia"
        ])
    print(tabulate(table, headers=header, tablefmt="simple_grid")) # menampilkan tabel dengan format yang rapi secara berurutan dari 1 sampai set mobil yang tersedia
    pilihan = input("Pilih mobil yang ingin dihapus (nomor) atau ketik 'keluar' untuk ke menu utama: ")
    if pilihan.lower() == "keluar": # jika user memilih untuk keluar, maka akan kembali ke menu utama jasa
        menuUtamaJasa()
        return
    try: # validasi untuk memastikan input adalah angka dan berada dalam rentang nomor mobil yang tersedia
        pilihan = int(pilihan) - 1
        if 0 <= pilihan < len(listMobil): # jika input adalah angka dan berada dalam rentang nomor mobil yang tersedia (1 => kesediaan terakhir)
            mobil = listMobil[pilihan]
            if input(f"Apakah Anda yakin ingin menghapus mobil {mobil['nama']}? (ya/tidak): ").lower() == "ya":
                print(f"Mobil {mobil['nama']} telah dihapus.")
                recycleMobil.append(mobil.copy()) # menyimpan mobil yang dihapus ke keranjang sampah kepada list recycleMobil
                del listMobil[pilihan] # menghapus data mobil yang dipilih dari daftar mobil yang tersedia
                print("Mobil telah dihapus dan dimasukkan ke keranjang sampah.")
                menuUtamaJasa()
            else: # jika user tidak yakin ingin menghapus mobil, maka akan membatalkan penghapusan mobil dan kembali ke menu utama jasa
                print("Penghapusan dibatalkan.")
                menuUtamaJasa()
        else: # jika input tidak valid, maka akan menampilkan pesan bahwa pilihan tidak valid
            print("Pilihan tidak valid.")
            return
    except ValueError: # jika input bukan angka, maka akan menampilkan pesan bahwa input tidak valid dan akan kembali ke menu tambah mobil
        print("Input tidak valid.")
    menuUtamaJasa()

def kembalikanMobil(): # fungsi untuk mengembalikan mobil yang telah dihapus dari daftar mobil yang tersedia
    if not recycleMobil: # jika keranjang sampah kosong, maka akan menampilkan pesan bahwa tidak ada mobil yang tersedia di keranjang sampah
        print("Tidak ada mobil yang tersedia di keranjang sampah.")
        return

    print("Daftar mobil di keranjang sampah:")
    for i, mobil in enumerate(recycleMobil): # menampilkan daftar mobil yang ada di keranjang sampah
        print(tabulate([[i + 1, mobil['nama'], mobil['plat_nomor']]], headers=["No", "Nama Mobil", "Plat Nomor"], tablefmt="simple_grid"))

    pilihan = input("Pilih mobil yang ingin dikembalikan (nomor) atau ketik 'keluar' untuk ke menu utama: ")
    if pilihan.lower() == "keluar": # jika user memilih untuk keluar, maka akan kembali ke menu utama jasa
        menuUtamaJasa()
        return
    try: # validasi untuk memastikan input adalah angka dan berada dalam rentang nomor mobil yang tersedia di keranjang sampah
        pilihan = int(pilihan) - 1
        if 0 <= pilihan < len(recycleMobil): # jika input adalah angka dan berada dalam rentang nomor mobil yang tersedia di keranjang sampah
            mobil = recycleMobil.pop(pilihan)
            listMobil.append(mobil)
            print(f"Mobil {mobil['nama']} telah dikembalikan.")
            menuUtamaJasa()
        else: # jika input bukan angka atau berada di luar rentang nomor mobil yang tersedia di keranjang sampah, maka akan menampilkan pesan bahwa pilihan tidak valid dan akan kembali ke menu tambah mobil
            print("Pilihan tidak valid.")
            return pilihan
    except ValueError: # jika input bukan angka, maka akan menampilkan pesan bahwa input tidak valid.
        print("Input tidak valid.")
    menuUtamaJasa()

def kesediaanMobil(): # fungsi untuk menampilkan daftar mobil yang tersedia
    if not listMobil: # jika daftar mobil kosong, maka akan menampilkan pesan bahwa tidak ada mobil yang tersedia
        print("Tidak ada mobil yang tersedia.")
        return
    print("Daftar Mobil Tersedia:")
    header = ["No", "Nama Mobil", "Harga Per Hari", "Jenis Mobil", "Jenis Bahan Bakar", "Tipe Transmisi", "Plat Nomor"]
    table = []
    for i, mobil in enumerate(listMobil):
        if mobil["ketersediaan"]:
            table.append([
                i + 1,
                mobil["nama"],
                f"Rp {mobil['harga']:,}",
                mobil["jenis"],
                mobil["bahan_bakar"],
                mobil["transmisi"],
                mobil["plat_nomor"]
            ])
    print(tabulate(table, headers=header, tablefmt="simple_grid")) # Menampilkan tabel dengan format yang rapi secara berurutan dari 1 sampai set mobil yang tersedia
    menuUtamaJasa() # kembali ke menu utama jasa setelah menampilkan daftar mobil yang tersedia

def updateHargaMobil(): # fungsi untuk mengupdate harga mobil yang tersedia
    header = ["No", "Nama Mobil", "Harga Per Hari"]
    table = []
    for i in range(len(listMobil)):
        table.append([i + 1, listMobil[i]["nama"], f"Rp {listMobil[i]['harga']:,}"])
    print(tabulate(table, headers=header, tablefmt="simple_grid")) # Menampilkan tabel dengan format yang rapi secara berurutan dari 1 sampai set mobil yang tersedia
    pilihan = input("Pilih nomor mobil yang ingin diupdate harganya (atau ketik 'keluar' untuk kembali): ")
    if pilihan.lower() == "keluar": # jika user memilih untuk keluar, maka akan kembali ke menu utama jasa
        menuUtamaJasa()
        return
    try: # validasi untuk memastikan input adalah angka dan berada dalam rentang nomor mobil yang tersedia
        idx = int(pilihan) - 1
        if 0 <= idx < len(listMobil): # jika input adalah angka dan berada dalam rentang nomor mobil yang tersedia
            harga_baru = input(f"Masukkan harga baru untuk {listMobil[idx]['nama']} (dalam Rp): ")
            if harga_baru.isdigit(): # jika input adalah angka, maka akan mengupdate harga mobil yang dipilih
                listMobil[idx]['harga'] = int(harga_baru)
                if input("apakah anda yakin ingin mengupdate harga mobil ini? (ya/tidak): ").lower() == "ya": # validasi untuk memastikan apakah user yakin ingin mengupdate harga mobil ini?
                    print(f"Harga mobil {listMobil[idx]['nama']} berhasil diupdate menjadi Rp {listMobil[idx]['harga']:,}.")
                    menuUtamaJasa() # kembali ke menu utama jasa setelah mengupdate harga mobil
                else:
                    print("Pengubahan dibatalkan.")
                    return
            else:
                print("Input harga tidak valid.")
                return
        else: # jika input bukan angka atau berada di luar rentang nomor mobil yang tersedia, maka akan menampilkan pesan bahwa pilihan tidak valid. kembali ke menu utama jasa
            print("Pilihan tidak valid.")
            return
    except ValueError: # jika input bukan angka, maka akan menampilkan pesan bahwa input tidak valid. kembali ke menu utama jasa
        print("Input tidak valid.")
        return # kembali ke menu utama jasa

def cariMobil(): # fungsi untuk mencari mobil berdasarkan nama
    keyword = input("Masukkan nama mobil yang ingin dicari: ").lower() 
    header = ["No", "Nama Mobil", "Harga Per Hari", "Jenis Mobil", "Jenis Bahan Bakar", "Tipe Transmisi", "Plat Nomor", "Ketersediaan"]
    table = [] # list untuk menyimpan data mobil yang akan ditampilkan dalam tabel
    found = False
    for i in range(len(listMobil)):
        if keyword in listMobil[i]["nama"].lower(): # jika nama mobil yang dicari ada dalam daftar mobil yang tersedia (walaupun tidak persis sama ex: "Toyota" akan menemukan "Toyota Avanza")
            table.append([
                i + 1,
                listMobil[i]["nama"],
                f"Rp {listMobil[i]['harga']:,}",
                listMobil[i]["jenis"],
                listMobil[i]["bahan_bakar"],
                listMobil[i]["transmisi"],
                listMobil[i]["plat_nomor"],
                "Tersedia" if listMobil[i]["ketersediaan"] else "Tidak Tersedia"
            ]) # menambahkan data mobil yang ditemukan ke dalam tabel
            found = True # menandakan bahwa mobil ditemukan
    if found:
        print(tabulate(table, headers=header, tablefmt="simple_grid")) # Menampilkan tabel mobil yang ditemukan dengan format yang rapi
    else: # jika tidak ada mobil yang ditemukan, maka akan menampilkan pesan bahwa mobil tidak ditemukan
        print("Mobil tidak ditemukan.")
    menuUtamaJasa()

def menuUtamaJasa():
    while True:
        print("\n=== Menu Rental Mobil ===")
        print("1. Daftar Mobil")
        print("2. Cari Mobil")
        print("3. Update Harga Mobil")
        print("4. Tambah Mobil")
        print("5. Hapus Mobil")
        print("6. Kembalikan mobil dari keranjang sampah")
        print("7. Informasi Pelanggan")
        print("8. Kesediaan Mobil")
        print("9. Logout")
        print("10. Keluar\n")
        pilihan = input("Pilih menu (1-10): ")
        if pilihan == '1':
            tableDaftarMobilJasa()
        elif pilihan == '2':
            cariMobil()
        elif pilihan == '3':
            updateHargaMobil()
        elif pilihan == '4':
            tambahMobil()
        elif pilihan == '5':
            hapusMobil()
        elif pilihan == '6':
            kembalikanMobil()
        elif pilihan == '7':
            print("Informasi Pelanggan:")
            if not identitasPelanggan: # Jika tidak ada informasi pelanggan yang tersedia, maka akan menampilkan pesan bahwa tidak ada informasi pelanggan yang tersedia
                print("Tidak ada informasi pelanggan yang tersedia.")
                return
            for pelanggan in identitasPelanggan: # Looping untuk menampilkan informasi pelanggan yang telah diinput
                print(f"Nama: {pelanggan['Nama']}, Alamat: {pelanggan['Alamat']}, Nomor Telepon: {pelanggan['Nomor Telepon']}, NIK: {pelanggan['NIK']}")
        elif pilihan == '8':
            if not listMobil: # Jika tidak ada mobil yang tersedia, maka akan menampilkan pesan bahwa tidak ada mobil yang tersedia
                print("Tidak ada mobil yang tersedia.")
            else: # Jika ada mobil yang tersedia, maka akan menampilkan daftar mobil yang tersedia
                kesediaanMobil()
        elif pilihan == '9':
            print("Logout berhasil!")
            login()
        elif pilihan == '10':
            print("Terima kasih telah menggunakan layanan kami!")
            exit()
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

def login():
    print("=== Selamat Datang di Sistem Jasa Rental Mobil ===")
    print("1. Masuk sebagai Admin")
    print("2. Masuk sebagai Pelanggan")
    pilihUser = input("Apakah Anda ingin masuk sebagai (1) Admin atau (2) Pelanggan? (ketik 1 atau 2): ")
    if pilihUser == '1':
        while True:
            UserName = input("Masukkan username admin: ")
            Password = input("Masukkan password admin: ")
            if UserName == "SukmaBagusYTTTA" and Password == "Sukma123":
                print("Login berhasil!")
                menuUtamaJasa()
            elif UserName != "SukmaBagusYTTTA" or Password != "Sukma123":
                print("Username atau password salah, silakan coba lagi.")
                continue
            elif UserName == "SukmaBagusYTTTA" and Password != "Sukma123":
                print("Password salah, silakan coba lagi.")
                continue
            elif UserName != "SukmaBagusYTTTA" and Password == "Sukma123":
                print("Username salah, silakan coba lagi.")
                continue
            else:
                print("Login gagal, silakan coba lagi.")
                continue
    elif pilihUser == '2':
        menuUtamaCustomer()
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
        login()

if __name__ == "__main__":
    login()
