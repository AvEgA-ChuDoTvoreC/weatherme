#!/bin/bash
#
# run-server.sh
#

python /opt/weatherme/telegram_bots/bot_weather/main.py &
weather_pid=$(echo $!)
python /opt/weatherme/telegram_bots/bot_matrix/main.py &
matrix_pid=$(echo $!)

python manage.py makemigrations
python manage.py migrate
gunicorn --config gunicorn-cfg.py core.wsgi

#kill -9 $(echo ${weather_pid})
#kill -9 $(echo ${matrix_pid})
echo "Need to be killed:"
echo ${weather_pid}
echo ${matrix_pid}
echo "Finnish!"

#set -e
#host="$1"
#shift
#cmd="$@"
#until mysql -h"172.19.0.9" -P"3306" -u"${ENV_MYSQL_USER}" -p"${ENV_MYSQL_PASSWORD}" -D"${ENV_MYSQL_DATABASE}" ; do
#  >&2 echo "MySQL is unavailable - sleeping"
#  sleep 1
#done
#>&2 echo "MySQL is up - executing command"