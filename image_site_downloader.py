from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests, bs4
import code, sys, os, time


#add image to search for
sys.argv += 'cats'.split()

os.makedirs('images', exist_ok=True)

browser = webdriver.Firefox(executable_path=r'C:\Users\Agasti Mhatre\Downloads\geckodriver.exe')
browser.get('https://www.flickr.com/search/')

search_field = browser.find_element_by_id('search-field')
search_field.click()
search_field.send_keys(sys.argv[1])
search_field.send_keys(Keys.ENTER)

#print(browser.current_url)
soup = bs4.BeautifulSoup(requests.get(browser.current_url).text, 'html.parser')

images = soup.find_all('div', class_='view photo-list-photo-view awake')
print(images)
print('hello')

code.interact(local={**globals(), **locals()})