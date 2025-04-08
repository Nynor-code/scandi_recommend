run:
	python src/main.py

notebook:
	jupyter notebook

test:
	pytest tests/

docker-build:
	docker build -t ds-project .

docker-run:
	docker run -p 8888:8888 -v $(PWD):/app ds-project

app_run:
	streamlit run src/app.py