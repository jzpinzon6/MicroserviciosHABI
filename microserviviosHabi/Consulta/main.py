# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == '__main__':
    from psycopg2 import connect
    conexion = connect(database='micodb', user='micousuario', password='micontraseña', host='localhost')
    dao = InmuebleDAO(conexion)
    controller = InmuebleController(InmuebleDAO)
    vista = InmuebleView(InmuebleController)
