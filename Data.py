class Data:
    """Class untuk menyimpan data villa dan booking."""
    def __init__(self):
        self.villas = {
            1: {"name": "Villa dzaki", "type": "biasa", "price": 1000000},
            2: {"name": "Villa arif", "type": "mewah", "price": 1500000},
            3: {"name": "Villa rahman", "type": "mewah pake banget", "price": 2000000},
        }
        self.bookings = []

    def add_booking(self, name, phone, date, villa_id):
        self.bookings.append({
            "name": name,
            "phone": phone,
            "date": date,
            "villa": self.villas[villa_id]
        })
