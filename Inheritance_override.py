#INHERITANCE
#class mengambil metode dari class lain

#OVERRIDE
#mengganti dan memanggil fungsi dari class lain
#sintax >> super(namaclass_anak,self).nama_fungsi

#contoh
class kendaraan(object):    #class induk
    def __init__(self,nama,roda):  #fungsi identitas
        self.nama=nama
        self.roda=roda
        self.penumpang=[] #array kosong

    def tambah_penumpang(self,nama_penumpang):
        self.penumpang.append(nama_penumpang)  #membuat parameter nama_penumpang utuk mengisi array
    def buka_pintu(self):
        print('Buka pintu Kendaraan')

class mobil(kendaraan):     #class anak
    pintu_terbuka=False

    def buka_pintu(self):
        self.pintu_terbuka=True
        print('Buka pintu Mobil')
        super(mobil, self).buka_pintu()  #override = memanggil fungsi induk
    def tutup_pintu(self):
        self.pintu_terbuka=False


mobnas=mobil("Lamborghini",4)    #mengisi value fungsi diclass
mobnas.tambah_penumpang("ukon")     #menambah value array difungsi induk
mobnas.tambah_penumpang("alan")
mobnas.tambah_penumpang("adol")
mobnas.buka_pintu()                     #memanggil fungsi buka_pintu diclass induk dan anak

print("penumpang : "+str(mobnas.penumpang))     #mencetak nilai array penumpang
print("pintu terbuka : "+str(mobnas.pintu_terbuka))
print("kendaraan: ",mobnas.nama+" roda "+str(mobnas.roda))    #mencetak fungsi nama dan roda di class induk
