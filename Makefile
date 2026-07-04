.PHONY: install migrate seed run test docker-up

install:
	pip install -r requirements.txt

migrate:
	python manage.py migrate

seed:
	python manage.py seed_demo

run:
	python manage.py runserver

test:
	python manage.py check
	python manage.py test

docker-up:
	docker compose up --build
