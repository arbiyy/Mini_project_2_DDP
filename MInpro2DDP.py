user = {
    "barista": {"password": "123", "role": "barista"},
    "customer": {"password": "321", "role": "customer"}
}

menu = {
    "1": {"nama": "Espresso", "harga": 15000},
    "2": {"nama": "Americano", "harga": 20000},
    "3": {"nama": "Japanese/V60", "harga": 35000},
    "4": {"nama": "Butter Coffee", "harga": 27000},
    "5": {"nama": "Spanish Latte", "harga": 31000}
}

def login():
    print("=== SISTEM LOGIN ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username in user and user [username] ["password"] == password:
        role = user [username] ["role"]
        print(f"Login berhasil! Selamat datang, {username} ({role}).")
        return role
    else:
        print("Username atau password salah!")
        return None

def menuread():
    if not menu:
        print("Menu kosong.")
        return
    print("\n=== DAFTAR MENU ===")
    for kodeitem, data in menu.items():
        print(f"Nomor: {kodeitem} | Nama: {data['nama']} | Harga: Rp {data['harga']:,}")

def menucreate():
    try:
        kodebr = input("Masukkan Kode baru (angka): ")
        if kodebr in menu:
            print("kode sudah ada!")
            return
        nama = input("Masukkan nama item: ")
        if not nama:
            print("Nama tidak boleh kosong!")
            return
        
        inputhrg = input("Masukkan harga (angka): ")
        harga = int(inputhrg)
        menu[kodebr] = {"nama": nama, "harga": harga}
        print("Item menu berhasil ditambahkan!")
    except ValueError:
        print("Harga harus berupa angka!")
    except Exception as e: 
        print(f"Terjadi kesalahan: {e}")

def menuupdate():
    menuread()  
    if not menu:
        print("Tidak ada menu untuk diupdate.")
        return 
    try:
        kodeitem = input("Masukkan nomor item yang ingin diupdate: ")
        if kodeitem not in menu:
            print("kode tidak ditemukan!")
            return      
        print("Update apa? (1: Nama, 2: Harga)")
        pilihan = input("Pilih (1/2): ")

        if pilihan == "1":
            namabr = input("Masukkan nama baru: ")
            if namabr:
                menu[kodeitem]["nama"] = namabr
                print("Nama berhasil diupdate!")
            else:
                print("Nama tidak boleh kosong!")
        elif pilihan == "2":
            hargabr = input("Masukkan harga baru (angka): ")
            harga = int(hargabr)
            menu[kodeitem]["harga"] = harga
            print("Harga berhasil diupdate!")
        else:
            print("Pilihan tidak valid!")
    except ValueError:
        print("Harga hanya berupa angka!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def menudelete():
    menuread()  
    if not menu:
        print("Tidak ada menu untuk dihapus.")
        return 
    try:
        kodeitem = input("Masukkan kode yang ingin dihapus: ")
        if kodeitem not in menu:
            print("kode tidak ditemukan!")
            return
        
        pilihan = input(f"Yakin hapus '{menu[kodeitem]['nama']}'? (y/n): ")
        if  pilihan == "y":
            del menu[kodeitem]
            print("Item menu berhasil dihapus!")
        else:
            print("Pembatalan penghapusan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def customer_menu():
    while True:
        print("\n=== MENU CUSTOMER ===")
        print("1. Lihat Menu")
        print("2. Logout")   
        try:
            pilihan = input("Pilih opsi: ")
            if pilihan == "1":
                menuread()
            elif pilihan == "2":
                print("Logout berhasil.")
                break
            else:
                print("Pilihan tidak valid!")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

def barista_menu():
    while True:
        print("\n=== MENU BARISTA ===")
        print("1. Lihat Menu (Read)")
        print("2. Tambah Menu (Create)")
        print("3. Update Menu")
        print("4. Hapus Menu (Delete)")
        print("5. Logout")

        try:
            pilihan = input("Pilih opsi: ")
            if pilihan == "1":
                menuread()
            elif pilihan == "2":
                menucreate()
            elif pilihan == "3":
                menuupdate()
            elif pilihan == "4":
                menudelete()
            elif pilihan == "5":
                print("Logout berhasil.")
                break
            else:
                print("Pilihan tidak valid!")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

def main():
    print("Selamat datang di Sistem Manajemen Menu coffee shoop!")
    
    while True:
        role = login()
        if role is None:
            continue
        if role == "customer":
            customer_menu()
        elif role == "barista":
            barista_menu() 
        pilihan = input("Login lagi? (y/n): ")
        if pilihan != "y":
            print("Program selesai.")
            break
main()
