FROM nikolaik/python-nodejs:python3.10-nodejs18

RUN apt-get update
USER pn

ENV LANG=C.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=C.UTF-8
ENV MODE=production
ENV APP_PATH=/home/pn/app
ENV PATH="${PATH}:/home/pn/.local/bin"
WORKDIR $APP_PATH
COPY --chown=pn:pn . .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
