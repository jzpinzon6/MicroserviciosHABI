# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------------------------------------
# Función: Capa de Modelo en el patron MVC.
# Autor: Javier Pinzón.
# Version: 1
# Descripción:
#
#   La funcionalidad de esta capa es manejar las solicitudes HTTP y procesar la acción de "Me gusta" realizada por el
#   usuario. Este componente puede recibir el ID del inmueble y el ID del usuario que dio el "Me gusta" como parámetros
#   de la consulta de la URL. El controlador puede llamar al componente DAO para registrar el "Me gusta" del usuario
#   en la base de datos.


class ControladorMeGusta:
    def dar_me_gusta(self, id_usuario, id_inmueble):
        usuario = Usuario.obtener_por_id(id_usuario)
        inmueble = Inmueble.obtener_por_id(id_inmueble)
        if usuario is not None and inmueble is not None:
            me_gusta = MeGusta(id_usuario, id_inmueble)
            me_gusta.guardar()
            return "Me gusta registrado correctamente."
        else:
            return "Error: Usuario o inmueble no existen."