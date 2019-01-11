from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
import re
import csv

csv_file = open('scraping_test.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['BOOK_Author', 'BOOK_NAME', 'Ratings', 'Review', 'Publisher', 'Language', 'Other Details'])

my_url = "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books"

amazon = "https://www.amazon.com"

u_client = req(my_url)  # loads the my_url variable into u_client

best_seller = u_client.read()

u_client.close()

book = soup(best_seller, 'html.parser')

book_details = book.find_all('span',
                             class_="aok-inline-block zg-item")  # gives the details of all the book present in the page of amazon_best_seller

print(len(book_details))

for x in range(len(book_details)):

    try:

        book_name = book_details[x].find('div', class_="p13n-sc-line-clamp-1").text
        print(book_name)

        book_author = book_details[x].find('div', class_="a-row a-size-small").text
        print(book_author)

        book_rating = book_details[x].find('span', class_="a-icon-alt").text
        print(book_rating)

        book_url = book_details[x].find('a', class_="a-link-normal")['href']  # gives the respective href of the first book book_detail i.e book_details[0]

        book_full_url = amazon + book_url  # this makes the url as "https://amazon.com/........"

        u_book_client = req(book_full_url)

        book_full_detail = u_book_client.read()
        u_book_client.close()
        book_data = soup(book_full_detail, 'html.parser')
        book_review = book_data.find_all('div', class_='a-expander-content a-expander-partial-collapse-content',attrs={"data-hook": "review-collapsed"})
        review = book_review[0].text
        # from here the variable loop is not used this tag is same for every book of every different page
        print(book_review[0].text)  # this gives the top reveiw among other reviews

        book_type = book_data.find('div', {"class": "content"},'ul')  # this encloses the content tag which contains the other details like page, published date,etc

        rest_detail = book_type.find('li').text  # this states the no.of pages in that book and if that is hardcover or not

        print(rest_detail)

        publisher = book_type.find_all('li')[1].text  # this gives the detail about the published dates and edition
        print(publisher)
        lang = book_type.find_all('li')[2].text
        print(lang)
        csv_writer.writerow([book_author, book_name, book_rating, review, publisher, lang, rest_detail])
    except:

        pass

csv_file.close()




















