from datetime import datetime
import requests
from bs4 import BeautifulSoup
from django.core.mail import send_mail
from celery import shared_task
from core.celery import app
from .models import Author, Quote


@shared_task()
def send_mail_task(email_address, message):
    send_mail('Reminder', message, 'hillel@example.com', [email_address], fail_silently=False)


@app.task
def fetch_new_quotes():
    url = 'https://quotes.toscrape.com/'
    response = requests.get(url)
    added_count = 0
    while response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        quotes = soup.find_all('div', {'class': 'quote'})
        for quote in quotes:
            text = quote.find('span', {'class': 'text'}).text
            if Quote.objects.filter(text=text).exists():
                continue
            author_name = quote.find('small', {'class': 'author'}).text
            author_url = url + quote.find('a')['href']
            author_response = requests.get(author_url)
            author_html = author_response.text
            author_soup = BeautifulSoup(author_html, 'html.parser')
            born_date = author_soup.find('span', {'class': 'author-born-date'}).text
            location = author_soup.find('span', {'class': 'author-born-location'}).text
            description = author_soup.find('div', {'class': 'author-description'}).text
            author, created = Author.objects.get_or_create(name=author_name, birth_date=born_date,
                                                           location=location, bio=description)
            quote, created = Quote.objects.get_or_create(text=text, author=author)
            if created:
                added_count += 1
                if added_count >= 5:
                    break
        if added_count >= 5:
            break
        next_page = soup.find('li', {'class': 'next'})
        if not next_page:
            send_mail(
                subject='Good job, take cookie from polochla, lol',
                message='All is ok',
                from_email='from@example.com',
                recipient_list=['to@example.com', ],
                fail_silently=False)
            break
        next_url = url + next_page.find('a')['href']
        response = requests.get(next_url)
        added_count = 0
