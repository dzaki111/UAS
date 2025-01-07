from Data import Data
from Process import Process
from View import View

if __name__ == "__main__":
    data = Data()
    process = Process()
    view = View(data, process)

    while True:
        print("\nMenu:")
        print("1. Booking Villa")
        print("2. Lihat Daftar Booking")
        print("3. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            view.get_user_input()
        elif choice == "2":
            view.display_bookings()
        elif choice == "3":
            print("Terima kasih telah menggunakan layanan kami.")
            break
        else:
            print("Pilihan tidak valid.")
