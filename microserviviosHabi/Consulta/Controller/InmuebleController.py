# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------------------------------------
# Función: Capa de Controlador en el patron MVC.
# Autor: Javier Pinzón.
# Version: 1
# Descripción:
#
#   La funcionalidad de esta capa es manejar las solicitudes HTTP y procesar los filtros aplicados por el usuario.
#   Este componente puede recibir los parámetros de la consulta de la URL y llamar al componente DAO para obtener los
#   inmuebles que coinciden con los filtros aplicados. El controlador también puede ser responsable de transformar los
#   datos obtenidos en un formato JSON para enviarlos como respuesta al usuario.

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3

class InmuebleController:
    def __init__(self):
        self.dao = InmuebleDAO()

    def obtener_inmuebles(self, filtro_año=None, filtro_ciudad=None, filtro_estado=None):
        inmuebles = self.dao.obtener_inmuebles(filtro_año, filtro_ciudad, filtro_estado)
        inmuebles_dict = [vars(inmueble) for inmueble in inmuebles]
        return inmuebles_dict
