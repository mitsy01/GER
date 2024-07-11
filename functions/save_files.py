import json

from files import list_files

def save_products(animals: list) -> None:
    animals = [f"{animals}\n" for animal in animals]
    with open(list_files.animals, "w", encoding="utf-8") as fh:
        fh.writelines(animals)
        
def save_reviews(reviews: list) -> None:
    reviews = [f"{review}\n" for review in reviews]
    with open(list_files.reviews, "w", encoding="utf-8") as fh:
        fh.writelines(reviews)

def save_animals_cured(animals_cureds: list) -> None:
    with open(list_files.animals_cured, "w", encoding="utf-8") as fh:
        json.dump(animals_cureds, fh, indent=4)


def save_employees(employees: dict) -> None:
    with open(list_files.employees, "w", encoding="utf-8") as fh:
        json.dump(employees, fh, indent=4)


def save_log(log: list) -> None:
    with open(list_files.log, "w", encoding="utf-8") as fh:
        json.dump(log, fh, indent=4)


def save_most_using_command(most_using_command: dict) -> None:
    with open(list_files.most_using_command, "w", encoding="utf") as fh:
        json.dump(most_using_command, fh, indent=4)