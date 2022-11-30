FROM python:3.7

WORKDIR /usr/src/app

COPY ./search_flow.yml ./
RUN pip install -U "clip-server[search]"

CMD [ "python", "-m", "clip_server", "search_flow.yml" ]
