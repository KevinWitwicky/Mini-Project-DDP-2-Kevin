# Sistem Tiket Pesawat

# Data
akun = {
    "admin": {"sandi": "admin123", "peran": "admin"},
    "kevin": {"sandi": "kevin123", "peran": "pelanggan"}
}

jadwal = {
    "GA101": {"dari": "JKT", "ke": "DPS", "tanggal": "2025-10-01", "harga": 750000},
    "JT202": {"dari": "SUB", "ke": "JKT", "tanggal": "2025-10-05", "harga": 600000}
}

tiket_saya = {}
id_pesanan_terakhir = 0
pengguna = {"nama": "", "peran": ""}

# Fungsi Utama
def masuk():
    global pengguna
    print("\n--- MASUK SISTEM ---")
    nama = input("Nama: ")
    sandi = input("Sandi: ")
    
    if nama in akun and akun[nama]["sandi"] == sandi:
        pengguna["nama"] = nama
        pengguna["peran"] = akun[nama]["peran"]
        print(f"\nLogin berhasil! Selamat datang, {pengguna['nama'].upper()}.")
        return True
    else:
        print("Nama atau sandi salah!")
        return False

def keluar():
    global pengguna
    pengguna = {"nama": "", "peran": ""}
    print("Anda telah keluar.")

def menu_admin():
    while True:
        print("\n--- MENU ADMIN ---")
        print("1. Lihat Jadwal")
        print("2. Tambah Penerbangan")
        print("3. Ubah Penerbangan")
        print("4. Hapus Penerbangan")
        print("5. Keluar")
        pilih = input("Pilih menu: ")
        
        if pilih == "1":
            lihat_jadwal()
        elif pilih == "2":
            tambah_penerbangan()
        elif pilih == "3":
            ubah_penerbangan()
        elif pilih == "4":
            hapus_penerbangan()
        elif pilih == "5":
            keluar()
            break
        else:
            print("Pilihan tidak valid.")

def menu_pelanggan():
    while True:
        print("\n--- MENU PELANGGAN ---")
        print("1. Lihat Jadwal Penerbangan")
        print("2. Pesan Tiket")
        print("3. Lihat Pesanan Saya")
        print("4. Ubah Pesanan")
        print("5. Hapus Pesanan")
        print("6. Keluar")
        pilih = input("Pilih menu: ")
        
        if pilih == "1":
            lihat_jadwal()
        elif pilih == "2":
            pesan_tiket()
        elif pilih == "3":
            lihat_pesanan_saya()
        elif pilih == "4":
            ubah_pesanan()
        elif pilih == "5":
            hapus_pesanan()
        elif pilih == "6":
            keluar()
            break
        else:
            print("Pilihan tidak valid.")

# CRUD Admin
def lihat_jadwal():
    print("\n--- JADWAL PENERBANGAN ---")
    if not jadwal:
        print("Tidak ada jadwal.")
    else:
        for kode, info in jadwal.items():
            print(f"Kode: {kode} | {info['dari']} -> {info['ke']} | Tgl: {info['tanggal']} | Harga: Rp {info['harga']:,}")
            
def tambah_penerbangan():
    kode = input("Kode penerbangan: ").upper()
    if kode in jadwal:
        print("Kode sudah ada!")
        return
    info = {
        "dari": input("Kota asal: ").upper(),
        "ke": input("Kota tujuan: ").upper(),
        "tanggal": input("Tanggal (YYYY-MM-DD): "),
        "harga": int(input("Harga: "))
    }
    jadwal[kode] = info
    print("Penerbangan berhasil ditambahkan.")

def ubah_penerbangan():
    lihat_jadwal()
    kode = input("Kode penerbangan yang diubah: ").upper()
    if kode in jadwal:
        info = jadwal[kode]
        info["dari"] = input(f"Asal baru ({info['dari']}): ") or info["dari"]
        info["ke"] = input(f"Tujuan baru ({info['ke']}): ") or info["ke"]
        info["tanggal"] = input(f"Tanggal baru ({info['tanggal']}): ") or info["tanggal"]
        info["harga"] = int(input(f"Harga baru ({info['harga']}): ") or info["harga"])
        print("Penerbangan berhasil diubah.")
    else:
        print("Kode tidak ditemukan.")

def hapus_penerbangan():
    lihat_jadwal()
    kode = input("Kode penerbangan yang dihapus: ").upper()
    if kode in jadwal:
        del jadwal[kode]
        print("Penerbangan berhasil dihapus.")
    else:
        print("Kode tidak ditemukan.")

# CRUD Pelanggan
def pesan_tiket():
    global id_pesanan_terakhir
    lihat_jadwal()
    kode_penerbangan = input("Kode penerbangan: ").upper()
    if kode_penerbangan in jadwal:
        jumlah = int(input("Jumlah tiket: "))
        id_pesanan_terakhir += 1
        tiket_saya[id_pesanan_terakhir] = {
            "pengguna": pengguna["nama"],
            "penerbangan": kode_penerbangan,
            "jumlah": jumlah
        }
        print("Tiket berhasil dipesan.")
    else:
        print("Kode penerbangan tidak valid.")

def lihat_pesanan_saya():
    print("\n--- PESANAN SAYA ---")
    ditemukan = False
    for id_pesan, info in tiket_saya.items():
        if info["pengguna"] == pengguna["nama"]:
            ditemukan = True
            print(f"ID Pesanan: {id_pesan} | Kode Penerbangan: {info['penerbangan']} | Jumlah: {info['jumlah']}")
    if not ditemukan:
        print("Anda belum memiliki pesanan.")

def ubah_pesanan():
    lihat_pesanan_saya()
    id_ubah = int(input("ID pesanan yang diubah: "))
    if id_ubah in tiket_saya and tiket_saya[id_ubah]["pengguna"] == pengguna["nama"]:
        jumlah_baru = input(f"Jumlah tiket baru ({tiket_saya[id_ubah]['jumlah']}): ")
        if jumlah_baru:
            tiket_saya[id_ubah]["jumlah"] = int(jumlah_baru)
            print("Pesanan berhasil diubah.")
    else:
        print("ID pesanan tidak valid atau bukan milik Anda.")

def hapus_pesanan():
    lihat_pesanan_saya()
    id_hapus = int(input("ID pesanan yang dihapus: "))
    if id_hapus in tiket_saya and tiket_saya[id_hapus]["pengguna"] == pengguna["nama"]:
        del tiket_saya[id_hapus]
        print("Pesanan berhasil dihapus.")
    else:
        print("ID pesanan tidak valid atau bukan milik Anda.")

# Alur Program
def main():
    while True:
        if masuk():
            try:
                if pengguna["peran"] == "admin":
                    menu_admin()
                elif pengguna["peran"] == "pelanggan":
                    menu_pelanggan()
            except ValueError:
                print("Input tidak valid. Silakan coba lagi.")
        
        lagi = input("\nKembali ke login? (y/n): ")
        if lagi.lower() != 'y':
            break

# Jalankan Program
if __name__ == "__main__":
    main()