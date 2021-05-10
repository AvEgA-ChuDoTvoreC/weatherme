# Weatherme


<p align="">
    <a href="https://python.org/downloads/release/python-390/">
        <img src="https://img.shields.io/badge/python-v3.9-blue" 
            alt="Python"></a>
    <a href="https://docs.djangoproject.com/en/3.1/releases/2.2.10/">
        <img src="https://img.shields.io/badge/django-v2.2.10-brightgreen?logo=django" 
            alt="Django"></a>
    <a href="https://discord.gg/">
        <img src="https://img.shields.io/badge/chat-on%20line-brightgreen?logo=discord"
            alt="chat on Discord"></a>
    <a href="https://twitter.com/intent/follow?screen_name=ChuDoTvoreC">
        <img src="https://img.shields.io/badge/-%40ChuDoTvoreC-white?style=social&logo=twitter"
            alt="follow on Twitter"></a>
</p>
<p>
    <a href="">
    <img src="https://img.shields.io/badge/tested%20on-MacOS-orange?logo=macos"
    alt="Test platform MacOS"></a>
</p>


Django project to get weather from [OWM](https://openweathermap.org) and [WB](https://weatherbit.io) by **API**, **TelegramBot** or **Browser** html-page.

<br />

## Table of Contents

* [TODO check](#todo-check)
* [Installation](#installation)
* [Quick start](#quick-start)
* [Building docker containers](#Building-docker-containers)
* [API communication](#api-communication)
* [Tests](#tests)
* [File Structure](#file-structure)
* [Some pictures](#some-pictures)
* [Useful stuff](#useful-stuff)
* [Original Task text](#original-task-text)

<br />

### TODO check

- [x] Write tests
- [ ] Publish on Heroku
- [ ] GitHub CI/CD build
- [ ] Add telegram bot
- [ ] Write templates

<br />

### Installation

Clone the repo:
```bash
$ git clone https://github.com/AvEgA-ChuDoTvoreC/weatherme.git
$ cd weatherme/
```

Set up virtual environment:
```bash
Install pipenv https://docs.pipenv.org/

$ pip install pipenv
$ pipenv install --dev
$ pipenv shell
```

Create [.env](#some-pictures) file:
```.dotenv
DEBUG=True
SECRET_KEY=<your_django_secret_key>
SERVER=<your_server>
OWM_API_KEY=<your_openweathermap_API_key>
OWM_API_URL=https://api.openweathermap.org/data/2.5/weather
WB_API_KEY=<your_weatherbit_API_key>
WB_API_URL=http://api.weatherbit.io/v2.0/current
ENV_MYSQL_DATABASE=<your_data_base_name>
ENV_MYSQL_USER=<your_data_base_user>
ENV_MYSQL_PASSWORD=<your_data_base_user_password>
ENV_MYSQL_ROOT_PASSWORD=<your_data_base_root_password>
ENV_MYSQL_TIMEZONE=<your_data_base_timezone>
ENV_MYSQL_ROOT_HOST=172.19.0.9
ENV_MYSQ_PORT_EXTERNAL=3307
ENV_MYSQ_PORT_INTERNAL=3306
```

<br />

### Quick start

Choose one of shell scripts...
```bash
$ ./run_docker_weatherme.sh
$ ./run_weatherme.sh
```

...or build it up by your own:

<br />

Start db:
```bash
$ docker-compose -f db-docker-compose.yml up -d
```

Make migrations:
```bash
$ cd django_core/
$ python manage.py makemigrations
$ python manage.py migrate
```

Run the server:
```bash
$ python manage.py runserver
```

<br />

### Building docker containers

To start project in docker containers follow this steps:
- First you need [Docker](https://docs.docker.com/docker-for-mac/install/) installed on your PC. 
- Next step is to install [Docker-compose](https://docs.docker.com/compose/install/). 
- Run the commands below
```bash
$ docker-compose -f db-docker-compose.yml up -d
$ docker-compose -f docker-compose.yml up

    ## If you face problem ->
    ## First comment migrations in Dockerfile and after rebuild
    ## Try:
    
$ docker exec -it weather_me bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

### API communication

Start with:
```bash
Main page:
    http://127.0.0.1:8000/
    
API:
    add town list (POST):
        http://127.0.0.1:8000/api/v1/weather/town/
            {"town_list": ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Kazan", "Chelyabinsk", "Volgograd", "Magnitogorsk", "Kemerovo", "Vladimir"]}
    check returnd town ids (POST):
        http://127.0.0.1:8000/api/v1/weather/town/1/
    from 1 to 5 (POST):
        http://127.0.0.1:8000/api/v1/weather/town/1/5/
        
```

<br />

### Tests

For tests:
```bash
$ cd django_core
$ export DJANGO_SETTINGS_MODULE=django_core.core.settings
$ python -m pytest tests/

    ## If you face problem -> 
    ## Add root user to mysql with no password and
    ## try `django_core/core/settings.py` uncomment `DATABASES=` (FOR TESTS)
```

<br />

### File Structure

```
< PROJECT ROOT >
    .
    ├── db_conf
    │   ├── db_diagram/          # MySQL Diagram file
    │   └── sql_scripts/         # SQL scripts to check database tables
    │
    ├── django_core/             # Django project
    │   ├── api/                 # API appllication
    │   ├── app/
    │   ├── authentication/
    │   ├── core/
    │   └── manage.py
    │    
    ├── Dockerfile               # Weatherme Dockerfile
    ├── db-docker-compose.yml    # Compose for database
    ├── docker-compose.yml       # Compose for main project
    ├── nginx/
    ├── tests/                   # Tests folder
    ├── weather_app/             # Package with weather requests
    └── weather_app.egg-info/    # Package egg

```

<br />

### Some pictures

![MySQL_EER_Diagram](https://github.com/AvEgA-ChuDoTvoreC/weatherme/blob/main/db_conf/pic/mysql_eer_diagram.png)

![ENV_File_Example](https://github.com/AvEgA-ChuDoTvoreC/weatherme/blob/main/db_conf/pic/env_file_example.png)



<br />

### Useful stuff

<br />

Get auto-file from database generated by django. Configure ```DATABASES``` variable at ```settings.py``` to change db.
Read more at [Django ORM Cookbook](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/existing_database.html)
```bash
$ python manage.py inspectdb > models.py
```
<br />

Directly login to a remote mysql console. Read more at [StackOverflow](https://stackoverflow.com/questions/15872543/access-mysql-remote-database-from-command-line)
```bash
$ mysql -u {username} -p'{password}' \
     -h {remote server ip or name} -P {port} \
     -D {DB name}
```

<br />

Installation of ```yourmodule``` via Pipenv same as for Pip. Read more at [StackOverflow](https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder) :
```python
# setup.py  -- in main project directory
from setuptools import setup, find_packages

setup(name='your_module_folder', 
      version='1.0', 
      packages=find_packages())
```
```bash
$ pipenv install -e .
```

<br />

If ```models.py``` was edited and DataBase need changes... Run next:
```bash
$ python manage.py makemigrations [yourapp]
$ python manage.py migrate [yourapp]
```

<br />

Get/Load MySQL Dump file via mysqldump. Check [StackOverflow](https://stackoverflow.com/questions/105776/how-do-i-restore-a-dump-file-from-mysqldump):
```bash
$ mysqldump -uDBUSER -pUSERPASSWORD DBNAME > DUMPFILENAME.sql
$ mysql -uDBUSER -pUSERPASSWORD DATABASE < BACKUP.sql
```

<br />

Want to see docker build progress as it was before? Check [StackOverflow](https://stackoverflow.com/questions/64804749/docker-build-not-showing-any-output-from-commands):
```bash
$ docker build --progress=plain .
```



<br />

To get list of towns to send via API use next link to [Wiki](https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Russia_by_population) or [Bulk download](https://openweathermap.org/current#bulk) at OpenWeatherMap.

<br />

### Original Task text

```
Есть два API. Например, сайты погоды:
https://openweathermap.org/current#current_JSON
https://www.weatherbit.io/api/swaggerui/weather-api-v2#!/Current32Weather32Data/get_current_city_id_city_id
 
Необходимо получить и сохранить в БД список значений 
для десятка городов на ваш выбор, предоставляемый API сайтов, 
в которых будет указан 
(город, время, широта, долгота и температура), 
а затем предоставить для фронтенда route для GET-запроса. 
Route должен содержать весь список, сохраненных значений 
и дополнительно необходимо указывать тот сайт, 
из которого была изначально получена информация.
 
Это не совсем ТЗ на разработку, а, скорее, описание, 
с возможностью Вам показать, какие приемы вы бы использовали.
Хорошо было бы увидеть в задании юнит-тесты.
```

<br />

GL & HF