users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dict = {
    'Общее количество' : 0,
    'Уникальные посещения' : 0
}

dict['Общее количество'] = len(users)
unic_users = list(set(users))
dict['Уникальные посещения'] = len(unic_users)
print(dict)