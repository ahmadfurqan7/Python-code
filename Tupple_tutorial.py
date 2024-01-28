#TUPPLES
#tupple bersifat immutable atau tidak bisa diubah/ganti

#tupple mirip dengan list
tp=(1,(1,2,3))
print(tp[0])
print(tp[1])
#memanggil value tupple

#tupple dengan variable
num = (1,2,3)
a,b,c = num
print(a)
print(b)
print(c)

#ASTERISK
#mengelompokkan value dari tupple
a,b,*c,d=[1,2,3,4,5]
print(a)
print(b)
print(c)
print(d)
#nilai *c akan mencetak 3,4 karena asterisk

a,b,c,d,*e,f,g=range(20)
print(e)

#tupple dan for
tx=('ukon','adol','alan')
for keren in tx:
    print(keren) #keren adalah variable baru yg dibuat for

