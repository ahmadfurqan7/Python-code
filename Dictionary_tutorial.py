#DICTIONARY
"""
DICTIONARY bersifat immutable atau tidak bisa diubah
BERBEDA DENGAN LIST dan TUPPLES (muttable)
"""
#didalam dict terbagi 2 ada "key':value

age={"ukon":23,"adol":21,"alan":16}
print(age["ukon"])
print(age["adol"])
print(age["alan"])
#dictionary memiliki 2 nilai setiap value
#dan bisa dipanggil seperti list

#menambah value dictionary
age={"ukon":23,"adol":21}
age["alan"]=16
print(age)
#menambahkan value "alan" di dictionary

#menghubungkan dictionary dan variable
saudara={"pertama":"ukon","kedua":"adol", "ketiga":"alan"}
a=saudara.get("pertama")
b=saudara.get("kedua")
c=saudara.get("ketiga")
print(a)
print(b)
print(c)
#mencetak value dari dictionary

fib={1:1,2:1,3:2,4:3}
a=fib.get(4,2) #jika tidak ada 4 maka diganti 2
b=fib.get(2,1) #jika tidak ada 2 maka diganti 1
print(a+b)
#mencetak value dari dictionary integer

#IN/NOT IN
#fungsi IN dan NOT IN
saudara={"pertama":"ukon","kedua":"adol", "ketiga":"alan"}
print("pertama" in saudara)
print("kedua" not in saudara)
#hasil akan mencetak nilai boolean true/false

#menggabunggkan dict lebih dari 1
anak1={'nama':'ukon','lahir':2000}
anak2={'nama':'adol','lahir':2002}
anak3={'nama':'alan','lahir':2008}
tx=[anak1,anak2,anak3]
for p in tx:
    print(p['nama']+' lahir tahun '+str(p['lahir']))

#dict dengan for
tx={'nama':'ukon', 'umur':23}
for i in tx:
    print(i+':'+str(tx[i])) #i adalah key dan tx[i] alah nilai key

#dict dengan for (pengulangan) + fungsi format
orang={'nama':'ukon','tahun lahir':2000,'warga negara':'indonesia'}
for x in orang:
    print("{}:{}".format(x,orang[x])) #x adalah value key di list orang

#fungsi keys() dan values()
orang={'nama':'ukon',"umur":23,'warga negara':'indonesia'}
for x in orang:
    print(orang.keys()) #mencetak dict keys pada list orang saja
    print(orang.values()) #mencetak dict values pada list orang saja

#membuat dict dengan range()
print({'tx='+str(a) : a**2 for a in range(5)})
#menghasilkan dict dari kuadrat 5 bilangan pertama
