# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)
# buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method 
# buat minimal 2 objek untuk setiap class childnya.

from Animal import Animal

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, paruh, warna_bulu):
        super().__init__(nama, makanan, hidup, berkembang_biak, ),
        self.paruh = paruh
        self.warna_bulu = warna_bulu

    def info_burung(self):
        super().info_animal(),
        print('paruh \t\t\t : ', self.paruh,
              '\nwarna bulu \t\t :', self.warna_bulu)
        
Burung_beo = Burung('lovebrid', 'milet', 'Darat', 'bertelur', 'melengkung', 'warna-warni')
Burung_beo.info_burung()
print('================================')
Burung_merpati = Burung('Merpati', 'jagung', 'Darat', 'bertelur', 'melengkung', 'putih')
Burung_merpati.info_burung()



       
