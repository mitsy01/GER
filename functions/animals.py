def show_all_animals(animals: list) -> None:
    for i, animal in enumerate(animals, start=1):
        print(i, animal)


def add_new_animal(animals: list) -> list:
    animal = input("Введіть нову домашню тварину для додавання у список на лікування: ")
    if animal not in animals:
        animals.append(animal)
        print(f"\nТварина додано до списку на лікування")
    else:
        print("\nТака тварина вже є у списку")
    
    return animals


def animal_cured(animals: list, animals_cureds: list) -> tuple:
    animal = input("Введіть тварину яку ви хочете вилікувати: ")
        
    if animal in animals:
        animals.remove(animal)
        animals_cureds.append(animal)
        print(f"\nТварину '{animal}' вилікувано.")
    else:
        print("\nТакої тварини немає у списку.")
        
    return animals, animals_cureds


def show_list_cured_animals(animals_cureds: list) -> None:
    if not animals_cureds:
        print("Список вилікуваних тварин пустий")
            
    for animal in animals_cureds:
        print(animal)


def del_animal_by_name(animals: list) -> list:
    animal = input("Введіть ім'я тварини, яку ви хочете видалити зі списку: ")
    if animal in animals:
        animals.remove(animal)
        print(f"\nТварину '{animal}' видалено зі списку.")
    else:
        print("\nТакої тварини немає у списку.")
    
    return animals


def del_numb_animal(animals: list) -> list:
    index = input("Введіть номер тварини, яку ви хочете видалити зі списку: ")
    if index and index.isdigit() and 0 < int(index) <= len(animals):
        animal = animals.pop(int(index) - 1)
        print(f"\nТварину '{animal}' видалено зі списку.")
    else:
        print("Ви ввели не вірний номер тварини.")
    
    return animals


def sorted_animal_by_name(animals: list) -> None:
    anm = sorted(animals)
    for animal in anm:
        print(animal)
    
    
def change_name_animal(animals: list) -> list:
    animal = input("Змінити ім'я тварині: ")
        
    if animal in animals:
        animal_new = input("Введіть нове ім'я для тварини: ")
        idx = animals.index(animal)
        animals.remove(animal)
        animals.insert(idx, animal_new)
                    
        print(f"Тваринку '{animal}' було змінено на '{animal_new}'.")
    
    return animals


def find_numb_animal_by_name(animals: list) -> None:
    animal = input("Введіть ім'я тварини для її пошуку: ")
        
    if animal in animals:
        index = animals.index(animal)
        print(f"Тварина '{animal}' знаходиться за номером {index + 1}.")
    else:
        print("Такої тварини немає.")
    
    
def find_animal_palindrimes(animals: list[str]) -> None:
    palindrom_animal = []
    for animal in animals:
        if animal.lower() == animal[::-1].lower():
            palindrom_animal.append(animal)
                
    message = f"В списку тварин є такі імена паліндроми:\n{palindrom_animal}" if palindrom_animal else "В списку тварин немає імен паліндромів."
    print(message)