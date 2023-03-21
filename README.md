# MicroserviciosHABI
Proyecto de prueba para HABI
Para desarrollar estos dos microservicios en Python, se puede utilizar  la guía de estilo PEP 8 de Python y utilizar patrones de desarrollo de software como MVC (Modelo-Vista-Controlador) y DAO (Data Access Object).
Para el Microservicio de Consulta se pueden usar los siguientes componentes:
Controlador (InmuebleController): encargado de manejar las solicitudes HTTP y procesar los filtros aplicados por el usuario. Este componente puede recibir los parámetros de la consulta de la URL y llamar al componente DAO para obtener los inmuebles que coinciden con los filtros aplicados. El controlador también puede ser responsable de transformar los datos obtenidos en un formato JSON para enviarlos como respuesta al usuario.
Modelo (InmuebleModel): representa los datos de los inmuebles almacenados en la base de datos. Este componente puede tener una clase Inmueble con los atributos dirección, ciudad, estado, precio de venta, descripción y estado del inmueble. La clase DAO puede utilizar esta clase para mapear los resultados de la consulta a objetos Inmueble.
Objeto de Acceso a Datos (InmuebleDAO): encargado de acceder a la base de datos y recuperar los inmuebles que coinciden con los filtros aplicados por el usuario. Este componente puede tener una clase InmuebleDAO con métodos para realizar la consulta de inmuebles con filtros aplicados.
Vista (InmuebleView): es el componente que maneja la interfaz de usuario y permite la interacción del usuario con la aplicación. En este caso, la vista puede ser una interfaz web que permite al usuario aplicar los filtros y ver los resultados de la consulta
Para el Microservicio de "Me Gusta" se pueden usar los siguientes componentes:
Controlador (Controller): encargado de manejar las solicitudes HTTP y procesar la acción de "Me gusta" realizada por el usuario. Este componente puede recibir el ID del inmueble y el ID del usuario que dio el "Me gusta" como parámetros de la consulta de la URL. El controlador puede llamar al componente DAO para registrar el "Me gusta" del usuario en la base de datos.
Modelo (Model): representa los datos de los usuarios y los inmuebles almacenados en la base de datos.
El objeto JSON a esperar en el Microservicio de consulta seria:
{
  "inmuebles": [
    {
      "direccion": "Calle 123",
      "ciudad": "Bogotá",
      "estado": "en_venta",
      "precio": 150000000,
      "descripcion": "Hermoso apartamento en el centro de la ciudad",
      "anio_construccion": 2010
    },
    {
      "direccion": "Avenida 456",
      "ciudad": "Medellín",
      "estado": "en_venta",
      "precio": 210000000,
      "descripcion": "Amplio apartamento con vista a la montaña",
      "anio_construccion": 2015
    },
    {
      "direccion": "Carrera 789",
      "ciudad": "Barranquilla",
      "estado": "vendido",
      "precio": 180000000,
      "descripcion": "Apartamento de dos habitaciones cerca de la playa",
      "anio_construccion": 2005
    }
  ]
}
