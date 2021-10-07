from bs4 import BeautifulSoup
import requests
import re

# get URL
page = requests.get("https://ro.wikipedia.org/wiki/O_mie_nouă_sute_optzeci_și_patru_(roman)")

# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')

list(soup.children)

# find all occurance of p in HTML (includes HTML tags)
# print(soup.find_all('p'))

# return only text (does not include HTML tags)
# print(soup.find_all('p')[0].get_text())

# writing the text in a file
# f = open("corpus.txt", "ab")
# for item in soup.find_all('p'):
#     f.write(item.get_text().encode("UTF-8"))

# the tokenizer
text = open("corpus.txt", "r", encoding="utf-8").read()
print(re.split(' |\n', text))
