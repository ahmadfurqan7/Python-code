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
list_saya=range(11)
print(filter(lambda a:a>5,list_saya))

x=[0,1,2,3,4,5,6,7,8,9,10]
print(filter(lambda a:a>5,x))