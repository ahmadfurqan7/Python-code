#OOP (Object Oriented Program)
"""
class NamaClass(object):
"""
class gadget(object):
    sumber_energy = "listrik"
hp=gadget() #hp menjadi class gadget
print(hp.sumber_energy)

#output = listrik karena hp sudah termasuk class gadget

#ditambah metode/fungsi
class tekno(object):
    baterai=100
    def gunakan(self,waktu):                #membuat fungsi didalam class
        self.baterai=self.baterai-waktu
hp=tekno()  #hp termasuk class tekno
print(hp.baterai)
hp.gunakan(20) #input nilai parameter waktu ke fungsi gunakan
print(hp.baterai)
#output 100 dan 80 karena terjadi pengurangan pada fungsi gunakan

class merek(object):
    pembuat=[]
    def tambah_pembuat(self,pembuat):
        self.pembuat.append(pembuat) #appen bertujuan menggabungkan string pembuat yaitu []
hp=merek()
tablet=merek()

hp.tambah_pembuat('apple') #memasukkan/input nilai parameter ke fungsi tambah_pembuat
tablet.tambah_pembuat('samsung')

print(str(hp.pembuat))
print(str(tablet.pembuat))

#fungsi lebih didalam class
"__init__"
#contoh:

class elektronik(object):
    def __init__(self):     #membuat metode batu
        self.fitur=[]
    def tambah_fitur(self,fitur):   #menambah metode baru
        self.fitur.append(fitur)    #append berfungsi menghubungkan parameter fitur
hp=elektronik()
tablet=elektronik()
hp.tambah_fitur('telepon')      #hp dan tablet menginput parameter ke fungsi tambah_fitur
tablet.tambah_fitur('layar besar')

print(str(hp.fitur))
print(str(tablet.fitur))

#contoh lain:
class kendaraan(object):
    def __init__(self,nama):
        self.nama=nama
        self.penumpang=[]

    def tambah_penumpang(self,nama_penumpang):
        self.penumpang.append(nama_penumpang) #kalau tidak append 'penumpang' saja akan mencetak []

mobil=kendaraan('mobil')    #mobil dan motor beserta parameternya diinput ke class kendaraan
motor=kendaraan('motor')
mobil.tambah_penumpang('ukon') #input parameter2 ke fungsi tambah_penumpang
motor.tambah_penumpang('adol')
motor.tambah_penumpang('alan')

print(mobil.penumpang)
print(motor.penumpang)

#parameter fungsi lebih dari 2
#contoh:
class cat:
    def __init__(self,color,legs):
        self.color=color
        self.legs=legs
felix=cat('ginger',4)   #input parameter2 ke fungsi
rover=cat('blond',4)
stumpy=cat('brown',3)

print(felix.color)
print((rover.legs))

#contoh:
class player:
    def __init__(self,name,level):
        self.name=name
        self.level=level
    def intro(self):
        print(self.name+"(Level "+self.level+")")   #mencetak string dan parameter fungsi ("+nama parameter+")

#juga bisa kita input
name=input()
level=input()

char=player(name,level) #menghubungkan class dengan input
char.intro()    #menghubungkan char dengan fungsi intro