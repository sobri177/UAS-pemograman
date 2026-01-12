# UAS-pemograman
Tentu, mari kita bedah bagaimana kode di atas bekerja berdasarkan prinsip-prinsip yang diminta dalam tugas UAS Anda. Program ini menggunakan arsitektur yang mirip dengan pola MVC (Model-View-Controller) yang umum digunakan dalam pengembangan perangkat lunak profesional.

1. Konsep Modular
Konsep modular berarti memecah program besar menjadi bagian-bagian (modul) yang lebih kecil dan mandiri.

Keuntungan: Kode lebih mudah dibaca, dikelola, dan jika ada kesalahan di bagian tampilan, Anda tidak perlu mengutak-atik bagian logika data.

Penerapan: Kita membagi kode ke dalam file data.py, process.py, dan view.py.
2. Penerapan OOP (Object-Oriented Programming)
Dalam tugas ini, kita membagi tanggung jawab ke dalam tiga kelas utama:

Class Data (DaftarMahasiswa): Berperan sebagai wadah penyimpanan. Ia tidak peduli bagaimana data diinput atau ditampilkan; tugasnya hanya menyimpan list objek mahasiswa.

Class Process (ProcessMahasiswa): Berperan sebagai jembatan logika. Ia menangani cara mengambil input dan memprosesnya sebelum disimpan.

Class View (ViewMahasiswa): Berperan sebagai antarmuka (interface). Ia hanya fokus pada bagaimana data diformat agar terlihat rapi (tabel) saat dilihat oleh pengguna.
3. Validasi Input & Eksepsi (Exception Handling)
Penting untuk menjaga agar program tidak crash saat pengguna melakukan kesalahan.
try: Blok untuk mencoba menjalankan kode yang berisiko error (seperti konversi string ke integer).

raise ValueError: Kita membuat error buatan jika input tidak masuk akal (misal nilai -5), sehingga program bisa memberikan peringatan yang sopan.

except: Menangkap error tersebut agar program tetap berjalan dan tidak berhenti tiba-tiba.
4. Menampilkan Hasil (Table View)
Tampilan tabel dibuat menggunakan string formatting di Python:

{:<10}: Artinya teks rata kiri dengan lebar 10 karakter.

{:^41}: Artinya teks rata tengah dengan lebar 41 karakter. Ini memastikan kolom NIM, Nama, dan Nilai tetap lurus meskipun panjang karakter yang diinput berbeda-beda.
Alur Kerja Program:
Main memanggil Process untuk meminta input.

Process melakukan validasi. Jika valid, data dikirim ke Data.

Data menyimpan objek tersebut ke dalam list.

Saat ingin melihat hasil, Main memanggil View.

View mengambil list dari Data dan mencetaknya dalam bentuk tabel.
