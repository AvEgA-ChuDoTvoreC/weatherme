#!/bin/bash
#
# run_weatherme.sh
#

hack_file="$(echo $(ls -a | grep -wo '\.env'))"
if [[ -z $hack_file ]] ; then
  echo -e "No file .env found!\nexit 1"
  exit 1
fi


if [[ -f 'db-docker-compose.yml' ]]; then
  docker-compose -f db-docker-compose.yml up -d
else
  echo -e "One or more files not found:\ndb-docker-compose.yml\nexit 1"
  exit 1
fi

export DJANGO_SETTINGS_MODULE="django_core.core.settings"

python -m pytest django_core/tests/test_args.py
status=$?

if [ ${status} -eq 0 ]; then
  echo "status: ${status}"
  echo "[OK]"
else
  echo "status: ${status}"
  echo "exiting"
  exit 1
fi
#sed 's|TAR_QUEUE|cons_{queue_name}|g'


echo "Using variables:"
while IFS='=' read -r var text; do
  echo "${var}=${text}"
#  export ${var}="${text}"
done < ${hack_file}


export ENV_MYSQL_ROOT_HOST="127.0.0.1"
export ENV_MYSQ_PORT_INTERNAL="3307"
echo "Args changed:"
echo 'ENV_MYSQL_ROOT_HOST="127.0.0.1"'
echo 'export ENV_MYSQ_PORT_INTERNAL="3307"'


python telegram_bots/bot_weather/main.py &
weather_pid=$(echo $!)
#echo $$ $BASHPID
python telegram_bots/bot_matrix/main.py &
matrix_pid=$(echo $!)

python django_core/manage.py makemigrations
python django_core/manage.py migrate
python django_core/manage.py runserver

ubuntu_db=$(docker ps -a | grep "ubuntu_db" | awk '{ print $1 }')

docker rm -f ${ubuntu_db}
kill -9 $(echo ${weather_pid})
kill -9 $(echo ${matrix_pid})
echo "killed:"
echo ${weather_pid}
echo ${matrix_pid}
echo "Finnish!"

#while IFS=[разделитель напр - ,/=] read -r line; do
#if [[ "$line" == *"ip"* ]] ; then
#echo "$line
#fi
#done < book
# done < <$(cat book)
# done <<< $(cat book)