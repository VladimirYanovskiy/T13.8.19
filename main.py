tickets = int(input("Введите количество приобретаемых билетов: "))
person = 1

b0 = 0.00 # Билет бесплатный 0,00 руб.
b1 = 990.00 # Билет 990,00 руб.
b3 = 1390.00 # Билет 1390,00 руб.

sum = 0.00
while person <= tickets:
    age_for_ticket = int(input(f"Укажите взраст посетителя, для которого приобретается билет № {person} ? "))
    if age_for_ticket < 18:
        print(f"Билет бесплатный: {b0} руб.")
    elif 25 > age_for_ticket >= 18:
        sum = sum + b1
        print(f"Стоимость билета: {b1} руб.")
    else:
        sum = sum + b3
        print(f"Стоимость билета: {b3} руб.")
    person = person + 1

if tickets > 3:
    sale = sum * 0.9
    print(f"Сумма к оплате {sale} руб., в т.ч. прменена 10% скидка от полной стоимости заказа за покупку более 3-х билетов.")
else:
    print(f"Сумма к оплате {sum} руб.")
