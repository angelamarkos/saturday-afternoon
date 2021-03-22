import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import os

from helpers import send_email_for
from helpers import Restaurant, DB_NAME
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

ENDPOINT = 'https://buy.am/hy/food-court?p={}'
current = os.getcwd()
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
engine = create_engine(f'sqlite:///{current}/helpers/{DB_NAME}')
session = sessionmaker(bind=engine)()
def get_parsed_data():
    new_name_ids = []
    for i in range(1, 5):
        file = open(FILE_NAME.format(i), 'r')
        data = file.read()
        file.close()
        soup = BeautifulSoup(data, 'html.parser')
        div = soup.find('div', attrs={"class": "listing im-manufacturers-listing"})
        all_a = div.find_all('a')
        for a in all_a:
            info = a.find('div', attrs={'class': "manufacturer-info"}).stripped_strings
            img = a.find('span', attrs={'class': "img-logo-media"}).find('img')['src']
            name_id = os.path.basename(img).split('.')[0]
            existing_restaurant = session.query(Restaurant).filter(Restaurant.name_id==name_id).one_or_none()
            if not existing_restaurant:
                new_restaurant = Restaurant(**{
                    'name': next(info),
                    'open_hours': next(info),
                    'image_url': img,
                    'name_id': name_id
                })
                session.add(new_restaurant)
                new_name_ids.append(name_id)
            else:
                existing_restaurant.name = next(info)
                existing_restaurant.open_hours = next(info)
                session.add(existing_restaurant)
            session.commit()

    send_email_for(new_name_ids, session)

get_parsed_data()
# print(session.query(Restaurant.name, Restaurant.restaurant_id).all())
