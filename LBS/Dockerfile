FROM python:3.12.2-alpine

WORKDIR /LBS

COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]