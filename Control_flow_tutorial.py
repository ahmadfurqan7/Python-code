#control flow
#SEQUENCE - BERURUTAN
#ITERATION - PENGULANGAN
#SELECCTION - PEMILIHAN

#Sequencing
i="hello world"
print(i)

#ITERATION (for/while)
#(FOR)
for i in range(5):
    print("hello world")
#mencetak "hello world" sebanyak 5 kali

cost=[2,4,6,8,10]
total=0
for i in cost:
    total=total+i
print(total)
#mencetak jumlah dari semua nilai cost

#(WHILE)
i = 5
while i > 1:
    print ("hello")
    i=i-1
#mencetak "hello" sampai nilai i tidak besar dari 1

i=1
while i<=5:
    print(i)
    i=i+1
print("loop done")

#SELECTION (if-else)
age=23
if age >= 20:
    print("Dewasa")
else:
    print("Remaja")
#mencetak dewasa karena menseleksi age besar dari 20

age=17
if age >= 20:
    print("Dewasa")
elif age >=15:
    print("Remaja")
else:
    print("Anak-anak")
#mencetak "remaja" karena age besar dari 15 tapi tidak besar dari 20

#gabungan
angka=3
while True:
    print(angka)
    angka=angka+1
    if not angka>=5:
        break #berguna memberhentikan pengulangan
#jika angka+1 tidak sama atau lebih 5 maka mencetak angka smpai tak hingga