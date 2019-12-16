import urllib.request
from bs4 import BeautifulSoup


urls = open('C:/job/yaltabooking/urls.txt', 'r')
lines = urls.readline()
singleurl = []
for lines in urls:
    singleurl.append(lines)
urls.close()


def get_url(lines):
    response = urllib.request.urlopen(lines)
    return response.read()


def parse(html): #none?
    soup = BeautifulSoup()
    table = soup.find('div', class_= 'page-entity-item-index')
    print(table.prettify())

def main():
    print(get_url(lines))

if __name__ == '__main__':
    main()



   