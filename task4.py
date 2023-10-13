users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
pos={'Общее количество':0,'Уникальные посещения':0}
ynik_list = set(users)
ynik = len(ynik_list)
count = len(users)
pos['Общее количество'] = count
pos['Уникальные посещения'] = ynik
print(pos)