-- START
insert into weather_api_db.telegram (id,username,fname,lname) values (11111112,'toVasya','Vasya','Pupkin');
insert into weather_api_db.town (id,name) values (1,'Moscow');
insert into weather_api_db.coord (town_id,latitude,longitude) values (1,'55.727638','37.619839');

-- DATETIME: 'YYYY-MM-DD HH:MM:SS.faction' '1000-01-01 00:00:00 - 9999-12-31 23:59:59'
-- TIMESTAMP: 'YYYY-MM-DD HH:MM:SS.faction' '1970-01-01 00:00:01 - 2038-01-19 03:14:07'
insert into weather_api_db.weather_wb (town_id,time_ts,temperature,site,create_dt,update_dt,delete_dt) values (1,'2020-01-01 22:23:24.123','18.23','WeatherBit',null,null,null);
insert into weather_api_db.weather_owm (town_id,time_ts,temperature,site,create_dt,update_dt,delete_dt) values (1,'2020-02-02 21:22:23.012','17.12','OpenWeatherMap',null,null,null);

