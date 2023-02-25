"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
people_dict =   [
    {'name': 'john', 'age':'45', 'job': 'seller'}, 
    {'name': 'Alex', 'age':'33', 'job': 'manager'}, 
    {'name': 'Ivan', 'age':'65', 'job': 'broker'} ,
    {'name': 'Johanes', 'age':'13', 'job': 'unemployed'}, 
    {'name': 'Sam', 'age':'19', 'job': 'cashier'} ,
    {'name': 'Obi-wan', 'age':'25', 'job': 'Jedi'} ,
   ]
import csv

def main():
    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in people_dict:
            writer.writerow(user)

if __name__ == "__main__":
    main()
