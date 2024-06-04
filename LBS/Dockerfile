FROM python:3.12.2-alpine

WORKDIR /LBS

RUN pip install poetry

COPY ./pyproject.toml .

COPY ./poetry.lock .

RUN poetry install

COPY . .

CMD ["poetry", "run", "flask", "--app", "app", "run", "--host=0.0.0.0"]