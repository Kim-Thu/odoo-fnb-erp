SHELL := /bin/bash

.PHONY: up down restart logs shell db-shell lint test install-core

up:
	docker compose --env-file .env up -d

down:
	docker compose --env-file .env down

restart: down up

logs:
	docker compose --env-file .env logs -f --tail=200 odoo db

shell:
	docker compose --env-file .env exec odoo bash

db-shell:
	docker compose --env-file .env exec db psql -U $${POSTGRES_USER:-odoo} -d $${POSTGRES_DB:-postgres}

install-core:
	docker compose --env-file .env exec odoo odoo --stop-after-init -d fnb_dev -i fnb_core --db_host=db --db_user=$${POSTGRES_USER:-odoo} --db_password=$${POSTGRES_PASSWORD}

lint:
	python -m compileall addons

# Requires the database and Odoo container to be running.
test:
	docker compose --env-file .env exec odoo odoo --stop-after-init -d fnb_test -i fnb_core --test-enable --log-level=test --db_host=db --db_user=$${POSTGRES_USER:-odoo} --db_password=$${POSTGRES_PASSWORD}
