umur = int(input("masukkan umur: "))

if umur <= 5:
    print("balita")
elif umur > 5 and umur <= 13:
    print("anak-anak")
elif umur > 13 and umur <= 25:
    print("remaja")
elif umur > 25 and umur <= 35:
    print("dewasa")
elif umur > 35 and umur <= 55:
    print("orang tua")
else:
    print("lansia")