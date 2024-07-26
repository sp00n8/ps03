import requests
from bs4 import BeautifulSoup
from googletrans import Translator


# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except Exception as e:
        print("Произошла ошибка:", e)


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    translator = Translator()
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        if not word_dict:
            continue
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и его определение
        translated_word = translator.translate(word, src='en', dest='ru').text
        translated_definition = translator.translate(word_definition, src='en', dest='ru').text

        # Начинаем игру
        print(f"Значение слова - {translated_definition} ({word_definition})")
        user = input("Что это за слово? ")
        if user == translated_word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {translated_word} ({word})")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break


word_game()
