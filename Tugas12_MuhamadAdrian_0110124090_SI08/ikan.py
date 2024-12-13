from Animal import Animal

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, habitat,  warna_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak, ),
        self.habitat = habitat
        self.warna_ikan = warna_ikan

    def info_ikan(self):
        super().info_animal(),
        print('habitat \t\t : ', self.habitat,
              '\nWarna ikan \t\t :', self.warna_ikan)
        
ikan_hiu = ikan('HIU', 'ikan kecil', 'air', 'bertelur', 'laut', 'biru')
ikan_hiu.info_ikan()
print('================================')
ikan_cupang = ikan('cupang', 'cacing sutra', 'air', 'bertelur', 'aquarium', 'warna-warni')
ikan_cupang.info_ikan()
