# UAS
# NAMA  = DZAKI ARIF RAHMAN
# NIM   = 312410312
# KELAS = TI.24.A4
## tugas
![Screenshot 2025-01-02 203312](https://github.com/user-attachments/assets/ce0a811c-e167-4826-8b16-fd0bfe9b5848)

## Deskripsi Program
Program ini adalah sistem manajemen booking villa berbasis konsol. Pengguna dapat melakukan booking villa dengan memilih villa yang tersedia, memasukkan detail booking, dan melihat daftar booking yang telah dibuat.

Program ini terdiri dari tiga komponen utama:
1. **Data**: Menyimpan data villa dan data booking.
2. **Process**: Memproses logika bisnis dan validasi.
3. **View**: Mengatur input/output pengguna dan tampilan data.

---

## Cara Menjalankan Program
1. Pastikan Python telah terinstal di komputer Anda.
2. Simpan file program dengan nama file seperti `booking_villa.py`.
3. Jalankan program menggunakan terminal atau command prompt dengan perintah:
   ```
   python booking_villa.py
   ```
4. Ikuti instruksi yang ditampilkan di konsol untuk memilih menu:
   - **1. Booking Villa**: Memasukkan data booking baru.
   - **2. Lihat Daftar Booking**: Menampilkan daftar booking yang telah dibuat.
   - **3. Keluar**: Mengakhiri program.

---
## Screenshout vsc kodingan

![UAS semester 1](https://github.com/user-attachments/assets/8852c4a4-7ed4-4bc1-b19c-ce2e2f7d4105)

## Struktur Program
### 1. **Class Data**
Class ini bertanggung jawab untuk menyimpan data villa dan data booking.

#### Atribut:
```python
self.villas = {
    1: {"name": "Villa dzaki", "type": "biasa", "price": 1000000},
    2: {"name": "Villa arif", "type": "mewah", "price": 1500000},
    3: {"name": "Villa rahman", "type": "mewah pake banget", "price": 2000000},
}
self.bookings = []
```

#### Metode:
```python
# Menambahkan data booking ke dalam list bookings
def add_booking(self, name, phone, date, villa_id):
    self.bookings.append({
        "name": name,
        "phone": phone,
        "date": date,
        "villa": self.villas[villa_id]
    })
```

### 2. **Class Process**
Class ini bertanggung jawab untuk memproses logika bisnis seperti validasi input pengguna.

#### Metode:
```python
# Memvalidasi format tanggal
def validate_date(date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')  # Konversi string ke format tanggal
        if date < datetime.now():  # Periksa apakah tanggal berada di masa lalu
            raise ValueError("Tanggal tidak boleh di masa lalu.")
        return date  # Mengembalikan tanggal yang valid
    except ValueError as e:
        raise ValueError(f"Format tanggal salah atau tidak valid: {e}")

# Memvalidasi nomor telepon
def validate_phone(phone):
    if not phone.isdigit() or len(phone) < 10:  # Periksa apakah telepon berupa angka dan panjangnya >= 10
        raise ValueError("Nomor telepon harus berupa angka dan minimal 10 digit.")

# Memvalidasi pilihan villa
def validate_villa_choice(choice, villas):
    if choice not in villas:  # Periksa apakah ID villa valid
        raise ValueError("Pilihan villa tidak valid.")
    return choice  # Mengembalikan ID villa yang valid
```

### 3. **Class View**
Class ini mengatur input/output pengguna dan menampilkan data di konsol.

#### Metode:
```python
# Menampilkan daftar villa yang tersedia
def display_villas(self):
    print("Daftar Villa:")
    for villa_id, villa in self.data.villas.items():
        print(f"{villa_id}. {villa['name']} - {villa['type']} - Rp {villa['price']:,}")

# Meminta input dari pengguna untuk melakukan booking
def get_user_input(self):
    try:
        name = input("Masukkan nama Anda: ")  # Input nama pelanggan
        phone = input("Masukkan nomor telepon Anda: ")  # Input nomor telepon
        self.process.validate_phone(phone)  # Validasi nomor telepon

        date_str = input("Masukkan tanggal booking pakai angka semua (tahun-bulan-hari): ")  # Input tanggal booking
        date = self.process.validate_date(date_str)  # Validasi tanggal booking

        self.display_villas()  # Menampilkan daftar villa
        villa_choice = int(input("Pilih villa (masukkan nomor): "))  # Input pilihan villa
        villa_id = self.process.validate_villa_choice(villa_choice, self.data.villas)  # Validasi pilihan villa

        self.data.add_booking(name, phone, date, villa_id)  # Menambahkan data booking
        print("Booking berhasil!")  # Pesan sukses
    except ValueError as e:
        print(f"Error: {e}")  # Menampilkan pesan error jika input tidak valid

# Menampilkan daftar booking yang telah dibuat dalam format tabel
def display_bookings(self):
    if not self.data.bookings:  # Periksa apakah ada data booking
        print("Belum ada booking.")
        return

    # Menampilkan daftar booking dalam tabel
    print("+----+---------------+---------------+------------+---------------+")
    print(f"| {'No':<2} | {'Nama':<13} | {'Telepon':<13} | {'Tanggal':<10} | {'Villa':<13} |")
    print("+----+---------------+---------------+------------+---------------+")
    for idx, booking in enumerate(self.data.bookings, start=1):  # Iterasi setiap data booking
        print(f"| {idx:<2} | {booking['name']:<13} | {booking['phone']:<13} | {booking['date'].strftime('%Y-%m-%d'):<10} | {booking['villa']['name']:<13} |")
    print("+----+---------------+---------------+------------+---------------+")
```

### 4. **Fungsi Utama (`__main__`)**
Program dijalankan dengan menampilkan menu utama:
```python
if __name__ == "__main__":
    data = Data()  # Membuat instance Data
    process = Process()  # Membuat instance Process
    view = View(data, process)  # Membuat instance View dengan data dan process

    while True:
        # Menu utama program
        print("
Menu:")
        print("1. Booking Villa")
        print("2. Lihat Daftar Booking")
        print("3. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            view.get_user_input()  # Memanggil fungsi input pengguna untuk booking
        elif choice == "2":
            view.display_bookings()  # Menampilkan daftar booking
        elif choice == "3":
            print("Terima kasih telah menggunakan layanan kami.")  # Pesan keluar
            break
        else:
            print("Pilihan tidak valid.")  # Pesan jika input menu tidak valid
```

---

## Contoh Penggunaan
1. **Booking Villa**
   - Input nama, nomor telepon, tanggal booking (format `YYYY-MM-DD`), dan pilihan villa.
   - Jika input valid, booking akan berhasil disimpan.

2. **Lihat Daftar Booking**
   - Menampilkan daftar booking yang telah dibuat dalam format tabel dengan kolom: No, Nama, Telepon, Tanggal, dan Villa.

---

## Validasi dan Pesan Error
1. **Tanggal**:
   - Format harus `YYYY-MM-DD`.
   - Tidak boleh memilih tanggal di masa lalu.
   - Pesan error: `Format tanggal salah atau tidak valid`.

2. **Nomor Telepon**:
   - Harus berupa angka.
   - Minimal 10 digit.
   - Pesan error: `Nomor telepon harus berupa angka dan minimal 10 digit.`

3. **Pilihan Villa**:
   - Harus sesuai dengan ID villa yang tersedia.
   - Pesan error: `Pilihan villa tidak valid.`

---

## Daftar Villa
![Screenshot 2025-01-07 111951](https://github.com/user-attachments/assets/7017282c-74b7-429f-a9c7-52faa412e007)


---
## Screenshout output 
![image](https://github.com/user-attachments/assets/a8137ccc-18e3-432c-9b7a-76d3c1da5dcd)


## Catatan
- Program ini menggunakan format tanggal `YYYY-MM-DD`.
- Nomor telepon harus berupa angka dan panjang minimal 10 digit.
- Daftar booking akan hilang ketika program ditutup, karena data hanya disimpan di memori selama program berjalan.

---

