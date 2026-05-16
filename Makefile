.PHONY: install lint docker-run

install:
	pip install -r requirements.txt

lint:
	flake8 src/
	ruff check src/

docker-run:
	docker-compose up --build