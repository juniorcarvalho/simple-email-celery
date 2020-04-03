from django.conf import settings


def test_app_companies_is_configured():
    assert 'sendemail.core' in settings.INSTALLED_APPS
