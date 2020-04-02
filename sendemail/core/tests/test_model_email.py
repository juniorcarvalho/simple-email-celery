from sendemail.core.models import Email


def test_model():
    email = Email(email='test@test.com',subject='subject', body='body')
    assert isinstance(email, Email)
    assert email.email == 'test@test.com'
    assert email.subject == 'subject'
    assert email.body == 'body'
