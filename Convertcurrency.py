#Словарь со значениями валют
valuet = {"USD": 79.5782, 
          "BYN": 26.9300,
          "EUR": 93.2060,
          "CNY": 11.1209,
          "CHF": 99.5723}


print("Это конвертер валют, просмотрите список доступных валют к преобразованию в рубли, и введите его. Что бы покинуть программу введите слово EXIT")
print("USD, BYN, EUR, CNY, CHF")

def convex():
    exxt = 0
    while exxt == 0:
        choice = input("Введите код валюты: ")
        if choice == "EXIT":
            exxt = 1
        elif choice.upper() in valuet.keys():
            try:
                amount = float(input("Введите кол-во валюты для перевода её в Российские рубли(RUB):"))
                print(f"{amount} {choice.upper()} в RUB равно {round(amount*valuet[choice.upper()], 2)}")
            except ValueError:
                print("Введено не число!")
        
        else:
            print("Вы ввели код валюты некоректно")

convex()
