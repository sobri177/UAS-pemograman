class ViewMahasiswa:
    def cetak_daftar(self, daftar_obj):
        print("\n" + "="*45)
        print(f"| {'NIM':<10} | {'NAMA':<15} | {'NILAI':<10} |")
        print("="*45)
        
        if not daftar_obj.list_mahasiswa:
            print(f"| {'TIDAK ADA DATA':^41} |")
        else:
            for mhs in daftar_obj.list_mahasiswa:
                print(f"| {mhs.nim:<10} | {mhs.nama:<15} | {mhs.nilai:<10} |")
        
        print("="*45)
