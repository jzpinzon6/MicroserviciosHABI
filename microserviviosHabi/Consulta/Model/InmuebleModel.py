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


import MySQLdb
from urllib.parse import urlparse, parse_qs
import urllib.parse
import sqlite3

class InmuebleModel:

    # Función para iniciar el servidor HTTP

    def run(self):
        print('Iniciando servidor...')

        # Especificamos la dirección IP y el puerto donde se ejecutará el servidor
        db_servidor = ('3.130.126.210', 3309)
        db_user = "pruebas"
        db_pass = "VGbt3Day5R"
        db_schema = "habi_db"
        httpd = HTTPServer(direccion_servidor, InmuebleController)

        parameters = [db_servidor, db_user, db_pass, db_schema]
        link = MySQLdb.connect(*parameters)
        pointer = link.cursor()
        pointer.execute(query)
        if (query.upper().startswith('SELECT')):
            data = pointer.fetchall()
        else:
            link.commit()
            if query.upper().startswith('INSERT'):
                data = pointer.lastrowid
            else:
                data = None
        pointer.close()
        link.close()

        return data

    def __init__(self, direccion, ciudad, estado, precio, descripcion):
        self.direccion = direccion
        self.ciudad = ciudad
        self.estado = estado
        self.precio = precio
        self.descripcion = descripcion
