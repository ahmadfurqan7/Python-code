#SETS
#sets hampir mirip dictionary

#in dan not in
letters={"a","b","c","d"}
if "e" not in letters:
    print("benar")
else:
    print("salah")

#fungsi add dan remove
num={1,2,3,4,5,6,7,8,9,10}
print(num)
num.add(11)
num.remove(1)
print(num)
#menambah dan menghapus value pada sets

#Operasi matematika pada sets
'''
| untuk union
& untuk intersection
- untuk difference
^ untuk symetric difference
'''

a={1,2,3,4,5,6}
b={2,4,6,8,10,12}
print(a|b)
print(a&b)
print(a-b)
print(b-a)
print(a^b)

#membuat sets
cube=[i**3 for i in range(5)]
print(cube)
#mencetak sets pangkat 3 dari range 5
num=[i**2 for i in range(10)]
print(num)
#mencetak pangkat 2 dari range 10

#membuat set ditambah kondisi
even=[i**2 for i in range(10) if i**2 % 2==0]
print(even)
#membuat set pangkat dua bilangan genap dari range 10

num=[i for i in range(10) if i % 3==0]
print(num)
#membuat set kelipatan 3 dari range 10
