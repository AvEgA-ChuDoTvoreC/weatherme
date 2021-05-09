#!/bin/bash
#
# run_weatherme.sh
#

hack_file="$(echo $(ls -a | grep -wo '\.env'))"

while IFS='=' read -r var text; do
  echo "${var} = ${text}"
  ${var}=${text}
done < ${hack_file}

if [[ -f 'db-docker-compose.yml' ]]; then
  docker-compose -f db-docker-compose.yml up -d
else
  echo -e "One or more files not found:\ndb-docker-compose.yml\nexit 1"
  exit 1
fi

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

ubuntu_db=$(docker ps -a | grep "ubuntu_db" | awk '{ print $1 }')

docker rm -f ${ubuntu_db}
echo "Finnish!"

#while IFS=[разделитель напр - ,/=] read -r line; do
#if [[ "$line" == *"ip"* ]] ; then
#echo "$line
#fi
#done < book
# done < <$(cat book)
# done <<< $(cat book)