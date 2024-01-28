#FUNCTION

print("message:",2)
#fungsi bisa lebih dari 1 argumen

uang=5000
print("saldo :",uang)
#fungsi bisa memanggil nilai variable

#LOWER DAN UPPER (upper() dan lower())
print("ukon".upper())
print("UKON".lower())
print("ukon".capitalize())
#mencetak huruf kapital atau tidak di string

#FIND FUNCTION (find())
print("furqan".find("q"))
#mencetak urutan huruf di string

#FUNCTION COUNT
saudara=["ukon","adol","alan"]
print(len(saudara))
#mencetak banyak value di list saudara

#FUNCTION APPEND
saudara=['ukon','adol']
saudara.append('alan')
print(saudara)
#menambahkan value di list saudara

#INSERT FUNCTION
saudara=['ukon','alan']
saudara.insert(1,'adol')
print(saudara)
#menambahkan value pada list beserta posisinya

#POP FUNCTION
item=['buku','pena','pensil']
item.pop(1)
print(item)
#menghilangkan value dari list

#ROUND FUNCTION
print(round(2.555,2))

#function power (pangkat)
print(pow(2,4))
print(pow(3,4))

#FUNCTION ABS()
#NILAI ABSOLUT
a=-20
print("nilai absolut dair -20 adalah =",abs(a))

#FUNCTION COUNT & CLEAR
fruits=["apple","mango","apple","grape","banana","apple"]
print(fruits.count("apple"))
#menghitung jumlah apple
fruits.clear()
print(fruits)
#menghapus nilai list

#FUNCTION MAX DAN MIN
#memilih nilai tertinggi dan terendah
num=(7,10,8,5)
print(max(min(num[:2]),abs(-12)))
#diperoleh max(7,abs(-12)) jadi yg terpilih maksimum adalah abs(-12) = 12

#RANDOM FUNCTION
import random
print(random.randrange(1,10))
#menhasilkan angka random dari range 1-10

#FORMAT FUNCTION
x="ukon"
y="desain"
print("{} memiliki minat dengan {}".format(x,y))

prime=[2,3,5,7,11]
for angka in prime:
    print("tanggal {} juni".format(angka))
#fungsi format dengan pengulangan nilai prime

makanan=["sate","lontong"]
if len(makanan)==2:
    print("itu adalah {}".format(makanan[0]))
    print("itu adalah {}".format(makanan[1]))

#INPUT FUNCTION
name=input("what is your name?")
age=input("what is your age?")
print("hi "+name+". oke, jadi umur anda "+age+" tahun")
#fungsi ini setelah dinputkan nama akan merespon "hi" + nama anda dan umur anda

total=int(input("Berapa kali diadakan kelas?"))
kehadiran=int(input("Berapa kali kehadiran anda?"))
nilaihadir=round(kehadiran/total, 2)
print("Nilai kehadiran anda : "+str(nilaihadir))
if nilaihadir<0.7:
    print("Anda Kurang absen")
else:
    print("Anda Cukup absen")

