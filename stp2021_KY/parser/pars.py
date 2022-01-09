from bs4 import BeautifulSoup
import requests


def parser():
    url = 'https://www.kufar.by/l/r~minsk/telefony-i-planshety'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='kf-cCuQ-3b1df')
    elems = []
    links = []

    for item in items:
        elems.append({
            'title': item.find('h3', class_='kf-cCsi-64b0e').get_text(strip=True),
            'price': item.find('span', class_='kf-plRR-69e81').get_text(strip=True),
        })

        for elem in elems:
            print(f'{elem["title"]} -> price: {elem["price"]}')




parser()