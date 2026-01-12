class Mahasiswa:
    def __init__(self, nim, nama, nilai):
        self.nim = nim
        self.nama = nama
        self.nilai = nilai

class DaftarMahasiswa:
    def __init__(self):
        self.list_mahasiswa = []

    def tambah_data(self, mahasiswa):
        self.list_mahasiswa.append(mahasiswa)