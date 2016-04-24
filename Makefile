.PHONY: clean deps migrations migrate runserver

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  clean       => to clean clean all automatically generated files"
	@echo "  deps        => to update Python packages"
	@echo "  migrations  => to create new migration(s)"
	@echo "  migrate     => to update database schema"
	@echo "  runserver   => to run development server"

clean:
	find src/ -name \*.pyc -delete
	find src/ -name \*__pycache__ -delete

deps:
	pip install -U -r requirements/local.txt

migrations:
	cd ./src && alembic revision --autogenerate -m "auto"

migrate:
	cd ./src && alembic upgrade head

runserver:
	cd ./src && python main.py
