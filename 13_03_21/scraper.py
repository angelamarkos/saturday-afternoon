import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer


ENDPOINT = 'https://buy.am/hy/food-court?p={}'
FILE_NAME = 'buyam_{}.html'
def save_html_files(endpoint_template):
    page = 1
    while page != 18:
        response = requests.get(endpoint_template.format(page))

        if response.status_code != 200:
            print(response.text)
            break
        with open(FILE_NAME.format(page), 'w+b') as html_file:
            html_file.write(response.content)
        page += 1

def save_html_files_v2(endpoint_template):
    page = 1
    while True:
        response = requests.get(endpoint_template.format(page))

        if response.status_code != 200:
            print(response.text)
            break
        with open(FILE_NAME.format(page), 'w+b') as html_file:
            soupstrainer = SoupStrainer('div', attrs={"class": "listing im-manufacturers-listing"})
            soup = BeautifulSoup(response.content, 'html.parser', parse_only=soupstrainer)
            if not soup.find('a'):
                break
            html_file.write(response.content)
        page += 1

# save_html_files_v2(ENDPOINT)

def get_parsed_data():
    dict_data = []
    for i in range(1, 18):
        file = open(FILE_NAME.format(i), 'r')
        data = file.read()
        file.close()
        soup = BeautifulSoup(data, 'html.parser')
        div = soup.find('div', attrs={"class": "listing im-manufacturers-listing"})
        all_a = div.find_all('a')
        for a in all_a:
            info = a.find('div', attrs={'class': "manufacturer-info"}).stripped_strings
            dict_data.append({
                'name': next(info),
                'open_hours': next(info),
                'image_url': a.find('span', attrs={'class': "img-logo-media"}).find('img')['src']
            })
    return dict_data

data = get_parsed_data()
