
# Requerimientos previos:
    - VirtualEnv
    - Python 3.7

### 1. Crear un entorno virtual y activar en entorno virtual. En una terminal (En Windows):
    - Crear entorno virtual
    ```bash
    virtualenv -p  C:\Users\Home\AppData\Local\Programs\Python\Python37\python.exe  venv
    ```
    - Activar el entorno virtual
    ```bash
    .\venv\Scripts\activate
    ```
### 2. Ejecutar en la terminal:
    ```bash
    python main.py
    ```

# Puntos de desarrollo

### 1. Crear un sistema que recorra los usuarios -contacts- (revisar la API) - https://developers.hubspot.com/docs/api/crm/contacts
#### R/: 
[Link to code](https://github.com/AndresGarzonJ/test_Orbidi/blob/c68199f5c6ba9ecf50caa5bffb115e7fc009bf24/src/controller/contacts_controller.py#L23)
### 2. Primer algoritmo: Que por cada contacto: Revisar si tienen phone number. En el caso que no tengan aplicar el: 660049971
#### R/: 
[Link to code](https://github.com/AndresGarzonJ/test_Orbidi/blob/c68199f5c6ba9ecf50caa5bffb115e7fc009bf24/src/controller/contacts_controller.py#L36)
#### R/: 
### 3. Segundo algoritmo: Crear un deal (objeto CRM Hubspot) vinculado a cada uno de los con datos dummy
#### R/: 
Sin solución
### 4. Hacer propuesta de ¿cómo podríamos hacer que este proceso se organizara como una API?
#### R/: 
Con el uso de microservicios con el uso de librerias como 'http_handler', 'http', 'request', y 'wsgiref'. Con ello, el servidor que gestioana las acciones HTTP (Ej; POST, GET). Y para la respuesta se podría usar una estructura de datos como JSON o XML.

Otra propuesta es usar frameworks como Flask o Django. Que brinda beneficios como el desarrollo ágil.
### 5. Hacer una propuesta de cómo crees que se puede crear una BD de datos que sirva como respaldo para estos procesos.
#### R/: 
Respondo la pregunta desde la optimización. Para ello, se podría guardar las busquedas en cache (temporalmente), y asi, reducir la carga tanto en el servidor como en la db.


## Authors

- [@AndresGarzonJ](https://linktr.ee/andresgarzonj)
