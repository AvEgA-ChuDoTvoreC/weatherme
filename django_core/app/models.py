from django.db import models
from sqlalchemy import Column, DECIMAL, DateTime, ForeignKey, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata
# DB weather_api_db


class Telegram(Base):
    __tablename__ = 'telegram'
    __table_args__ = {'comment': 'Holds unique telegram id and username link.'}

    id = Column(INTEGER, primary_key=True, unique=True, comment='\\n')
    username = Column(String(45), nullable=False, comment='\\n')
    fname = Column(String(45))
    lname = Column(String(45))
    create_dt = Column(DateTime)
    update_dt = Column(DateTime)
    delete_dt = Column(DateTime)


class Town(Base):
    __tablename__ = 'town'
    __table_args__ = {'comment': 'List of available towns.'}

    id = Column(INTEGER, primary_key=True)
    name = Column(String(45), nullable=False, unique=True)


class Coord(Base):
    __tablename__ = 'coord'
    __table_args__ = {'comment': 'latitude - shirota, longitude - dolgota.'}

    id = Column(INTEGER, primary_key=True)
    town_id = Column(ForeignKey('town.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, unique=True)
    latitude = Column(String(45), nullable=False)
    longitude = Column(String(45), nullable=False)

    town = relationship('Town')


class WeatherOwm(Base):
    __tablename__ = 'weather_owm'
    __table_args__ = {'comment': 'Holds request data from api weather service: https://openweathermap.org/ .'}

    id = Column(INTEGER, primary_key=True)
    town_id = Column(ForeignKey('town.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    time_ts = Column(TIMESTAMP, nullable=False)
    temperature = Column(DECIMAL(4, 2), nullable=False)
    create_dt = Column(DateTime)
    update_dt = Column(DateTime)
    delete_dt = Column(DateTime)

    town = relationship('Town')


class WeatherWb(Base):
    __tablename__ = 'weather_wb'
    __table_args__ = {'comment': 'Holds request data from api weather service: https://www.weatherbit.io/ .'}

    id = Column(INTEGER, primary_key=True)
    town_id = Column(ForeignKey('town.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    time_ts = Column(TIMESTAMP, nullable=False)
    temperature = Column(DECIMAL(4, 2), nullable=False)
    create_dt = Column(DateTime)
    update_dt = Column(DateTime)
    delete_dt = Column(DateTime)

    town = relationship('Town')

