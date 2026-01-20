from celery import shared_task
from app.celery import app
import time

from main.models import *
from main.services.send_mail import send_email

import os
from django.conf import settings
from django.core import management


@shared_task()
def form_consult_email_send(data):
    form_name = data.get('form_name')
    page_url = data.get('page_url')
    phone = data.get('phone') 
    name = data.get('name') 
    truba = data.get('truba') 
    raion = data.get('raion') 
    deep = data.get('deep') 
    obustr = data.get('obustr') 

    email_body = ""

    if form_name:
        email_body += f"Форма: {form_name}\n"

    if name:
        email_body += f"Имя: {name}\n" 
    
    if phone:
        email_body += f"Телефон: {phone}\n" 
    
    if truba:
        email_body += f"Обсадная труба: {truba}\n" 
    
    if raion:
        email_body += f"Выберите район: {raion}\n" 
    
    if deep:
        email_body += f"Глубина скважины у ваших соседей: {deep}\n" 
    
    if obustr:
        email_body += f"Обустройство: {obustr}\n" 

    if page_url:
        email_body += f"Страница: {page_url}\n" 

    send_email("Заявка с сайта", email_body, [])
    return "Отправка заявки с сайта"
