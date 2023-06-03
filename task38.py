# Задача 38
# Создать телефонный справочник с возможностью импорта и экспорта данных
# в формате .txt
# Фамилия, имя,отчество,номер телефона - данные, которые должны находится в файле
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь  может ввести одну из характеристик 
#    для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. 
#    Ваша программа не должна быть линейной.
# 5.Дополнить справочник возможностью изменения и удаления данных.
# пользователь также сможет ввести имя или фамилию.



with open('task38.txt','w') as f:
    f.write('Ivanov,Ivan,+79852345433')
    f.write('\nPetrov,Sergei,+79852345434')
    f.write('\nRubin,Vlad,+79852345435')
    f.write('\nCerikov,Roman,+79852345437')


def add_user():
    with open('task38.txt','a') as f:
        f.write('\n')
        f.write((input("Введите Фамилию, Имя, телефон - ")).title())
   

def read_all_users():
    with open('task38.txt','r') as f:
        for line in f:
            print(line)            

def search_user():
    with open('task38.txt','r') as f:
        search = input("Введите искомого абонента: ").title()
        for line in f:
            if search in line:
                print(line)
        
def change_contact():
    with open('task38.txt','r') as f:
        list1 = f.readlines()
    print(list1)
    search = input("Введите искомого абонента: ")
    for i in range(len(list1)):
        if search in list1[i]:
            print(list1[i])
            list1[i] =input("Внесите изменения  - ") + '\n'
    print(list1)
    with open('task38.txt','w') as f:
        for line in list1:
            f.write(line)

def delete_contact():
    with open('task38.txt','r') as f:
        list1 = f.readlines()
    print(list1)
    search = input("Введите искомого абонента: ")
    for i in range(len(list1)):
        if search in list1[i]:
            print(list1[i])
            list1.pop(i)
            break
    print(list1)
    with open('task38.txt','w') as f:
        for line in list1:
            f.write(line)

def info_func():
    print('1. Показать весь справочник ')
    print('2. Добавить абонента ')
    print('3. Поиск абонента')
    print('4. Внести изменения')
    print('5. Удалить контакт')
    print('6. Выход ')
info_func()
while (user_action :=int(input('Выберите запрос по цифре - '))) != 6:
    match user_action:
        case 1:
            read_all_users()
            info_func()
        case 2:
            add_user()
            info_func()
        case 3:
            search_user()
            info_func()
        case 4:
            change_contact()
            info_func()
        case 5:
            delete_contact()
            info_func()
        case 6:
            break
        case _:
            print('Такой функции нет')


           