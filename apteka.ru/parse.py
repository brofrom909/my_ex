import urllib.request
from bs4 import BeautifulSoup
#import csv
# Включить csv, если нужно сохранить

def get_html(url): #Дает URL
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):
    soup = BeautifulSoup(html) #Интерфейс soup
    table = soup.find('div', class_='index_dropdown-menu')
    
    med = []  # Список, в который будет записаны искомые значения
    
    for category in table.find_all('li'):
        cols = category.find_all('a')

        med.append({
            'name': cols[0].span.text
        })

    for medicines in med:
        print(medicines)


#def save(med, path):
#    with open(path, 'w') as csvfile:            #Сохранение если нужно
#        writer = csv.writer(csvfile)
#        writer.writerow(('Классификация'))
#
#
#    for medicines in med:
#                writer.writerow((medicines['name']))

def main():
    parse(get_html('https://apteka.ru/')) 


if __name__ == '__main__':
    main()
