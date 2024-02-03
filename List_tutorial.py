#LIST

#indexing list - mencari nilai list
cart=["milk","tea","coffee"]
print(cart[0])

#ADD LIST VALUE
cart=["milk","tea","coffee"]
cart.insert(1, "milktea")
print(cart)
#nilai milktea sudah masuk dilist dengan posisi 1

#SORT & REVERSE VALUE
cart=["milk","tea","coffee"]
cart.sort()
print(cart)
#mengurutkan value cart sesuai abjad
cart.reverse()
print(cart)
#membalikkan value cart sesuai abjad

#COPY LIST
cart2=cart.copy()
print(cart2)

#CHANGE LIST VALUE
cart=["milk","tea","coffee"]
cart[2]="water"
print(cart)

#INDEX FROM VARIABLE
name="ukon"
age=23
adress="solok selatan"
info=[name,age,adress]
print(info)

#SLICING LIST - [:]
animals=["cat","dog","bird","cow"]
print(animals[:3])
print(animals[1:3])

pesawat="airplane"
print(pesawat[3:7])
#mencetak "plan"

#SLICING NEGATIF LIST
animals=["cat","dog","bird","cow"]
print(animals[-1])
print(animals[-3:])
print(animals[-3:-1])
#slicing nol dimulai dari kanan

#membuat list
cube=[i**3 for i in range(5)]
print(cube)
#mencetak list pangkat 3 dari range 5
num=[i**2 for i in range(10)]
print(num)
#mencetak pangkat 2 dari range 10

#membuat list ditambah kondisi
even=[i**2 for i in range(10) if i**2 % 2==0]
print(even)
#membuat list pangkat dua bilangan genap dari range 10

num=[i for i in range(10) if i % 3==0]
print(num)
#membuat list kelipatan 3 dari range 10

#ARRANGE LIST
a=[6,3,2,5,4,1]
a.sort() #mengurutkan list
print(a)

a=range(11)
print(a[::2]) #menyusun list bil.genap
print(a[::-1]) #menyusun list secara terbalik/reverse