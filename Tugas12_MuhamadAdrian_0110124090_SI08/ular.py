from Animal import Animal

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, habitat, jenis_bisa):
        super().__init__(nama, makanan, hidup, berkembang_biak, ),
        self.habitat = habitat
        self.jenis_bisa = jenis_bisa

    def info_ular(self):
        super().info_animal(),
        print('habitat \t\t : ', self.habitat,
              '\nJenis bisa \t\t :', self.jenis_bisa)
        
ular_pucuk = ular(' pucuk', 'katak', 'darat', 'bertelur', 'hutan', 'hijau')
ular_pucuk.info_ular()
print('================================')
ular_king_kobra = ular('king kobra', 'ular kecil', 'darat', 'bertelur', 'hutan', 'hitam')
ular_king_kobra.info_ular()