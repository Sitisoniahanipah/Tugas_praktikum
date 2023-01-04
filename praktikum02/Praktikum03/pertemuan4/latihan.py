nilai = int(input("masukkan nilai:"))
grade = ""

if nilai > 90 and nilai <100:
    print("Grade Anda adalah A")
elif nilai >= 80 and nilai < 89:
    print("Grade Anda adalah B")
elif nilai >= 70 and nilai < 79:
    print("Grade Anda adalah C")
elif nilai >= 50 and nilai < 69:
    print("Grade Anda adalah D")
else:
    print("Anda tidak lulus")
