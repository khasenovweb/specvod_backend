import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

from urllib.parse import unquote, urlparse
import email.utils


def send_email(
    subject,
    body,
    attachment_files,
):
    """
    Отправка email с несколькими вложениями
    
    :param sender_email: email отправителя
    :param sender_password: пароль отправителя
    :param receiver_email: email получателя
    :param subject: тема письма
    :param body: текст письма
    :param attachment_files: список путей к файлам для прикрепления
    :param smtp_server: SMTP сервер
    :param smtp_port: SMTP порт
    """

    sender_email="sender@akvalir.ru"
    sender_password="AquaLir2024"
    receiver_email="hasenovkirill@yandex.ru"
    smtp_server="smtp.yandex.com"
    smtp_port=587
    
    # Создаем multipart сообщение
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    
    # Добавляем текст письма
    message.attach(MIMEText(body, "plain"))
    
    # Добавляем вложения
    for file_path in attachment_files:

        # decoded_path = unquote(file_path)
        decoded_path = unquote(file_path, encoding='utf-8')

        if not os.path.isfile(decoded_path):
            print(f"Файл {decoded_path} не найден, пропускаем...")
            continue
        
        # Открываем файл в бинарном режиме
        with open(decoded_path, "rb") as attachment:
            # Создаем MIME объект
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        
        # Кодируем файл в ASCII
        encoders.encode_base64(part)
        
        # Добавляем заголовок
        filename = os.path.basename(decoded_path)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={encode_filename(filename)}",
        )
        
        # Прикрепляем файл к сообщению
        message.attach(part)
    
    # Конвертируем сообщение в строку
    text = message.as_string()
    
    # Отправляем email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Включаем шифрование
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, text)
        print("Письмо успешно отправлено!")
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")

        

def encode_filename(filename):
    """Кодирует имя файла для email заголовков"""
    return email.utils.encode_rfc2231(filename, 'utf-8')