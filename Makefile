PROJECT_NAME = "pangolin"
DB_NAME = "pangolin"

default: req local_settings db collect_static test end

local_settings:
	@echo "Emitting local development settings module"
	@cp settings/local.py.example settings/local.py

req:
	@echo "Installing requirements"
	@pip install -r requirements/dev.txt

db: dropdb createdb migrate loaddata

createdb:
	@echo "Creating PostgreSQL database $(DB_NAME)"
	@make -i _createdb >> /dev/null

_createdb:
	@createdb $(DB_NAME)

dropdb:
	@echo "Destroying PostgreSQL database $(DB_NAME)"
	@make -i _dropdb >> /dev/null

_dropdb:
	@dropdb $(DB_NAME)

migrate:
	@echo "Running migrations"
	@python manage.py migrate

loaddata:
	@echo "Loading additional data fixtures"
	@python manage.py filldb

run:
	@python run.py

runserver:
	@python manage.py runserver

runpub:
	@python manage.py runserver 0.0.0.0:8000

test:
	@coverage run -m py.test
	@coverage report
	@coverage erase

shell:
	@python manage.py shell_plus

end:
	@echo "You can now run development server using 'make run' command"

clean:
	@echo "Cleaning *.pyc files"
	@find . -name "*.pyc" -exec rm -f {} \;

clean_images:
	@echo "Cleaning *.jpg files"
	@rm -rf public/media/cache

clean_public:
	@echo "Cleaning *.jpg files"
	@rm -rf public/*

collect_static:
	python manage.py collectstatic -l --noinput

compilemessages:
	python manage.py compilemessages

makemessages:
	python manage.py makemessages -l ru -e 'jhtml,html,txt'

flush:
	@echo "Flushing redis"
	@redis-cli FLUSHALL
