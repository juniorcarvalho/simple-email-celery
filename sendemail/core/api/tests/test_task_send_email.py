from unittest import mock

from sendemail.core.api.tasks import send_simple_email


def test_task_simple_send_email():
    with mock.patch('sendemail.core.api.tasks.send_simple_email') as email:
        result = send_simple_email('subject', 'body', 'email_from', ['to'])
        assert result == 1
