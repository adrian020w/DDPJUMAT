import math

def l_balok(p, l, t):
    hitung = 2 * (p*l) + (p*t) + (l*t)
    print(f'luas balok adalah {hitung}')

def l_kubus(s):
    hitung = 6 * s * s
    print(f'luas kubus adalah {hitung}')

def l_prisma(la, ls):
    hitung = 2 * la * ls
    print(f'luas prisma adalah {hitung}')

def l_tabung(r, t):
    hitung = 2 * 3.14 * r * r + 2 * 3.14 * r * t
    print(f'luas tabung adalah {hitung}')

def l_limas(la, ls):
    hitung = la * ls
    print(f'luas limas adalah {hitung}')




