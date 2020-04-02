import json
from unittest import mock

from rest_framework.test import APIClient

client = APIClient()
DATA = {
    'email': 'test@gmail.com',
    'subject': 'subject',
    'body': 'body',
}


def test_view_sendemail():
    with mock.patch('sendemail.core.api.tasks.send_simple_email') as email:
        response = client.post('/api/email/', format='json', data=DATA)
        assert response.status_code == 201
        assert json.loads(response.content) == {
            'email': 'test@gmail.com',
            'subject': 'subject',
            'body': 'body'
        }
