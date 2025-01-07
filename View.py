class View:
    """Class untuk mengatur tampilan dan input/output."""
    def __init__(self, data, process):
        self.data = data
        self.process = process

    def display_villas(self):
        print("Daftar Villa:")
        for villa_id, villa in self.data.villas.items():
            print(f"{villa_id}. {villa['name']} - {villa['type']} - Rp {villa['price']:,}")

    def get_user_input(self):
        try:
            name = input("Masukkan nama Anda: ")
            phone = input("Masukkan nomor telepon Anda: ")
            self.process.validate_phone(phone)

            date_str = input("Masukkan tanggal booking (tahun-bulan-hari): ")
            date = self.process.validate_date(date_str)

            self.display_villas()
            villa_choice = int(input("Pilih villa (masukkan nomor): "))
            villa_id = self.process.validate_villa_choice(villa_choice, self.data.villas)

            self.data.add_booking(name, phone, date, villa_id)
            print("Booking berhasil!")
        except ValueError as e:
            print(f"Error: {e}")

    def display_bookings(self):
        if not self.data.bookings:
            print("Belum ada booking.")
            return

        print("+----+---------------+---------------+------------+---------------+")
        print(f"| {'No':<2} | {'Nama':<13} | {'Telepon':<13} | {'Tanggal':<10} | {'Villa':<13} |")
        print("+----+---------------+---------------+------------+---------------+")
        for idx, booking in enumerate(self.data.bookings, start=1):
            print(f"| {idx:<2} | {booking['name']:<13} | {booking['phone']:<13} | {booking['date'].strftime('%Y-%m-%d'):<10} | {booking['villa']['name']:<13} |")
        print("+----+---------------+---------------+------------+---------------+")
