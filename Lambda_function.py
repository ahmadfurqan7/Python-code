#LAMBDA
#berfungi sebgai pangganti function dan return

#pada fungsi biasa
def tx(x):
    return x**2+x
print(tx(2))

#pada lambda dapat ditulis
print((lambda x: x**2+x)(2))

#LAMBDA DENGAN FUNGSI FILTER()
#contoh
list_saya=range(15)
hasil_list = list(filter(lambda a:a>5,list_saya))
print(hasil_list)

x=[0,1,2,3,4,5,6,7,8,9,10]
hasil = list(filter(lambda a:a>5, x))
print(hasil)
