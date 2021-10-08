from bs4 import BeautifulSoup
import requests
import re
import rowordnet as rwn

"""
task 1
"""
# get URL
page = requests.get("https://ro.wikipedia.org/wiki/O_mie_nouă_sute_optzeci_și_patru_(roman)")

# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')

list(soup.children)

# find all occurance of p in HTML (includes HTML tags)
# print(soup.find_all('p'))

# return only text (does not include HTML tags)
# print(soup.find_all('p')[0].get_text())

"""
  Am facut scraping si am salvat plain textul in fisierul "corpus.txt" la inceput, dupa care am comentat liniile de 
cod ce urmeaza deoarece in acest fisier am adaugat si noi text pentru a face mai multe teste.
"""
# writing the text in a file
# f = open("corpus.txt", "ab")
# for item in soup.find_all('p'):
#     f.write(item.get_text().encode("UTF-8"))
# f.close()


"""
task 2 + task 3

Facem split dupa:
- spatiu
- new line
- numere de telefon
- referinte wikipedia, de exemplu: [10]
- formule de politete simple sau urmate de unul sau mai multe nume
- prescurtari de nume proprii (de exemplu: M. Eminescu) 
- prescurtari de cuvinte

Facand split dupa spatiu, adresele de email, adresele web, adresele IP raman compacte.
"""
text = open("corpus.txt", "r", encoding="utf-8").read()
words_list = re.split(
    r' |\n|(^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\.\/0-9]*$)|\[\d+\]|((?:Dl|Dlui|Dna|Dnei|Dra|Drei|Dr|D-ei|D-lui|D-sa|D-sale|D-ta|Dv|Dvs|D-voastră|dl|dlui|dna|dnei|dra|drei|dr|d-ei|d-lui|d-sa|d-sale|d-ta|dv|dvs|d-voastră|[A-Z]).?\s(?:[A-Z][a-z]+\s*){0,4}|(?:a\.c\.|art\.|cap\.|cca\.|ex\.|etc\.|nr\.|obs\.|op\.cit\.|pag\.|p\.|ș\.a\.|A\.c\.|Art\.|Cap\.|Cca\.|Ex\.|Etc\.|Nr\.|Obs\.|Op\.cit\.|Pag\.|Ş\.a\.))',
    text)
# print(words_list)

"""
Eliminam sirurile vide si elementele None din lista
"""
words_list1 = list()
for word in words_list:
    if word != "" and word is not None:
        words_list1.append(word)
# print(words_list1)

"""
Eliminam new line-urile si spatiile excesive de la finalul cuvintelor
"""
for i in range(0, len(words_list1)):
    if '\n' in words_list1[i] or ' ' in words_list1[i]:
        words_list1[i] = words_list1[i].strip()
# print(words_list1)


patterns = [".", "!", "?", ",", ":", ";", "(", ")", '„', '”', '"']
cuvinte_abreviate = ["a.c.", "art.", "cap.", "cca.", "ex.", "etc.", "nr.", "obs.", "op.cit.", "pag.", "p.", "ș.a.", "A.c.", "Art.", "Cap.", "Cca.", "Ex.", "Etc.", "Nr.", "Obs.", "Op.cit.", "Pag.", "Ş.a."]
formule_de_politete = ["Dl", "Dlui", "Dna", "Dnei", "Dra", "Drei", "Dr", "D-ei", "D-lui", "D-sa", "D-sale", "D-ta", "Dv", "Dvs", "D-voastră", "dl,dlui", "dna", "dnei", "dra", "drei", "dr", "d-ei", "d-lui", "d-sa", "d-sale", "d-ta", "dv", "dvs", "d-voastră"]


"""
Facem split in momentul in care intalnim:
- semne de punctuatie la inceputul sau finalul unui cuvant
- semne de punctuatie la inceputul si finalul unui cuvant
si facem exceptie pentru cuvintele abreviate sau numerele de telefon (a doua componenta din task-ul 4)
"""
f = open("corpus1.txt", "ab")
for word in words_list1:
    string = word + "\n"
    if word[0] in patterns:
        string = word[0] + "\n" + word[1::] + "\n"
    elif len(word) >= 3 and word[-3] in patterns and word[-2] in patterns and word[-1] in patterns:
        string = word[0:-3] + "\n" + word[-3] + "\n" + word[-2] + "\n" + word[-1] + "\n"
    elif len(word) >= 2 and word[-2] in patterns and word[-1] in patterns:
        string = word[0:-2] + "\n" + word[-2] + "\n" + word[-1] + "\n"
    elif word[-1] in patterns:
        string = word[0:-1] + "\n" + word[-1] + "\n"
    if len(word) >= 3 and word[0] in patterns and word[-1] in patterns:
        string = word[0] + "\n" + word[1:-1] + "\n" + word[-1] + "\n"
    elif len(word) >= 3 and word[0] in patterns and word[-2] in patterns and word[-1] in patterns:
        string = word[0] + "\n" + word[1:-2] + "\n" + word[-2] + "\n" + word[-1] + "\n"
    elif len(word) >= 4 and word[0] in patterns and word[-3] in patterns and word[-2] in patterns and word[-1] in patterns:
        string = word[0] + "\n" + word[1:-3] + "\n" + word[-3] + "\n" + word[-2] + "\n" + word[-1] + "\n"
    if word in cuvinte_abreviate:
        string = word + "\n"
    if word in patterns:
        string = word + "\n"
    if re.match("(^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\.\/0-9]*$)", word) is not None:
        string = word + "\n"
    f.write(string.encode("UTF-8"))
f.close()

words_list2 = []
with open('corpus1.txt', encoding="utf-8") as file:
    for line in file:
        words_list2.append(line.strip())
# print(words_list2)


"""
task 4 - prima componenta
Compunem numele de orase, persoane etc.
"""
words_list3 = []
i = 0
while i < len(words_list2):
    new_word = words_list2[i]
    if words_list2[i][0].isupper():
        while words_list2[i + 1][0].isupper():
            new_word += " " + words_list2[i + 1]
            i += 1
    words_list3.append(new_word)
    i += 1
# print(words_list3)


"""
task 5
"""
words_list4 = []
for word in words_list3:
    if "-" in word and word[-1] != "-" and len(word) > 1 and not any(p in word for p in formule_de_politete) and not any(char.isdigit() for char in word) and word[word.find("-") + 1].islower():
        words_list4.extend(word.split("-"))
    else:
        words_list4.append(word)
# print(words_list4)


"""
task 6
In fisierul "corpus2.txt" se afla rezultatul tokenizarii finale.
"""
f = open("corpus2.txt", "ab")
wn = rwn.RoWordNet()
i = 0
while i < len(words_list4):
    new_word = words_list4[i] + "\n"
    if words_list4[i][-1] == "-":
        new_word = words_list4[i][:-1] + words_list4[i + 1]
        if wn.synsets(literal=new_word):
            new_word += "\n"
            f.write(new_word.encode("UTF-8"))
            i += 2
        else:
            i += 1
    else:
        f.write(new_word.encode("UTF-8"))
        i += 1
f.close()
