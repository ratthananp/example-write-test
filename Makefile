up:
	docker-compose up

attach-django:
	bash -c "./scripts/wait-for-postgres.sh postgres"
	bash -c "./scripts/wait-for-it.sh --timeout=0 localhost:8000"
	docker-compose exec django sh -c "pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate && uvicorn --host 0.0.0.0 --reload main.asgi:application"

.migrate:
	docker-compose exec django python manage.py migrate

migrate:
	docker-compose exec django python manage.py migrate $(filter-out $@,$(MAKECMDGOALS))

.migrations:
	docker-compose exec django python manage.py makemigrations

migrations:
	docker-compose exec django python manage.py makemigrations $(filter-out $@,$(MAKECMDGOALS))

migrations-migrate: .migrations .migrate

build-backend:
	docker-compose build django

init-data:
	docker-compose exec django python manage.py init_data $(filter-out $@,$(MAKECMDGOALS))

pip-compile:
	docker-compose exec django sh -c "pip install pip-tools && pip-compile"

delete-migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc" -delete

reset-migrations: delete-migrations reset-db migrations-migrate

lint-backend:
	docker-compose exec django flake8 $(filter-out lint,$(filter-out $@,$(MAKECMDGOALS)))

test-backend:
	docker-compose exec django python manage.py test $(filter-out test,$(filter-out $@,$(MAKECMDGOALS))) --parallel

test-backend-no-parallel:
	docker-compose exec django python manage.py test $(filter-out test,$(filter-out $@,$(MAKECMDGOALS)))

down:
	docker-compose down --remove-orphans

%:
	@:
