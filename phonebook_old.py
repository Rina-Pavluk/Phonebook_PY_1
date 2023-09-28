import os

NAME_FILE = "Телефонный справочник.txt"


def main():
   
    # если есть файл,то его считать,если нет, то пустой список
    # вывести меню и меню обработать в цикле

    data = {}
    if os.path.exists(NAME_FILE):
        with open(NAME_FILE) as f:
            for line in f.readlines():
                if line:
                    # print(line.split("\t"))
                    print('line - ', line)
                    name, num = line.split("\t")
                    data[name] = num
    else:
        with open(NAME_FILE, "w") as f:
            pass

    while True:
        while True:

            print("1. Ввести данные")    
            print("2. Поиск") 
            print("3. Изменить/Удалить данные")
            print("4. Выход")
            user_choice = input("Введите:")
            if user_choice not in ["1","2","3","4"]:
                print("Ошибка")
            else:
                break
        match user_choice: 
            case "1":
                data = input_data(data)
            case "2":
                search_data(data)
            case "3":
                update_or_delete_data(data)    
            case "4":
                print("Выход")
                if not data:
                    return
                with open(NAME_FILE, "w") as f:
                    for name in data:
                        print(f"{name}\t{data[name]}", file=f)
                return              


def input_data(data):    
    name = input("Ведите ФИО: ")
    if name and len(name.split()) == 3:
        num = input("Введите номер телефона: ")
        if num and num.isdigit():

            data[name.replace("\t", " ")] = num
            return data 
    print("Неверный ввод данных")   
    return data                     


def search_data(data):
    user_input = input("Введите данные для поиска: ")
    while True:
    
            print("1. Найти фамилию:")    
            print("2. Найти имя:")    
            print("3. Найти отчество:")
            print("4. Найти номер телефона:")
            print("5. Вернуться в меню:")
            user_choice = input("Введите:")
            if user_choice not in ["1","2","3","4","5"]:
                print("Ошибка")
            else:
                break      
    
    match user_choice: 
            case "1":
                for key in data:
                    name1, name2, name3 = key.clear()
                    if name1 == user_input:
                        print(f"{key} {data[key]}")
            
            case "2":
                for key in data:
                    name1, name2, name3 = key.clear()
                    if name2 == user_input:
                        print(f"{key} {data[key]}")
            
            case "3":
                for key in data:
                    name1, name2, name3 = key.clear()
                    if name3 == user_input:
                        print(f"{key} {data[key]}")
                
            case "4":
                for key, value in data.items():
                    if value == user_input:
                       print(f"{key} {data[key]}") 
                     
            case "5":
                print("Выход")
                
                return  


def update_or_delete_data(data):
    while True:
    
            print("1. Изменить данные:")    
            print("2. Удалить данные:")    
            print("3. Вернуться в меню:")
            user_choice = input("Введите:")
            if user_choice not in ["1","2","3"]:
                print("Ошибка")
            else:
                break

    if user_choice == "1":
        update_data(data)  
    elif user_choice == "2":
        delete_data(data)
    elif user_choice == "3":
        print("Выход")


def update_data(data):
    user_input = input("Введите ФИО для изменения данных: ")        
    if user_input in data:
        new_num = input("Введите новый номер телефона: ")
        if new_num.isdigit():
            data[user_input] = new_num
            print("Данные обновлены: ") 
        else:
            print("Ошибка.Номер не найден")
    else:
        print("Ошибка.Данные не найдены")


def delete_data(data):
    user_input = input("Введите ФИО для удаления данных: ")        
    if user_input in data:
        del data[user_input]
        print("Данные удалены")
    else:
        print("Данные не найдены")


def save_data(data):
    with open(NAME_FILE, "w") as f:
                    for name in data:
                        print(f"{name}\t{data[name]}", file=f)
                

if __name__   == "__main__" :
    main()                      


# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может 
# ввести имя или фамилию,и Вы должны реализовать функционал для изменения и удаления данных.