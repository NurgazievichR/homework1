import requests
from bs4 import BeautifulSoup as BS
import json
import csv


lst = []
for i in range(1,10):
    url = f'https://shop.casio.ru/catalog/?PAGEN_1={i}'
    header={
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.3.954 (beta) Yowser/2.5 Safari/537.36'
    }
    html = requests.get(url, headers=header)
    soup = BS(html.text, 'lxml')
    names = soup.find_all(class_='product-item__articul')
    prices = soup.find_all(class_= "product-item__price")
    links = soup.find_all(class_='product-item__link')
    for n, p, l in zip(names,prices,links):
        name = n.text.strip()
        price = p.text
        link = 'https://shop.casio.ru'+l.get('href')
        with open(f'/home/ramazan/Рабочий стол/python_les/parsing/March 7/watches/watchescsv.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(
                (name, 
                price, 
                link                   
                )
            )

        data = { 
            'watchname': name,
            'price': price,
            'link': link
        }
        lst.append(data)
with open(f'/home/ramazan/Рабочий стол/python_les/parsing/March 7/watches/watchesjson.json', 'a+', encoding='utf-8') as file:
    json.dump(lst, file, indent=4, ensure_ascii=False)




        