a= ("@@@@  @  @     @       @ @@@@ @@    @")
b= ("@     @  @      @     @  @    @ @   @")
c= ("@ @@  @  @       @   @   @@@@ @  @  @")
d= ("@  @  @  @        @ @    @    @   @ @")
e= ("@@@@  @  @@@@      @     @@@@ @     @")
print(a)
print(b)
print(c)
print(d)
print(e)

print('Kalkulator Pythagoras')

from math import sqrt
print("asumsikan sisi-sisinya adalah a,b,c dengan c sebagai sisi miring")
formula = input('sisi mana yang ingin anda hitung = ')

if formula == 'c':
    sisiA = int(input('masukan panjang sisi a = '))
    sisiB = int(input('masukan panjang sisi b = '))
    sisiC = sqrt(sisiA*sisiA + sisiB*sisiB)
    print('panjang sisi c adalah',sisiC)

elif formula == 'a':
    sisiC = int(input('masukan panjang sisi c = '))
    sisiB = int(input('masukan panjang sisi b = '))
    sisiA = sqrt(sisiC*sisiC + sisiB*sisiB)
    print('panjang sisi a adalah' ,sisiA)

elif formula == 'b':
    sisiC = int(input('masukan panjang sisi c = '))
    sisiA = int(input('masukan panjang sisi a = '))
    sisiB = sqrt(sisiC*sisiC + sisiA*sisiA)
    print('panjang sisi b adalah',sisiB)

else:
        print('input salah')