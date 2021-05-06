select weather_api_db.town.name,weather_api_db.coord.latitude,weather_api_db.coord.longitude from weather_api_db.town
natural left join weather_api_db.coord;

select *
from weather_api_db.town as t 
join weather_api_db.coord as c on t.id=c.town_id
join weather_api_db.weather_wb as wb on t.id=wb.town_id
join weather_api_db.weather_owm as owm on t.id=owm.town_id
order by t.id;

select *
from weather_api_db.town as t 
natural left join weather_api_db.coord as c
natural left join weather_api_db.weather_wb as wb
natural left join weather_api_db.weather_owm as owm
order by t.id;
