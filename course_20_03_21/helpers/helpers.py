from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import ssl
import os
from getpass import getpass

from .models import Restaurant, DB_NAME
current = os.getcwd()


def send_email_for(restaurant_name_ids, session):

    restaurants = session.query(Restaurant).filter(Restaurant.name_id.in_(restaurant_name_ids)).all()
    passwd = getpass()
    context = ssl.create_default_context()

    with SMTP_SSL('smtp.gmail.com', context=context, port=465) as smtp_server:
        smtp_server.login('programmingangela@gmail.com', password=passwd)
        # message = """
        # From: no-reply@test.com
        # Subject: Test123
        # Test 12356
        # """
        text_restaurants = "\n".join(f'{restaurant.name}-{restaurant.open_hours}' for restaurant in restaurants)
        text = f"""
        Hi, this is list of new restaurants...,
        {text_restaurants}
        Have a nice day.
        """
        html_restaurants = "\n".join(f'<p>{restaurant.name}-{restaurant.open_hours}</p>' for restaurant in restaurants)
        html = f"""
        <h1>Hi</h1>
        <p>Hi, this is list of new restaurants...,</p>
        {html_restaurants}
        <p>Have a nice day!</p>
        """
        print(html_restaurants)

        content_text = MIMEText(text, 'plane')
        content_html = MIMEText(html, 'html')
        message = MIMEMultipart('multipart')
        message.attach(content_text)
        message.attach(content_html)
        message['Subject'] = 'Testing'
        message['From'] = 'programmingangela@gmail.com'
        message['To'] = 'programmingangela@gmail.com'

        smtp_server.sendmail('programmingangela@gmail.com', ['programmingangela@gmail.com'],
                             msg=message.as_string())

if __name__ == '__main__':
    send_email_for(None)



