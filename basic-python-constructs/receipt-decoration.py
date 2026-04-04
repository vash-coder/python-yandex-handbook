name = input()
price = int(input())
weight = int(input())
amount = int(input())

price_string = str(weight) + 'кг * ' + str(price) + 'руб/кг'
total_string = str(weight * price) + 'руб'
amount_string = str(amount) + 'руб'
change_string = str(amount - weight * price) + 'руб'

print('================Чек================')
print(f'Товар: {name:>28}')
print(f'Цена: {price_string:>29}')
print(f'Итого: {total_string:>28}')
print(f'Внесено: {amount_string:>26}')
print(f'Сдача: {change_string:>28}')
print('===================================')