import random
n = random.randrange(0,100)
guess = int(input("Vali number: "))
while n!= guess:
    if guess < n:
        print("Liiga väike")
        guess = int(input("Vali number jälle: "))
    elif guess > n:
        print("Liiga suur")
        guess = int(input("Vali number jälle: "))
    else:
      break
print("Sa valisid õige numbri: ")