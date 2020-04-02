from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from sendemail.core.models import Email
from .serializers import EmailSerializer
from .tasks import send_simple_email


class EmailViewSet(ModelViewSet):
    http_method_names = ['post']
    serializer_class = EmailSerializer
    queryset = Email.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        subject = serializer.data['subject']
        email = serializer.data['email']
        body = serializer.data['body']

        send_simple_email.delay(subject, body, settings.EMAIL_HOST_USER, [email])

        return Response(serializer.data, status=status.HTTP_201_CREATED)
