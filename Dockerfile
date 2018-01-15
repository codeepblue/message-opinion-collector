FROM python:3

COPY . /src

RUN cd /src \
    && pip install -r ./requirements.txt

ENV FLASK_APP=/app/app.py
ENV FLASK_DEBUG=1

CMD ["flask", "run"]
