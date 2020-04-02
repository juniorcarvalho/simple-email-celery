from django.db import models


class Email(models.Model):
    email = models.EmailField('Email')
    subject = models.CharField('Subject', max_length=256)
    body = models.TextField('Body')

    def __str__(self):
        return 'Email: {0}'.format(self.email)
