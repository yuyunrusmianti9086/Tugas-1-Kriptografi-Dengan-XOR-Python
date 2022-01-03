import os
from hashlib import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename

print("Silahkan pilih file yang ingin di encrypt / decrypt")


Tk().withdraw()
filename = askopenfilename()
print(filename)


Fin = filename
Fout = str(input("Silahkan masukan nama file output : "))

K = str(input("Silahkan masukan kata kunci : "))

ShaKey = sha256(K.encode('utf-8')).digest()
print(filename)



with open(Fin, 'rb') as Fin:
    with open (Fout, 'wb') as Fout:
        i = 0
        while Fin.peek():
            c = ord(Fin.read(1))
            j = i % len(ShaKey)
            b = bytes([c^ShaKey[j]])
            Fout.write(b)
            i = i + 1
print("File encrypted !")

