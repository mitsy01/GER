from datetime import datetime
from pprint import pprint 


from functions.animals import(
    show_all_animals,
    add_new_animal,
    animal_cured,
    show_list_cured_animals,
    del_animal_by_name,
    del_numb_animal,
    sorted_animal_by_name,
    change_name_animal,
    find_animal_palindrimes,
    find_numb_animal_by_name
)
from functions.employees import(
    add_new_employees,
    del_employees,
    show_list_employees,
    change_salary,
    change_position
)
from functions.password import is_verify_pass, generate_pass
from functions.reviews import write_reviews, find_simbols_repeated_all_reviews
from files import list_files
from functions import open_files, save_files


def assist():
    with open(list_files.assist, "r", encoding="utf-8") as fh:
        print(fh.read())


def exit() -> None:
    print("Бажаємо вам гарногодня, до побачення!")
    quit()


def show_log(log: list) -> None:
    pprint(log, width=322)


def show_most_using_commands(most_using_command: list) -> None:
    pprint(most_using_command)


def unknowing_command() -> None:
    print("Невідома команда. Спробуйте ще раз ввести команду.")


def main():
    animals = open_files.animals
    animal_cureds = open_files.animals_cureds
    reviews = open_files.reviews
    employees = open_files.employees
    log = open_files.log
    most_using_command = open_files.most_using_command
    
    user_name = input("Введіть свій логін: ")
    pass_word = employees.get(user_name, {}).get("password", "")

    while not pass_word:
        position = input("Введіть свою посаду: ")
        name = input("Введіть своє ім'я: ")
        salary = input("Введіть свою зарплатню: ")
        employees[user_name] = {
            "position": position,
            "name": name,
            "salary": salary,
            "startdate": datetime.now().strftime("%d.%m.%Y")
        }
        
        command = input("Введіть 'create' для введення свого паролю;\nВведіть 'generate' для автоматичної генерації паролю.\nАбо будь-який символ для виходу з програми\n-> ")
        if command == "create":
            password = input("Введіть пароль 8 і більше символів, цифра і буква:")
            
            if is_verify_pass(password):
                pass_word = password
            else:
                print("Пароль не пройшов перевірку")
                
        elif command == "generate":
            pass_word = generate_pass()
        print(f"Ваш пароль {pass_word}")
        
        password = input("Ввдеіть свій пароль для входу в систему: ")
        
        command = None
        while pass_word == password:
            if not command:
                log.append(f"Користувач з логіном '{user_name}' увійшов в систему: {datetime.now()}\n")
                print("")
            
            command = input("Введіть команду: ")
            log.append(f"Користучав з логіном '{user_name}' ввів команду {command}: {datetime.now()}")
            
            if command in most_using_command:
                most_using_command[command] += 1
            else:
                most_using_command[command] = 1
            
            match command:
                case "assist":
                    assist()
                case "show all animals":
                    show_all_animals(animals)
                case "add new animal":
                    animals = add_new_animal(animals)
                case "animal cured":
                    animals, animal_cureds = animal_cured(animals,animal_cureds)
                case "show list cured animals":
                    show_list_cured_animals(animals)
                case "exit":
                    
                    exit()
                case "del animal by name":
                    animals = del_animal_by_name(animals)
                case "del numb animal":
                    animals = del_numb_animal(animals)
                case "sorted animal by name":
                    sorted_animal_by_name(animals)
                case "change name animal":
                    change_name_animal(animals)
                case "find numb animal by name":
                    find_numb_animal_by_name(animals)
                case "find animal palindrimes":
                    find_animal_palindrimes(animals)
                case "write reviews":
                    write_reviews(reviews)
                case "find simbols repeated all reviews":
                    find_simbols_repeated_all_reviews(reviews)
                case "add new employee":
                    employees = add_new_employees(employees)
                case "del employee":
                    employees = del_employees(employees)
                case "show list employees":
                    show_list_employees(employees)
                case "change salary":
                    employees = change_salary(employees)
                case "change position":
                    employees = change_position(employees)
                case "show log":
                    show_log(log)
                case "show most using commands":
                    show_most_using_commands(most_using_command)
                case _:
                    unknowing_command()
                
            input("\nНатисніть 'enter' для продовження\n")
        else:
            print("Пароль невірний, доступ заборонено")


if __name__ == "__main__":
    main()
