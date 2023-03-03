import pickle
import os

storage_filename = "storage.pickle"

list = []

if not os.path.exists(storage_filename): # Если файла не существует
    with open(storage_filename, "wb") as f: # То создаем его
        pickle.dump(list, f) # Сохрняя в него наш список
else: # Если же существует
    with open(storage_filename, "rb") as f:
        list = pickle.load(f) # То загружаем из него список

print('Привет. Я хранитель товаров. Тут ты можешь добавить товак в список.')
print('Выберите номер действия:\n','1 - показать список\n', '2 - добавить товар \n', '3 - удалить товар.\n', '4 - изменить товар\n', '5 - очистить список')

user_choise = int(input())

if user_choise == 1:
    print('\nСписок: ')
    for i in list:
        print(i) 
elif user_choise == 2:
    num = input('Введите назание товара: \n')
    list.append(num)
    print('\nСписок: ')
    for i in list:
        print(i)
elif user_choise == 3:
    num = int(input('Введите индекс товара: \n'))
    list.pop(num)
    print('\nСписок: ')
    for i in list:
        print(i)
elif user_choise == 4:
    num = int(input('Введите индекс товара: \n'))
    name = input('Введите новое название товара: \n')
    list[num] = name
    print('\nСписок: ')
    for i in list:
        print(i) 
elif user_choise == 5:
    sure = input('Вы уверены(да/нет): ')
    if sure == 'да':
        print('\nСписок очищен')
        list.clear()
    elif sure =='нет':    
        exit()
    else:
        print('Команда не распознана')

else:
    print('Команда не распознана')

with open(storage_filename, "wb") as f:
    pickle.dump(list, f) # Сохраняем измененный список в файл
