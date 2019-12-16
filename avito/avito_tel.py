from selenium import webdriver
from time import sleep
from PIL import Image
from pytesseract import image_to_string


class Slojno:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')

    def tel_recon(self):
        image = Image.open('tel.gif')
        print(image_to_string(image))
    
    def crop(self, location, size):
        image = Image.open('avito_screenshot.png')
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']
        image.crop((x, y, x+width, y+height)).save('tel.gif')

        self.tel_recon()
    def navigate(self):
        self.driver.get('https://www.avito.ru/orel/telefony/telefon_iphone_x10_1843359581')

        button = self.driver.find_element_by_xpath('//a[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
        button.click()

        sleep(5)
        self.take_screenshot()

        image = self.driver.find_element_by_xpath('//a[@class="button item-phone-button js-item-phone-button button-origin button-origin_full-width button-origin_large-extra item-phone-button_card js-item-phone-button_card item-phone-button_with-img"]//*')
        location = image.location #dict{x:1234, y = 1234}
        size = image.size         #dict{width = 1234, height = 1234}

        self.crop(location, size)


def main():
    b = Slojno()


if __name__ == "__main__":
    main()