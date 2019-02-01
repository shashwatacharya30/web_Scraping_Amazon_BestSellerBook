from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import csv

from bs4 import BeautifulSoup as soup

csv_file = open('scraping_books.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['BOOK_Author', 'BOOK_NAME', 'Publisher', 'Language', 'Other Details'])

driver = webdriver.Firefox()

driver.get("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books")




my_url = "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books"

amazon = "https://www.amazon.com"


for x in range(1,45):
    try:
        book_name = driver.find_element(By.CSS_SELECTOR,'li.zg-item-immersion:nth-child('+str(x)+') > span:nth-child(1) > div:nth-child(1) > span:nth-child(2) > a:nth-child(1) > div:nth-child(2)').text
        print(book_name)
        time.sleep(random.randint(1,8))
        book_author = driver.find_element(By.CSS_SELECTOR,'li.zg-item-immersion:nth-child('+str(x)+') > span:nth-child(1) > div:nth-child(1) > span:nth-child(2) > div:nth-child(2) > a:nth-child(1)').text
        print(book_author)
        time.sleep(random.randint(1,8))
        book_link = driver.find_element(By.CSS_SELECTOR, 'li.zg-item-immersion:nth-child('+str(x)+') > span:nth-child(1) > div:nth-child(1) > span:nth-child(2) > a:nth-child(1)').get_attribute("href")
        driver.get(book_link)
        #gives the publication details 
        pub = driver.find_element(By.CSS_SELECTOR, '.content > ul:nth-child(1) > li:nth-child(2)').text
        print(pub)

      #gives the page number
        pd=driver.find_element(By.CSS_SELECTOR, '.content > ul:nth-child(1) > li:nth-child(1)').text
        print(pd)

        time.sleep(random.randint(1,8))
        #gives the language that the book is written in 
        lan = driver.find_element(By.CSS_SELECTOR, 'div.content:nth-child(2) > ul:nth-child(1) > li:nth-child(3)').text
        print(lan)
        driver.get("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books")
        
        if (x==4):
            x = x+2


        """
        book_link = driver.find_element(By.CLASS_NAME, 'a-link-normal').get_attribute("href")
        driver.get(book_link)
        pub = driver.find_element(By.CSS_SELECTOR, 'td.bucket > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > b:nth-child(1)').text
        print(pub)
        """

        csv_writer.writerow([book_author,book_name,pub,lan,pd])

        
    
    except Exception as e :
        print(e)



driver.quit()


