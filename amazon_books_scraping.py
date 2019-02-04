from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import random
import csv
import os





options = Options()
options.headless = True 
timestamp = time.time()


path = r'./data'
if not os.path.exists(path):
    os.makedirs(path)

csv_file = open('./data/'+str(timestamp)+'scraping_books.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['BOOK_Author', 'BOOK_NAME', 'Publisher', 'Language', 'Other Details'])

driver = webdriver.Firefox(options = options)



options = Options()
options.headless = True 
timestamp = time.time()



path = r'./data'
if not os.path.exists(path):
    os.makedirs(path)

#csv_file = open('./data/'+str(timestamp)+'scraping_books.csv', 'w')

def book_name():
    try:
        book_name = driver.find_element(By.CSS_SELECTOR,'li.zg-item-immersion:nth-child('+str(x)+') > span:nth-child(1) > div:nth-child(1) > span:nth-child(2) > a:nth-child(1) > div:nth-child(2)').text
        print(book_name)
        time.sleep(random.randint(1,8))
    except Exception as e:
        print(e)
        
    return(book_name)
    
def book_author():
    try:
        book_author = driver.find_element(By.CSS_SELECTOR,'li.zg-item-immersion:nth-child('+str(x)+') > span:nth-child(1) > div:nth-child(1) > span:nth-child(2) > div:nth-child(2) > a:nth-child(1)').text
        print(book_author)
        
    except Exception as e:
        print(e)
        
    return(book_author)
    
def book_link():
    try:
        book_link = driver.find_element(By.CSS_SELECTOR, 'li.zg-item-immersion:nth-child('+str(x)+') > span:nth-child(1) > div:nth-child(1) > span:nth-child(2) > a:nth-child(1)').get_attribute("href")
        driver.get(book_link)
    
    except Exception as e:
        print(e)
        
    return()

def pd():
    try:
        pd=driver.find_element(By.CSS_SELECTOR, '.content > ul:nth-child(1) > li:nth-child(1)').text
        print(pd)
    except Exception as e:
        print(e)
        
    return(pd)
    
def lan():
    try:
        lan = driver.find_element(By.CSS_SELECTOR, 'div.content:nth-child(2) > ul:nth-child(1) > li:nth-child(3)').text
        print(lan)
        
    except Exception as e:
        print(e)
    
    return(lan)

def pub():
    try:
        pub = driver.find_element(By.CSS_SELECTOR, '.content > ul:nth-child(1) > li:nth-child(2)').text
        print(pub)
    except Exception as e:
        print(e)
        
    return(pub)
    
def review():
    try:
        review = driver.find_elements_by_xpath('/html/body/div[2]/div[1]/div[4]/div[30]/div/div[2]/div/div[2]/span[3]/div/div/div[3]/div[3]/div/div[1]/div/div/div[4]/span/div/div[1]')
        
        for reviews in review:
            
            print(reviews.text)
        
    except Exception as e:
        print(e)

        
    return()

"""
for x in range(1,50):
=======
for x in range(1,45):
>>>>>>> fb8f753528e6deb58d3f9273e85cf7da5d1a28c3
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

        time.sleep(random.randint(1,8))

        review = driver.find_elements_by_xpath('/html/body/div[2]/div[1]/div[4]/div[30]/div/div[2]/div/div[2]/span[3]/div/div/div[3]/div[3]/div/div[1]/div/div/div[4]/span/div/div[1]')
        
        for reviews in review:
            
            print(reviews.text)

        csv_writer.writerow([book_author,book_name,pub,lan,pd])

        
    
    except Exception as e :
        print(e)

"""
if __name__ == "__main__":
    
    csv_file = open('./data/'+str(timestamp)+'scraping_books.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['BOOK_Author', 'BOOK_NAME', 'Publisher', 'Language', 'Other Details'])

    driver = webdriver.Firefox(options = options)


    driver.get("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books")

    for x in range(1,20):
        try:
            
            name=book_name()
            author = book_author()
            book_link()
            pages = pd()
            languages = lan()
            publication = pub()
            review()
            driver.get("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books")
            csv_writer.writerow([author,name,publication,languages,pages])
            
        except Exception as e:
            print(e)

  
  
  
  
  
  
  

csv_file.close()
driver.quit()


