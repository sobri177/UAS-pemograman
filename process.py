from data import Mahasiswa

class ProcessMahasiswa:
    def input_data(self):
        print("\n--- Input Data Mahasiswa ---")
        try:
            nama = input("Masukkan Nama: ")
            if not nama:
                raise ValueError("Nama tidak boleh kosong!")
            
            nim = input("Masukkan NIM: ")
            if not nim.isdigit():
                raise ValueError("NIM harus berupa angka!")
            
            nilai = int(input("Masukkan Nilai (0-100): "))
            if nilai < 0 or nilai > 100:
                raise ValueError("Nilai harus antara 0 sampai 100!")
                
            return Mahasiswa(nim, nama, nilai)
        
        except ValueError as e:
            print(f"Terjadi Kesalahan: {e}")
            return None