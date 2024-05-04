FROM python:3.12.2-alpine

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

COPY ./app .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]