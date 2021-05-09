#!/bin/bash
#
# run-server.sh
#

python manage.py makemigrations
python manage.py migrate
gunicorn --config gunicorn-cfg.py core.wsgi

#set -e
#host="$1"
#shift
#cmd="$@"
#until mysql -h"172.19.0.9" -P"3306" -u"${ENV_MYSQL_USER}" -p"${ENV_MYSQL_PASSWORD}" -D"${ENV_MYSQL_DATABASE}" ; do
#  >&2 echo "MySQL is unavailable - sleeping"
#  sleep 1
#done
#>&2 echo "MySQL is up - executing command"