up:
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f --tail=200

restart:
	docker compose down && docker compose up -d --build

ps:
	docker compose ps
