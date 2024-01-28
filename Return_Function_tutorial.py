#RETURN FUNCTION

def add_number(num1,num2):
    return num1+num2
#mengembalikkan fungsi
x=add_number(7,5)
print(x)

def hitung_tagihan(uang_muka):
    harga_laptop=7000
    sisa_cicilan=harga_laptop-uang_muka
    suku_bunga=10
    jumlah_bunga=sisa_cicilan*suku_bunga/100
    total_tagihan=sisa_cicilan+jumlah_bunga
    tagihan_bulanan=total_tagihan/12
    return tagihan_bulanan
print(round(hitung_tagihan(1000),1))
print(round(hitung_tagihan(2000),1))
#fungsi dengan return dapat dipanggil dengan berbagai parameter value

def iseng(kata,angka):
    return kata.upper()+str(angka*2)
print(iseng("sem",21))
#fungsi return dengan string

def ketawa(lucu):
    if lucu>8:
        return "Hahahaha"
    elif lucu>4:
        return "Ha"
    else:
        return "Garing"
lucu=5
print(ketawa(lucu))
#fungsi return dengan suatu kondisi

def diskon(harga):
    if harga>300:
        return harga/10
    elif ((harga>10)and(harga<=300)):
        return harga/20
    else:
        return 0
bayar=diskon(200)
print(bayar)
#fungsi dengan kondisi

