FROM python:3.9


# Copy django project
COPY django_core/gunicorn-cfg.py \
    setup.py \
    .env \
    /opt/weatherme/
COPY django_core /opt/weatherme/django_core/
COPY run-server.sh /opt/weatherme/django_core/

# Copy telegram project
COPY telegram_bots /opt/weatherme/telegram_bots/

# Copy weather project
COPY weather_app /opt/weatherme/weather_app/
COPY weather_app.egg-info /opt/weatherme/weather_app/weather_app.egg-info/


# The way to solve pipenv problem
RUN pip install pipenv
COPY Pipfile* /opt/weatherme/
RUN cd /opt/weatherme/ && pipenv lock --keep-outdated --requirements > requirements.txt
RUN cd /opt/weatherme/ && pip install -r /opt/weatherme/requirements.txt


# Set up Timezone settings and install some usefull stuff
RUN apt-get update \
    && apt-get -y install \
    vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/tmp/* \
    && mkdir /config /logs


RUN apt-get update \
    && apt-get -y install \
    tzdata \
    && dpkg-reconfigure -f noninteractive tzdata \
    && ln -snf /usr/share/zoneinfo/Europe/Moscow /etc/localtime && echo Europe/Moscow > /etc/timezone \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/tmp/*
#    && locale-gen en_US.UTF-8

# All environment variables also can be set in .env file (docker use .env file at building process)
# To list all env variablles type:        $ printenv
# To check virtualenv you're working at:  $ echo $VIRTUAL_ENV
#ENV LC_ALL=en_US.UTF-8
#ENV LANG=en_US.UTF-8
#ENV LANGUAGE=en_US.UTF-8

WORKDIR /opt/weatherme/django_core/

# Django project database configuration
#RUN python manage.py makemigrations
#RUN python manage.py migrate

EXPOSE 8000

CMD ["./run-server.sh"]
#ENTRYPOINT ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#ENTRYPOINT ["/bin/bash", "-c", "tail -f /dev/null"]