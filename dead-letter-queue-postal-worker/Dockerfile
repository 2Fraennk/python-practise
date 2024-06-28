FROM debian:stable-20240110

# Custom cache invalidation
ARG CACHEBUST=1
ARG username
ARG password

ENV TZ="Europe/Berlin"

WORKDIR /usr/local
RUN apt-get update
RUN apt-get install -y sudo
RUN apt-get install -y git \
    python3 \
    python3-poetry
RUN git --version
RUN python3 --version

RUN git clone https://$username:$password@github.com/2Fraennk/python-practise.git .
RUN git switch main
WORKDIR /usr/local/dead-letter-queue-postal-worker
RUN poetry config virtualenvs.create false
RUN poetry install
RUN playwright install --with-deps firefox

ENV PYTHONPATH "${PYTHONPATH}:/usr/local/dead-letter-queue-postal-worker/src"

WORKDIR /usr/local/dead-letter-queue-postal-worker/src
RUN touch ./properties.py

CMD ["python3", "-m", "main"]