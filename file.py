'''
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

1. Открыть файл
2. Сохранить файл
3. Показать контакты
4. Добавить контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход

'''


person_1 = {'Александр': {'ФИО': ' Александров Александр Александрович',   
        'пол': ' М',
        'номер телефона': ' +7(919)5682368',
        'комментарий': ' номер рабочий'} }

person_2 = {'Борис': {'ФИО': ' Борисов Борис Борисович', 
        'пол': ' М',
        'номер телефона': ' +7(193)6583688',   
        'комментарий': ' личный номер'} }

person_3 = {'Венера': {'ФИО': ' Иванова Венера Ивановна', 
        'пол': ' Ж',
        'номер телефона': ' +7(365)5682368',   
        'комментарий': ' номер рабочий'} }




#сохранение данных из словаря в файл:
# with open('contacts_info.txt','w', encoding='utf-8') as contacts_info:
#     for key,val1 in person_1.items():
#         contacts_info.write('{}\n'.format(key,val1))
#         for key_1,val_1 in val1.items():
#             contacts_info.write('{}:{}\n'.format(key_1,val_1))
#         contacts_info.write('\n')
#     for key,val2 in person_2.items():
#         contacts_info.write('{}\n'.format(key,val2))
#         for key_2,val_2 in val2.items():
#             contacts_info.write('{}:{}\n'.format(key_2,val_2))
#         contacts_info.write('\n')
#     for key,val3 in person_3.items():
#         contacts_info.write('{}\n'.format(key,val3))
#         for key_3,val_3 in val1.items():
#             contacts_info.write('{}:{}\n'.format(key_3,val_3))
#         contacts_info.write('\n')

#чтение из файла
with open('contacts_info.txt','r', encoding='utf-8') as contacts_info:
    for key,val1 in person_1.items():
        print('{}'.format(key,val1))
        for key_1,val_1 in val1.items():
            print('{}:{}'.format(key_1,val_1))
        print('\n')
    for key,val2 in person_2.items():
        print('{}'.format(key,val2))
        for key_2,val_2 in val2.items():
            print('{}:{}'.format(key_2,val_2))
        print('\n')
    for key,val3 in person_3.items():
        print('{}'.format(key,val3))
        for key_3,val_3 in val1.items():
            print('{}:{}'.format(key_3,val_3))
        print('\n')

#показать краткую информацию (имя и номер телефона):
with open('contacts_info.txt','r', encoding='utf-8') as contacts_info:
    for username, userinfo in person_1.items():
        phone = userinfo['номер телефона']
        print(f'{username} -> {phone}')
    for username, userinfo in person_2.items():
        phone = userinfo['номер телефона']
        print(f'{username} -> {phone}')
    for username, userinfo in person_3.items():
        phone = userinfo['номер телефона']
        print(f'{username} -> {phone}')
    
#создать новый файл для краткой информации(имя и номер телефона)
# with open('contacts.txt','w', encoding='utf-8') as contacts:
#     for username, userinfo in person_1.items():
#         phone = userinfo['номер телефона']
#         contacts.write(f'{username} -> {phone}\n')
#     for username, userinfo in person_2.items():
#         phone = userinfo['номер телефона']
#         contacts.write(f'{username} -> {phone}\n')
#     for username, userinfo in person_3.items():
#         phone = userinfo['номер телефона']
#         contacts.write(f'{username} -> {phone}')

#В РАБОТЕ:
#создать новый контакт:
# new_contact = {input('Введите имя пользователя: ') : 
#         {'ФИО': input('Введите ФИО пользователя: '),   
#         'пол': input('Введите пол пользователя: '),
#         'номер телефона': input('Введите номер телефона в формате +7(ХХХ)ХХХХХХХ: '),
#         'К=комментарий': input('Добавьте комментраий: ')} }