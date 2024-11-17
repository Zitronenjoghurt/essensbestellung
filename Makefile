dev-up:
	docker compose -f docker/docker-compose.dev.yml up -d --build

dev-down:
	docker compose -f docker/docker-compose.dev.yml down

dev-clean:
	docker compose -f docker/docker-compose.dev.yml down -v --remove-orphans

dev-restart: dev-down dev-up

prod-up:
	docker compose -f docker/docker-compose.prod.yml up -d --build

prod-down:
	docker compose -f docker/docker-compose.prod.yml down

prod-clean:
	docker compose -f docker/docker-compose.prod.yml down -v --remove-orphans

prod-restart: prod-down prod-up

clean: dev-clean prod-clean

logs-dev:
	docker compose -f docker/docker-compose.dev.yml logs -f

logs-prod:
	docker compose -f docker/docker-compose.prod.yml logs -f