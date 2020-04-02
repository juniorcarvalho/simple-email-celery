dev:
	python manage.py runserver

docker-compose-up:
	docker-compose up -d

celery:
	celery -A sendemail purge -f
	celery -A sendemail worker -l info