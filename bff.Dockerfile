FROM python:3.7

WORKDIR /usr/src/app

COPY ./listing-details.json ./
COPY ./requirements.txt ./
COPY ./bff_server.py ./
RUN pip install -U -r requirements.txt

CMD [ "python", "-m", "flask", "--app", "bff_server", "run" ]