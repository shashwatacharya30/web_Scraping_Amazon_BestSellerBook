from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
import csv
csv_file=open('scraping_test.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['BOOK_Author','BOOK_NAME','Ratings'])


my_url = "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books"

Uclient = req(my_url)

data = Uclient.read()

Uclient.close()

page_html = soup(data,'html.parser')

book_detail=page_html.find_all('span',attrs={"class":"aok-inline-block zg-item"})



for x in range(len(book_detail)):
    book_author = book_detail[x].find('div', class_="a-row a-size-small")
    author=book_author.text
    # book_name now
    book_name = book_detail[x].find('div', class_="p13n-sc-line-clamp-1")
    name=book_name.text
    #book rateing out of 5-star
    book_rating = book_detail[x].find('span', class_="a-icon-alt")
    rating = book_rating.text
    csv_writer.writerow([author,name,rating])

csv_file.close()



