a=[6,2,8,5,1]
#Mengakses data dalam list
print(a[2])
print(a[1:4])
print(a[4])
#Mengubah data dalam list
a[3]=7
print(a[3])
a[3:]=[3,4]
print(a[3:])
#Menambah elemen dalam list
b=a[2:4]
print(b[:])
b.append('A')
print(b[:])
b.extend([6,2,4])
print(b[:])
c=a+b
print(c[:])