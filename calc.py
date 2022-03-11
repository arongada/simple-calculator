#--operatorok felvetele--
#osszeadas
def osszead(x, y):
    return x + y
#kivonas
def kivon(x, y):
    return x - y
#szorzas
def szoroz(x, y):
    return x * y
#osztas
def oszt(x, y):
    return x / y
#--operatorok--

#--valasztasi lehetosegek kiirasa--
print("Művelet kiválasztása")
print("1. Összeadás")
print("2. Kivonás")
print("3. Szorzás")
print("4. Osztás")
#--valasztas

#--folyamat kezdet--
while True:
    valasz = input("Válassz műveletet (1/2/3/4): ")
    if valasz in ('1', '2', '3', '4'):
        num1 = float(input("Első szám: "))
        num2 = float(input("Második szám: "))
#ha osszeadas
        if valasz == '1':
            print(num1, "+", num2, "=", osszead(num1, num2))
#ha kivonas
        elif valasz == '2':
            print(num1, "-", num2, "=", kivon(num1, num2))
#ha szorzas
        elif valasz == '3':
            print(num1, "*", num2, "=", szoroz(num1, num2))
#ha osztas
        elif valasz == '4':
            print(num1, "/", num2, "=", oszt(num1, num2))
#--folyamat vege--
#--kovetkezo szamolas--
        next_calculation = input("Következő számolás (igen/nem): ")
        if next_calculation == "nem":
          break
#--kovektezo szamolas--

#hiba
    else:
        print("Ervenytelen!")