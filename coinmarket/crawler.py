#1. Парсер однопоточный.
#2.Замер времени
#3. multiprocessing Poll
#4.Замер времени
#5. Экспорт csv

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from multiprocessing import Pool
import csv


def get_html(url):                         
    r = requests.get(url)         #Response                                                  
    return r.text                        #Возвращает html-код страницы (url)                                                         


def get_all_lings(html):
    soup = BeautifulSoup(html, 'lxml')

    tds = soup.find('tbody').find_all('tr', class_="cmc-table-row")

    links =[]

    for td in tds:
        a = td.find('a').get('href')                                        #string
        link = 'https://coinmarketcap.com' + a                              #/currencies/bitcoin/
        links.append(link)

    return links


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    try:
        name = soup.find('h1').text.strip()
    except:
        name = ''

    try:
        price = soup.find('span', class_="cmc-details-panel-price__price").text.strip()
    except:
        price = ''

    data = {'name': name,
            'price': price }
    return data


def write_csv(data):
    with open('coinmarketcap.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow( (data['name'],
                          data['price']) )

        print(data['name'], 'parsed')


def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    write_csv(data)


def main():
    start = datetime.now()
    
    url = 'https://coinmarketcap.com/all/views/all/'
    all_links = get_all_lings(get_html(url))

    #for url in all_links:
    #   html = get_html(url)
    #   data = get_page_data(html)
    #  write_csv(data)

    with Pool(10) as p:
        p.map(make_all, all_links)
    
    end = datetime.now()

    total = end - start
    print(str(total))




if __name__ == '__main__':
    main()