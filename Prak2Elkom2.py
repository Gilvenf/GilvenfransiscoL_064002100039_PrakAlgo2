a = int(input("masukan nilai a: "))
b = int(input("masukan nilai b: "))
c = int(input("masukan nilai c: "))
maks = 0 
if a > b:
    maks = a
else:
    maks = b
if c > maks:
    maks = c
print ("terbesar:",maks)