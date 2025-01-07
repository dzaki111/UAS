from datetime import datetime

class Process:
    """Class untuk memproses validasi dan logika bisnis."""
    @staticmethod
    def validate_date(date_str):
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            if date < datetime.now():
                raise ValueError("Tanggal tidak boleh di masa lalu.")
            return date
        except ValueError as e:
            raise ValueError(f"Format tanggal salah atau tidak valid: {e}")

    @staticmethod
    def validate_phone(phone):
        if not phone.isdigit() or len(phone) < 10:
            raise ValueError("Nomor telepon harus berupa angka dan minimal 10 digit.")

    @staticmethod
    def validate_villa_choice(choice, villas):
        if choice not in villas:
            raise ValueError("Pilihan villa tidak valid.")
        return choice
