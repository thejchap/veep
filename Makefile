format:
	@python -m black .
	@python -m isort .

install:
	@pip install -r requirements.txt

run.dev:
	@uvicorn example:APP --port 8000 --host 0.0.0.0
