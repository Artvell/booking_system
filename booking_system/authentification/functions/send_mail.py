"""файл с классом SendMail для отправки мэйлов"""
from django.core.mail import send_mail
from django.conf import settings
class SendMail:
    """класс для отправки мэйлов с полученным текстом полученным адресатам"""
    def __init__(self,text,recipient_list):
        self.text = text
        self.recipient_list = recipient_list
    def send(self):
        """метод для отпправки мэйла"""
        subject = 'Devu Build'
        send_mail( subject, self.text, settings.EMAIL_HOST_USER, self.recipient_list )
