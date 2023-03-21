# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------------------------------------
# Función: Pruebas Unitarias al Microservicio de Consultas.
# Autor: Javier Pinzón.
# Version: 1


import unittest

class InmuebleTest:
    def test_consultar_inmuebles(self):
        # Conectar a la base de datos
        db = db_servidor()

        # Consultar inmuebles sin filtros
        inmuebles = consultar_inmuebles({}, "InmuebleView", db)

        # Verificar que la lista de inmuebles esté vacía
        assert inmuebles == []

    def consultar_inmuebles(filtros, estado, db):
        # Construir la consulta SQL
        consulta = "SELECT direccion, ciudad, estado, precio, descripcion FROM inmuebles WHERE estado = %s"

        # Agregar los filtros a la consulta
        if filtros.get("anno"):
            consulta += " AND anno = %s"
        if filtros.get("ciudad"):
            consulta += " AND ciudad = %s"
        if filtros.get("estado"):
            consulta += " AND estado = %s"

        # Ejecutar la consulta
        cursor = db.cursor()
        cursor.execute(consulta, (estado, filtros.get("anno"), filtros.get("ciudad"), filtros.get("estado")))
        resultados = cursor.fetchall()

        # Construir la lista de inmuebles
        inmuebles = []
        for resultado in resultados:
            inmueble = {
                "direccion": resultado[0],
                "ciudad": resultado[1],
                "estado": resultado[2],
                "precio": resultado[3],
                "descripcion": resultado[4]
            }
            inmuebles.append(inmueble)

        return inmuebles
