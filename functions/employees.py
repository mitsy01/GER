def add_new_employees(employees: dict) -> dict:
    username = input("Введіть логін користувача: ")
    name = input("Введіть ім'я працівника: ")
    position = input("Введіть посаду працівника: ")
    salary = input("Введіть зарплатню працівника: ")
    startdate = input("Введіть дату початку роботи працівника (день,місяць,рік): ")
    password = input("Введіть пароль для працівника: ")
        
    if username not in employees:
        employees[username] = {
            "position": position,
            "name": name,
            "salary": salary,
            "startdate": startdate,
            "password": password
        }
        print("Працівника зареєстровано у системі.")
    else:
        print("Такий логін вже зареєстрован у системі.")


def del_employees(employees: dict) -> dict:
    username = input("Введіть логін працівника для того щоб його видалити:")
    if username in employees:
        del employees[username]
        print(f"Користувача з логіном: '{username}' було видалено")
    else:
        print("Такого користувача немає в системі")
    
    return employees


def show_list_employees(employees: dict) -> None:
    for username in employees:
        print(f"Користувач з логіном '{username}', має ім'я{employees[username]['name']}, почав свою роботу'{employees[username]['startdate']}'.")


def change_salary(employees: dict) -> dict:
    username = input("Введіть логін працівника для того щоб змінити його зарплатню: ")
    salary = input("Введіть нову зарплатню для працівника: ")
    if username in employees:
        employees[username]["salary"] = salary
    else:
        print("Такого користувача немає в системі")
    
    return employees


def change_position(employees: dict) -> dict:
    username = input("Введіть логін працівника для того щоб змінити його посаду: ")
    position = input("Введіть нову посаду для працівника: ")
    if username in employees:
        employees[username]["position"] = position
    else:
        print("Такого користувача немає в системі")
    
    return employees