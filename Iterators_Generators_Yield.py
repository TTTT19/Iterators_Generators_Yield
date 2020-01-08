import json
import hashlib

# 1 задача сделать класс, который будет формировать пару - наименование страны и ссылку на страницу в википедии
class FindWiki:
    def __init__(self, domain):
        with open('countries.json', encoding='utf8') as countries_file:
            countries = json.load(countries_file)
            list = []
            for country in countries:
                country_fin = country['name']['common'].replace(" ", "_")
                list.append(country_fin)
        self.url = f'https://{domain}/'
        self.last_link = []
        self.chars = list.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        self.last_link = [self.chars.__next__()]
        link_with_country = f'{self.url}{"".join(self.last_link)}'
        list_county_and_link = [self.last_link[0], ' - ', link_with_country, '\n']
        return list_county_and_link

#Записываем эту пару в файл
with open('text.txt', 'w', encoding='utf8') as f:
    for link in FindWiki('en.wikipedia.org/wiki'):
        f.write("".join(link))

#функция, которая достает построчно текст из файла (ссылка к файлу - параметр) и хэширует ее в md5
def hash(name_or_url= 'text.txt'):
    with open(name_or_url) as f:
        for line in f:
            result = hashlib.md5(line.encode())
            print(line, f'в формате md5: {result.hexdigest()}')

#запускаем эту функцию с ссылкой на файл
hash('text.txt')


