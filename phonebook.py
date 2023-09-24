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
                    name, num = line.split("\t")
                    data[name] = num
    else:
        with open(NAME_FILE, "w") as f:
            pass

    while True:
        while True:

            print("1. Ввести данные")    
            print("2. Поиск")    
            print("3. Выход")
            user_choice = ("Введите:")
            if user_choice not in ["1","2","3"]:
                print("Ошибка")
            else:
                break
        match user_choice: 
            case "1":
                data = input_data(data)
            case "2":
                search_data(data)
            case "3":
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
    
            print("1. Найти фамилию")    
            print("2. Найти имя")    
            print("3. Найти отчество")
            print("4. Найти номер телефона")
            print("5. Вернуться в меню")
            user_choice = ("Введите:")
            if user_choice not in ["1","2","3","4","5"]:
                print("Ошибка")
            else:
                break      
    
    match user_choice: 
            case "1":
                for key in data:
                    name1, name2, name3 = key.split()
                    if name1 == user_input:
                        print(f"{key} {data[key]}")
            
            case "2":
                for key in data:
                    name1, name2, name3 = key.split()
                    if name2 == user_input:
                        print(f"{key} {data[key]}")
            
            case "3":
                for key in data:
                    name1, name2, name3 = key.split()
                    if name3 == user_input:
                        print(f"{key} {data[key]}")
                
            case "4":
                for key, value in data.items():
                    if value == user_input:
                       print(f"{key} {data[key]}") 
                     
            case "5":
                print("Выход")
                
                return   

if __name__   == "__main__" :
    main()                      


