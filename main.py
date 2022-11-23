tickets = int(input("Введите количество приобретаемых билетов: "))
person = 1

sum = 0.00
while person <= tickets:
    age_for_ticket = int(input(f"Укажите взраст посетителя, для которого приобретается билет № {person} ? "))
    if age_for_ticket < 18:
        print("Билет бесплатный: 0 руб.")
    elif 25 > age_for_ticket >= 18:
        sum += 990.00
        print("Стоимость билета: 990 руб.")
    else:
        sum += 1390.00
        print("Стоимость билета: 1390 руб.")
    person += 1

if tickets > 3:
    sale = sum * 0.9
    print(f"Сумма к оплате {sale} руб., в т.ч. прменена 10% скидка от полной стоимости заказа за покупку более 3-х билетов.")
else:
    print(f"Сумма к оплате {sum} руб.")