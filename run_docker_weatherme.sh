#!/bin/bash
#
# run_docker_weatherme.sh
#

hack_file="$(echo $(ls -a | grep -wo '\.env'))"
if [[ -z $hack_file ]] ; then
  echo -e "No file .env found!\nexit 1"
  exit 1
fi

echo "Using variables:"
while IFS='=' read -r var text; do
  echo "${var} = ${text}"
#  ${var}="${text}"
done < ${hack_file}


#sed 's|TAR_QUEUE|cons_{queue_name}|g'


if [[ -f 'db-docker-compose.yml' && -f 'docker-compose.yml' && -f 'Dockerfile' ]]; then
  docker-compose -f db-docker-compose.yml up -d
  docker-compose -f docker-compose.yml up --force-recreate
else
  echo -e "One or more files not found:\ndb-docker-compose.yml\ndocker-compose.yml\nDockerfile\nexit 1"
  exit 1
fi

weather_me=$(docker ps -a | grep "weather_me" | awk '{ print $1 }')
nginx_me=$(docker ps -a | grep "nginx_me" | awk '{ print $1 }')
ubuntu_db=$(docker ps -a | grep "ubuntu_db" | awk '{ print $1 }')
#mysql_db=$(docker ps -a | grep "mysql_db" | awk '{ print $1 }')
docker rm -f ${weather_me} ${nginx_me} ${ubuntu_db}
echo "Finnish!"