# Proyecto_CRUD

------- INTRODUCCION: -------

1) Integrantes del equipo:
- Nicolas Rivarola
- Tomas Baldi
- Evelin Herrera

2) Dependencias para correr el script:
- pip install PyQt5
- pip install qrcode

3) Para iniciar el script, ejecute login_window.py

4) Usuario y contraseña para ingresar:
profesor
123456

------- TABLA PRINCIPAL -------
Las tablas se ordenan en forma ascendente por el atributo 'Apellido':
- Pestaña 'Activos': Muestra todos los empleados que no tienen una fecha de baja.
- Pestaña 'Inactivos': Muestra todos los empleados que tienen una fecha de baja.

------- BOTONES DE LA INTERFAZ -------
- 'Agregar': se agrega un nuevo registro a la pestaña de 'Activos'. La fecha de alta es en formato "AAAA-MM-DD".
- 'Modificar': se modifica el atributo de cualquier registro en base al ID del empleado.
- 'Dar de baja': se da de baja un empleado. La fecha de baja es en formato "AAAA-MM-DD". El registro figurará a continuación en la pestaña 'Inactivos'.
- 'Consultar': hace una query dentro de los empleados 'Activos' en base a criterio especifico. No es una consulta excluyente, funciona con una condición 'OR' en todos los campos. El formato de fecha es "AAAA-MM-DD".
- 'Refrescar BD': sirve para actualizar la base de datos, en caso de que se hagan modificaciones.

------- BOTONES ADICIONALES DE LA INTERFAZ -------
- 'Deshacer baja': sirve para dar de alta un empleado nuevamente, en caso que se haya dado de baja por error.
- 'Eliminar registro': sirve para eliminar un registro de la base de datos de forma permanente.

------- SEGURIDAD -------
- Las credenciales de los usuarios se guardan encriptados en la base de datos, para que los mismos no puedan ser legibles. 
