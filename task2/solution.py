import requests
from bs4 import BeautifulSoup
import csv

def fetch_animals_count():
    base_url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    alphabet_counts = {}
    alphabet = "ЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮЪ"

    def parse_page(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        items = soup.select(".mw-category-generated li")
        for item in items[5:]:

            first_letter = item.text[0].upper()
            if first_letter.isalpha() and first_letter in alphabet:
                alphabet_counts[first_letter] = alphabet_counts.get(first_letter, 0) + 1


        next_link = soup.find("a", text="Следующая страница")
        if next_link:
            return "https://ru.wikipedia.org" + next_link["href"]
        return None

    next_page = base_url
    while next_page:
        next_page = parse_page(next_page)

    return alphabet_counts

def save_to_csv(data, filename="beasts.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for letter, count in sorted(data.items()):
            writer.writerow([letter, count])

if __name__ == "__main__":
    print("Начинаю сбор данных...")
    animal_counts = fetch_animals_count()
    save_to_csv(animal_counts)
    print("Данные сохранены в файл beasts.csv")
