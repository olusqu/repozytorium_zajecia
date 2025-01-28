def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Nie można dzielić przez zero!"
    return x / y

while True:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjście")

    wybor = input("Wpisz wybór (1/2/3/4/5): ")

    if wybor == '5':
        print("Zakończenie programu.")
        break

    try:
        num1 = float(input("Wpisz pierwszą liczbę: "))
        num2 = float(input("Wpisz drugą liczbę: "))
    except ValueError:
        print("Błędne dane. Proszę wpisać liczbę.")
        continue

    if wybor == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif wybor == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif wybor == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif wybor == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    
    else:
        print("Błędny wybór. Proszę wybrać poprawną operację.")
