name = input("Mis su nimi on: ")
print("Tere", name)
home = input("Kus sa elad: ")
if (home) == ("Saaremaa"):
      print("Tere saarlane")
age = int(input("Mis su vanus on: "))
if age < 18:
     print("kasutaja on liiga noor et kasutada autod")
elif age == 18:
    print("Suurepärane sa oled 18, sa võid kasutada autod")
else:
     print("võid autod juhtida")
