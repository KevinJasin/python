a = int(input("Enter first number  :"))
b = int(input("Enter second number  :"))
c = int(input("Enter third number  :"))
maximum = 0
if a > b and a > c:
    maximum = a 
if b > a and b > c:
    maximum = b
if c > a and c > b:
    maximum = c
print(maximum, "is the maximum of three numbers.")