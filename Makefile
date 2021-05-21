.PHONY: build dev dev_server prod prod_server shell stop

build:
	@echo "Building image:"
	docker-compose build

dev:
	@echo "Starting container(s) in dev mode:"
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d

dev_server: dev
	@echo "Starting app server in dev mode:"
	docker-compose exec app ./deploy/tools/dev_server

prod:
	@echo "Starting containers in prod mode:"
	docker-compose up -d

prod_server: prod
	@echo "Starting app server in prod mode:"
	docker-compose exec app ./deploy/tools/server

shell: dev
	@echo "Getting a shell inside the container:"
	docker-compose exec app bash

stop:
	@echo "Bringing Docker down:"
	docker-compose down
