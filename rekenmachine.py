Num1 = float(input("Kies je eerste getal: "))
while True:
  opr = input("kies hier je operator (+, -, , /, =): ")

  if "+" in opr: 
    Num2 = input("Kies je nieuwe getal: ")
    Num1 = Num1 + float(Num2)
    print("tussenuitkomst is", Num1)
  elif "-" in opr:
    Num2 = input("Kies je nieuwe getal: ")
    Num1 = Num1 - float(Num2)
    print("tussenuitkomst is", Num1)
  elif "" in opr:
    Num2 = input("Kies je nieuwe getal: ")
    Num1 = Num1 * float(Num2)
    print("tussenuitkomst is", Num1)
  elif "/" in opr:
    Num2 = input("Kies je nieuwe getal: ")
    Num1 = Num1 / float(Num2)
    print("tussenuitkomst is", Num1)

  elif "=" in opr:
    print(Num1)
    break