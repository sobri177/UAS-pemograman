from data import DaftarMahasiswa
from process import ProcessMahasiswa
from view import ViewMahasiswa

def main():
    data_storage = DaftarMahasiswa()
    processor = ProcessMahasiswa()
    viewer = ViewMahasiswa()

    while True:
        print("\nMenu Utama:")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            mhs_baru = processor.input_data()
            if mhs_baru:
                data_storage.tambah_data(mhs_baru)
                print("Data berhasil ditambahkan!")
        
        elif pilihan == '2':
            viewer.cetak_daftar(data_storage)
            
        elif pilihan == '3':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
