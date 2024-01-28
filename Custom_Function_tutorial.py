#CUSTOM FUNCTION

#membuat fungsi (def)
def greet():
    print("hello")
    print("hai")
greet()

"""
diatas membuat fungsi greet
yang berisikan perintah print
"""

#FUCTION bisa dipanggil beberapa kali
def perkenalan(nama):
    print("hai",nama)
perkenalan("ukon")
#memasukkan nama "ukon" ke parameter fungsi perkenalan

def say_hello(name,age):
    print("hello "+name)
    print("your age is " + age +" years old")
say_hello("ukon","23")
#fungsi juga bisa memiliki parameter lebih dari 1

#fungsi tanpa argumen
def greet(name="ukon"):
    print("hello", name)
greet() #untuk mencetak paramteter="ukon"
greet("john") #untuk mengganti parameter "ukon"

#fungsi dengan operasi mtk
def double(number):
    print(number*2)
double(5)
#memasukkan 5 ke fungsi double

#fungsi dengan variable
def bmi(lebar,panjang):
    index=lebar/(panjang*panjang)
    print(index)
bmi(16,2)
#bisa memasukkan parameter lebih dari 1

# *** RETURN VALUE (retun) ***
#mengembalikkan nilai parameter
def bmi(lebar,panjang):
    index=lebar/(panjang*panjang)
    return index
#dapat menambahkan nilai parameter sesuai keinginan
order1=bmi(18,3)
print(order1>0)
order2=bmi(50,5)
print(order2>5)
#mencetak 2 = TRUE dan 2 = FALSE

#return juga bisa memakai lebih dari 1 variable
def rect(d1,d2):
    area=d1*d2
    perimeter=2*d1+2*d2
    return area, perimeter

area=rect(50,100)
perimeter=rect(25,50)
print(area)
print(perimeter)
#mencetak masing2 nilai variabel




