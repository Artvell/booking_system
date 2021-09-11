"""файл с вьюхой ActivateUserView для активации юзера"""

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from authentification.functions import Encoder, SendMail
from authentification.models import User, TmpPass

class ActivateUserView(APIView):
    """класс для активации аккаунта юзера"""
    def get(self, request, user):
        """метод для обработки гет запроса
        и дальнейшей активации аккаунта
        """
        decoded_username = Encoder(user).decode()
        try:
            user = User.objects.get(username=decoded_username)
        except User.DoesNotExist:
            return Response({"error":"Несуществующий или удаленный аккаунт"},
                            status=status.HTTP_400_BAD_REQUEST)
        if user:
            if not user.is_active:
                tmp_user = TmpPass.objects.get(username=decoded_username)
                user.is_active = True
                user.save()
                resp = {"status":"Аккаунт активирован"}
                text = f"Логин: {user.username}\nПароль: {tmp_user.password}"
                SendMail(text,[user.email]).send()
                tmp_user.delete()
                return Response(resp,status=status.HTTP_200_OK)
            else:
                return Response({"error":"Этот аккаунт уже активен"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error":"Incorrect link"},status=status.HTTP_400_BAD_REQUEST)
