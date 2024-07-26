FROM python:3.12.2-alpine

WORKDIR /LBS

RUN pip install --no-cache-dir poetry==1.8.3

COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN poetry install --no-dev

COPY . .

CMD ["poetry", "run", "gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]

