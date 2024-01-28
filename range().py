#FUNCTION RANGE
#membuat list dengan range
x=[a**2 for a in range(1,6)]
print(x)

y=[a**3 for a in range(1,11)]
print(y)

#membuat list dengan range + if
#10 angka kuadrat pertama yg bil.genap dan bil.ganjil
x=[a**2 for a in range(1,11) if a%2==0] #bil.genap : jadi dibagi habis 2 sisa 0
y=[a**2 for a in range(1,11) if a%2==1 and a%5!=0] #bil.ganjil : dibagi habis 2 sisa 1 dan dibagi habis 5 tidak sisa 0
print(x)
print(y)

#for dan if in range
for x in range(1,6):
    if x%2==0:
        val='genap'
    elif x%2!=0:
        val='ganjil'
print(x,val)