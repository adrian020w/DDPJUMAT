class orang:
    #variabel
    nama = "zilong"
    umur = 0
    gender = ""
    
    #fungsi

    def ngomong(self):
        print("saya bisa bicara")

    def jalan(self, kata):
        print("saya bisa jalan", kata)

#objek1
supir = orang()
supir.nama = "agus"
print(supir.nama)
supir.jalan("kapan?")
supir.sim = "A"
print(supir.sim)

mahasiswa = orang()
print(mahasiswa.nama)

