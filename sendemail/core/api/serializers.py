from rest_framework import serializers

from sendemail.core.models import Email


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['email', 'subject', 'body']
