a = float(input("Sisesta 1. küljepikkus"))
b = float(input("Sisesta 2. küljepikkus"))
c = float(input("Sisesta 3. küljepikkus"))

if a + b > c and a + c > b and b + c > a:
   
     if a == b == c:
            print("Kolmnurg on võrdkülgne")
     elif a == b or b == c or c == a:
            print("Kolmnurg on võrdhaarne")
     else:
            print("Kolmnurg on erikülgne")

else:
     print("Selliste küljepikkustega kolmnurk ei saa eksisteerida")
