import heapq
num1 = int(input("Voor 1e getal in: "))
num2 = int(input("Voer 2e getal in: "))
num3 = int(input("Voer 3e getal in: "))
num4 = int(input("Voer 4e getal in: "))
num5 = int(input("Voer 5e getal in: "))

allenummers = {num1,num2,num3,num4,num5}
test = heapq.nlargest(5,allenummers)
print(test)