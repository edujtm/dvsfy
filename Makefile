

.PHONY: run_backend run_frontend build

run_backend:
	poetry run python manage.py runserver 

run_frontend:
	cd frontend && npm run start

build:
	npm run build --prefix frontend
	rm -rf ./assets
	mv ./frontend/build ./assets
	mv assets/index.html assets/app.html
