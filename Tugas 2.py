#Nama : Diodo Arrahman
#NPM  : G1A022027
#Kelas A Informatika
class Mahasiswa:
#Deklarasi Kelas Mahasiswa
    def __init__(self, nama,nim,jurusan):
#Definisi metode Init untuk menginisialisasi objek ketika objek dibuat, metode ini menerima 4 parameter yaitu self, nama, nim dan jurusan
#parameter self digunakan untuk merujik ke objek yang dibuat
        self.nama = nama
#inisialiasi atribut nama, nilainya diambil dari parameter nama
        self.nim = nim
#inisialiasi atribut nim, nilainya diambil dari parameter nim
        self.jurusan = jurusan
#inisialiasi atribut jurusan, nilainya diambil dari parameter jurusan
    def tampilkan_info(self):
#definisi method tampilkan_info dengan parameter self untuk menampilkan informasi Mahasiswa dalam objek yang menggunakan methodnya
        print("\nInformasi Mahasiswa",
              "\nNama    :",self.nama,
              "\nNIM     : ",self.nim,
              "\nJurusan :",self.jurusan.nama_jurusan)
#Kode ini mencetak ke output informasi Mahasiswa, dengan informasi yang ditampilkan adalah nama, nim, dan jurusan nya

class Jurusan:
#Deklarasi Kelas Jurusan
    def __init__(self,nama_jurusan):
#Definisi metode init yang digunakan untuk menginisialiasi objek ketika objek dibuat, metode ini menerima parameter self dan nama_jurusan
        self.nama_jurusan = nama_jurusan
#inisialiasi atribut nama_jurusan dengan nilainya diambil dari parameter nama_jurusan
        self.DaftarMahasiswa = []
#inisialiasi atribut DaftarMahasiswa untuk menyimpan daftar Mahasiswa yang berada pada jurusan tertentu
#atribut ini merupakan sebuah list
    def tambah_mahasiswa(self,mahasiswa):
#Definisi method tambah mahasiswa yang menerima parameter mahasiswa
        self.DaftarMahasiswa.append(mahasiswa)
#menambahkan mahasiswa yang diberikan pada parameter ke list daftar mahasiswa
    def tampilkan_daftar_mahasiswa(self):
#Definisi untuk menampilkan daftar mahasiswa ke output
        x =1
#pembuatan variabel x yang bernilai 1, digunakan untuk memberi nomor pada daftar mahasiswa
        print(f"\nDaftar Mahasiswa di {self.nama_jurusan}")
#mencetak judul yaitu daftar mahasiswa di jurusan yang diinginkan
        for daftarmahasiswa in self.DaftarMahasiswa:
#perulangan untuk mencetak daftar mahasiswa yang terdapat dalam list daftar mahasiswa
            print(f"{x}. {daftarmahasiswa.nama} ({daftarmahasiswa.nim}) ")
#mencetak nama dan nim mahasiswa 
            x+=1
#increement nilai x

class Universitas:
#Deklarasi kelas Universitas
    def __init__(self,NamaUniversitas):
#Definisi method init kelas Universitas yang mempunyai parameter self dan nama universitas
        self.namauniversitas = NamaUniversitas
#inisialiasi atribut nama universitas dengan nilai dari parameter NamaUniversitasi
        self.DaftarJurusan = []
#inisialiasi atribut daftar jurusan dalam bentuk list
    def tambah_jurusan(self,jurusan):
#definisi method tambah_jurusan dengan menerima parameter self dan jurusan
        self.DaftarJurusan.append(jurusan)
#menambahkan jurusan ke list daftar jurusan
    def tampilkan_daftar_jurusan(self):
#definisi method tampilkan daftar jurusan
        x =1
#deklarasi variabel x bernilai 1 sebagai nomor pada daftar jurusan
        print(f"\nDaftar Jurusan di {self.namauniversitas}")
#Mencetak judul Daftar Jurusan di objek universitas yang dimaksud
        for daftarjurusan in self.DaftarJurusan:
#Perulangan for untuk list Daftar Jurusan
            print(f"{x}. {daftarjurusan.nama_jurusan}")
#Mencetak nama-nama jurusan
            x+=1
#Increement x

universitas = Universitas("XYZ University")
#pembuatan objek universitas dari kelas Universitas dengan parameter berupa nama Universitas yaitu Universitas XYZ
jurusan1 = Jurusan("Teknik Informasika")
#pembuatan objek jurusan1 dari kelas Jurusan dengan parameter Teknik Informatika
jurusan2 = Jurusan("Ilmu Hukum")
#pembuatan objek jurusan2 dari kelas Jurusan dengan parameter Ilmu Hukum
universitas.tambah_jurusan(jurusan1)
#menggunakan metode tambah jurusan ke objek universitas dengan parameter jurusan1
#Dengan menggunakan metode ini, jurusan 1 akan ditambahkan ke daftar jurusan di kelas universitas
universitas.tambah_jurusan(jurusan2)
#menggunakan metode tambah jurusan ke objek universitas dengan parameter jurusan2
mahasiswa1 = Mahasiswa("Diodo Arrahman","G1A022027",jurusan1)
#pembuatan objek mahasiswa1 dengan parameter Nama, NIM, dan jurusan
mahasiswa2 = Mahasiswa("Simore Moremore","G1A022101",jurusan1)
#pembuatan objek mahasiswa2 dengan parameter Nama, NIM, dan jurusan
mahasiswa3 = Mahasiswa("Udin Sipudin","B1A022001",jurusan2)
#pembuatan objek mahasiswa3 dengan parameter Nama, NIM, dan jurusan
mahasiswa4 = Mahasiswa("Wawan Setiawan","B1A022076",jurusan2)
#pembuatan objek mahasiswa4 dengan parameter Nama, NIM, dan jurusan

jurusan1.tambah_mahasiswa(mahasiswa1)
#penggunaan metode tambah mahasiswa oleh objek jurusan1
jurusan1.tambah_mahasiswa(mahasiswa2)
#penggunaan metode tambah mahasiswa oleh objek jurusan1
jurusan2.tambah_mahasiswa(mahasiswa3)
#penggunaan metode tambah mahasiswa oleh objek jurusan2
jurusan2.tambah_mahasiswa(mahasiswa4)
#penggunaan metode tambah mahasiswa oleh objek jurusan2
#Penggunakan metode tersebut akan akan menambahkan objek mahasiswa ke objek jurusan sesuai dengan jurusan masing2

universitas.tampilkan_daftar_jurusan()
#Penggunaan method tampilkan_daftar_jurusan ke objek universitas
jurusan1.tampilkan_daftar_mahasiswa()
#penggunaan method daftar mahasiswa ke objek jurusan1
jurusan2.tampilkan_daftar_mahasiswa()
#penggunaan method daftar mahasiswa ke objek jurusan2
mahasiswa1.tampilkan_info()
#penggunaan method tampilkan info oleh objek mahasiswa1
mahasiswa4.tampilkan_info()
#penggunaan method tampilkan info oleh objek mahasiswa4
