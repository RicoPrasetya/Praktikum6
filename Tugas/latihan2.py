Nilai = []
stop = False
i = 0
b=0
a=0
while (not stop):
    Nilai_baru = input("Nama : ".format(i))
    Nilai.append(Nilai_baru)
    Nilai_baru = input("Nim : ".format(i))
    Nilai.append(Nilai_baru)
    Nilai_baru = input("Nilai tugas : ".format(i))
    Nilai.append(Nilai_baru)
    Nilai_baru = input("Nilai UTS : ".format(i))
    Nilai.append(Nilai_baru)
    Nilai_baru = input("Nilai UAS : ".format(i))
    Nilai.append(Nilai_baru)
    i += 1
    tanya = input("Mau isi lagi? (y/t): ")
    if (tanya == "t"):
        stop = True
# Cetak Semua Hobi
print ("===================================================================================")
print ("| No |    Nama    |    NIM    | Nilai tugas | Nilai UTS | Nilai UAS | Nilai akhir |".format(len(Nilai)))
for baris in range(i):
    c=int(int(Nilai[a+2])+int(Nilai[a+3])+int(Nilai[a+4]))
    d=int(c/3)
    print("| ",b+1,"|",Nilai[a],"      |",Nilai[a+1],"|",Nilai[a+2],"         |",Nilai[a+3],"       |",Nilai[a+4],"       |",d,"         |")
    b=b+1
    a=a+5
print ("===================================================================================")