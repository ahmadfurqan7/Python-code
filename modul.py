"""modul adalah pemanggilan fungsi dari file python lain
jadi dengan modul kita bisa mengambil fungsi"""

#mengambil fungsi diskon dari file return_function_tutorial.py
from Return_Function_tutorial import diskon
print(diskon(400))
#akan mencetak 40 karena 400/10 di fungsi diskon

#mengambil fungsi ketawa dan fungsi iseng dari return_function_tutorial.py
from Return_Function_tutorial import ketawa, iseng #bisa memanggil lebih dari 1 fungsi dari file yg sama
print(ketawa(9))
print(iseng("ukon",5))

#sintaknya juga bisa dibuat seperti ini
import Return_Function_tutorial as rf
print(rf.ketawa(3))
print(rf.iseng("alan",22))
#jadi nama fungsinya dibuat pada print