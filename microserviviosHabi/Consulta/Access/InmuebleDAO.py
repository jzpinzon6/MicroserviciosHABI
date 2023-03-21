
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------------------------------------
# Función: Capa de Acceso o Objeto de Acceso a Datos
# Autor: Javier Pinzón.
# Version: 1
# Descripción:
#
#   La funcionalidad de esta capa es acceder a la base de datos y recuperar los inmuebles que coinciden con los filtros
#   aplicados por el usuario. Este componente puede tener una clase InmuebleDAO con métodos para realizar la consulta
#   de inmuebles con filtros aplicados.

# Objeto de Acceso a Datos:

class InmuebleDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def buscar_inmuebles(self, filtros):
        # construir la consulta
        consulta = "SELECT * FROM inmuebles WHERE "
        valores = []
        for clave, valor in filtros.items():
            consulta += f"{clave} = %s AND "
            valores.append(valor)
        consulta = consulta[:-5]

        # ejecutar la consulta y mapear los resultados a objetos Inmueble
        cursor = self.conexion.cursor()
        cursor.execute(consulta, valores)
        resultado = []
        for fila in cursor.fetchall():
            resultado.append(Inmueble(*fila))
        return resultado