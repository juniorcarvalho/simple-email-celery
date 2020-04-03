<img src="https://img.shields.io/apm/l/vim-mode.svg" alt="APM">[![Build Status](https://travis-ci.org/juniorcarvalho/simple-email-celery.svg?branch=master)](https://travis-ci.org/juniorcarvalho/simple-email-celery)

# simple-email-celery
A simple api for sending email using Django, Django Rest Framework and Celery.

We use docker to run a redis instance

# Start
1. Clone project:
`git clone https://github.com/juniorcarvalho/simple-email-celery.git`

2. Create a virtualenv:
`python -m venv .venv`

3. Active virtualenv:
`source .venv/bin/activate`

4. Copy .env-sample to .env and configure your settings.

5. Install requirements:
`pip install -r requirements.txt`

6. Run redis container:
`make docker-compose-up` or `docker-compose up -d` 

7. Run Celery:
`make celery` or
`celery -A sendemail worker -l info`

8. Run project:
`make dev` or `python manage.py runserver`

# Tests
`pip install -r requirements-test.txt`

`make test` or `pytest -s -vvv`
