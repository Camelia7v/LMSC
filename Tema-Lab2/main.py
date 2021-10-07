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
words_list = re.split(r' |\n|\[\d+\]|((?:Dl|Dlui|Dna|Dnei|Dra|Drei|Dr|D-ei|D-lui|D-sa|D-sale|D-ta|Dv|Dvs|D-voastră|dl|dlui|dna|dnei|dra|drei|dr|d-ei|d-lui|d-sa|d-sale|d-ta|dv|dvs|d-voastră|[A-Z]).?\s(?:[A-Z][a-z]+\s*){0,4}|(?:a\.c\.|art\.|cap\.|cca\.|ex\.|etc\.|nr\.|obs\.|op\.cit\.|pag\.|p\.|ș\.a\.|A\.c\.|Art\.|Cap\.|Cca\.|Ex\.|Etc\.|Nr\.|Obs\.|Op\.cit\.|Pag\.|Ş\.a\.))', text)
# print(words_list)

words_list1 = list()
for word in words_list:
    if word != "" and word is not None:
        words_list1.append(word)
# print(words_list1)

for i in range(0, len(words_list1)):
    if '\n' in words_list1[i] or ' ' in words_list1[i]:
        words_list1[i] = words_list1[i].strip()
print(words_list1)

patterns = [".", "!", "?", ",", ":", ";", "(", ")", '„', '”', '"']
cuvinte_abreviate = ["a.c.", "art.", "cap.", "cca.", "ex.", "etc.", "nr.", "obs.", "op.cit.", "pag.", "p.", "ș.a.", "A.c.", "Art.", "Cap.", "Cca.", "Ex.", "Etc.", "Nr.", "Obs.", "Op.cit.", "Pag.", "Ş.a."]

f = open("corpus2.txt", "ab")
for word in words_list1:
    if any(x in word for x in patterns):
        word3 = list(filter(None, re.split('([.!?:;\(\),„”"])+$', word)))
        word1 = list(filter(None, re.split('^([.!?:;\(\),„”"])+', word3[0])))
        print(word1[::-1], word, word3[1::])
        # print(word1, word2, word3)


# f = open("corpus1.txt", "ab")
# for word in words_list1:
#     string = word + "\n"
#     if word[0] in patterns:
#         string = word[0] + "\n" + word[1::] + "\n"
#     if word[-1] in patterns:
#         string = word[0:-1] + "\n" + word[-1] + "\n"
#     if len(word) >= 2 and word[-2] in patterns and word[-1] in patterns:
#         string = word[0:-2] + "\n" + word[-2] + "\n" + word[-1] + "\n"
#     if len(word) >= 3 and word[-3] in patterns and word[-2] in patterns and word[-1] in patterns:
#         string = word[0:-3] + "\n" + word[-3] + "\n" + word[-2] + "\n" + word[-1] + "\n"
#     if len(word) >= 3 and word[0] in patterns and word[-1] in patterns:
#         string = word[0] + "\n" + word[1:-1] + "\n" + word[-1] + "\n"
#     if len(word) >= 3 and word[0] in patterns and word[-2] in patterns and word[-1] in patterns:
#         string = word[0] + "\n" + word[1:-2] + "\n" + word[-2] + "\n" + word[-1] + "\n"
#     if len(word) >= 4 and word[0] in patterns and word[-3] in patterns and word[-2] in patterns and word[-1] in patterns:
#         string = word[0] + "\n" + word[1:-3] + "\n" + word[-3] + "\n" + word[-2] + "\n" + word[-1] + "\n"
#     if word in cuvinte_abreviate:
#         string = word + "\n"
#     f.write(string.encode("UTF-8"))

# '(?:Dl|Dlui|Dna|Dnei|Dra|Drei|Dr|D-ei|D-lui|D-sa|D-sale|D-ta|Dv|Dvs|D-voastră|dl|dlui|dna|dnei|dra|drei|dr|d-ei|d-lui|
# d-sa|d-sale|d-ta|dv|dvs|d-voastră)\s(?.)(?:[A-Z][a-z]+\s*){1,8}'
# (etc.))".
