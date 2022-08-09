from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import code


browser = webdriver.Firefox(executable_path=r'C:\Users\Agasti Mhatre\Downloads\geckodriver.exe')
browser.get('https://play2048.co/')

htmlElem = browser.find_element_by_tag_name('html')
while(True):
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)






code.interact(local={**globals(), **locals()})