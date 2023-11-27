.PHONY: build up shell down lint

build:
	docker-compose build

up:
	docker-compose up -d

shell:
	docker-compose exec python-app /bin/bash

down:
	docker-compose down

lint:
	docker-compose exec python-app flake8 src

lint-fix:
	docker-compose exec python-app autopep8 --in-place --recursive src
	