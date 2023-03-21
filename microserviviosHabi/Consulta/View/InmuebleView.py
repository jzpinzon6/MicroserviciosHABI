# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------------------------------------
# Función: Capa de Vista en el patron MVC.
# Autor: Javier Pinzón.
# Version: 1
# Descripción:
#
#   La funcionalidad de esta capa es manejar la interfaz de usuario y permite la interacción del usuario con
#   la aplicación. En este caso, la vista puede ser una interfaz web que permite al usuario aplicar los filtros y ver
#   los resultados de la consulta

import MySQLdb
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import urllib.parse
import sqlite3

class InmuebleView:

    def __init__(self, controller):
        self.controller = controller


    def do_GET(self):
        # procesar la consulta de la URL
        parsed_url = urllib.parse.urlparse(self.path)
        request = {'args': urllib.parse.parse_qs(parsed_url.query)}

        # buscar inmuebles que coinciden con los filtros aplicados
        resultado = self.controller.buscar_inmuebles(request)

        # enviar la respuesta al usuario
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(resultado.encode())

#    def do_GET(self):
#            query_params = parse_qs(urlparse(self.path).query)
#            filtro_año = query_params.get('año_construccion', None)
#            filtro_ciudad = query_params.get('ciudad', None)
#            filtro_estado = query_params.get('estado', None)

#            controller = InmuebleController()
#            inmuebles = controller.obtener_inmuebles(filtro_año, filtro_ciudad, filtro_estado)

#            self.send_response(200)
#            self.send_header('Content-Type', 'application/json')
#            self.end_headers()
#            self.wfile.write(json.dumps(inmuebles).encode('utf-8'))