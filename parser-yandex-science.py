import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://yandex.ru/news/rubric/science'  # https://auto.ria.com/newauto/marka-jeep/' # ссылка
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52 rel: 0',
    'accept': '*/*'}  # юзер-агент
FILE = 'yandex_news.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS,
                     params=params)  # получить страницу гет запросом https://yandex.ru/news/rubric/science
    return r


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")  # обьект супа
    items = soup.find_all('article', class_='mg-card')  # карточки с новостями  #mg-grid__col mg-grid__col_xs_4
    # items2 = soup.find_all('div', class_='news-card__annotation') #аннотации

    yandex_news = []  # список с заголовками и аннотациями
    for item in items:  # цикл ищет в карточках

        yandex_news.append({  # добавление в список yandex_news словаря header
            "time":item.find('span', class_='mg-card-source__time').get_text(),
            "header": item.find('h2', class_='news-card__title').get_text(), # поиск и добавлние заголовков в словарь header
            "annotation": item.find('div', class_='news-card__annotation').get_text(),
            "link": item.find('a', class_='news-card__link').get('href'),
        })
    return yandex_news
    # rint(yandex_news)
    #print(len(yandex_news))

def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file,delimiter=';')
        writer.writerow([' время', ' заголовок', 'аннотация', ' ссылка'])
        for item in items:
            writer.writerow([item['time'], item['header'], item['annotation'], item['link']])


def parse():  # парсинг
    html = get_html(URL)
    if html.status_code == 200:  # проверка коннекта
        yandex_news = get_content(html.text)
        save_file(yandex_news, FILE)
    else:
        print("error")


parse()