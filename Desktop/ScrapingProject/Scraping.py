from bs4 import BeautifulSoup
import requests

page_to_scrape=requests.get("https://books.toscrape.com/")
soup=BeautifulSoup(page_to_scrape.text, "html.parser")
quotes=soup.find_all("article" , attrs={"class":"product_pod"})
author=soup.find_all("h3" , attrs={"title":""})

for quotes in quotes:
        print(quotes.img["alt"])

        for author in author:
                print(author.text)
                