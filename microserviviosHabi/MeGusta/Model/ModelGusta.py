# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------------------------------------
# Función: Capa de Modelo en el patron MVC.
# Autor: Javier Pinzón.
# Version: 1
# Descripción:
#
#   La funcionalidad de esta capa es representar los datos de los inmuebles almacenados en la base de datos.
#   Este componente puede tener una clase Inmueble con los atributos dirección, ciudad, estado, precio de venta,
#   descripción y estado del inmueble


# importar librerías necesarias
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# crear la base de datos y la sesión
engine = create_engine('sqlite:///likes.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

# crear el modelo
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Like(Base):
    __tablename__ = 'likes'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    property_id = Column(Integer, ForeignKey('properties.id'), primary_key=True)
    user = relationship("User", backref="likes")
    property = relationship("Property", backref="likes")

