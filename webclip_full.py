from splinter import Browser
import time
import os
import csv

#Trzeba zrobić prompt zeby uzytkownik mogl
#wpisac nazwe skanowanego pliku z lista


lista_spotow = []
with open('nazwa_pliku.csv', newline='') as csvfile:
    contents = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in contents:
        r = ', '.join(row)
        r = r.replace(',','')
        lista_spotow.append(r)

browser = Browser()

browser.visit('http://www.agbnielsen.pl/webclip/login.php')
print(browser.title)
if browser.title == "Logowanie do aplikacji WEBCLIP":
    element = browser.find_by_name('login').first
    element.value = "***"
    element2 = browser.find_by_name('pass').first
    element2.value = "***"
    browser.find_by_value('Loguj').click()

if browser.title == "Logowanie do aplikacji WEBCLIP":
    element = browser.find_by_name('login').first
    element.value = "***"
    element2 = browser.find_by_name('pass').first
    element2.value = "***"
    browser.find_by_value('Loguj').click()

if browser.title == "TYPOLOGIA":
    links_found = browser.find_link_by_href('szukaj.php').click()

x = 0
lista_ids = []
not_found = []
exclude = []
while x < len(lista_spotow):
    looked = lista_spotow[x]
    if browser.title == "WYSZUKIWARKA":
        element = browser.find_by_name('search_string').first
        element.value = looked
        element = browser.find_by_value('Szukaj').click()

    print(browser.find_by_css('.ResultTable'))
        
    if browser.find_by_css('.ResultTable'):
        element = browser.find_by_css('.ResultTable').first.find_by_css('a')
        if element.text == looked:
            for e in element:
                lista_ids.append(e["href"][e["href"].find('id=')+3:])
                element.click()
    else:
        exclude.append(lista_spotow[x])
        not_found.append(x+1)
        x += 1
        continue
    
    print(x)
    print(lista_spotow[x])
    print(lista_ids[-1])
    time.sleep(5)
    x += 1

#------------------------
print("lista spotow usuwanie wartosci")
print(len(lista_spotow))
for i in exclude:
    lista_spotow.remove(i)

print(len(lista_spotow))

#------------------------
new_li = []
for i in lista_spotow:
    new_li.append(i.replace('/',''))



print(new_li)
print(lista_ids)

#------------------------
j = 0
while j < len(lista_ids):
    for filename in os.listdir('.'):
        if filename.startswith(lista_ids[j]):
            os.rename(filename, new_li[j]+".mpg")

    j += 1

links_found = browser.find_link_by_href('logout.php').click()

print("not found items:")
print(not_found)
