
# Puntos de desarrollo

1. Crear un sistema que recorra los usuarios -contacts- (revisar la API) - https://developers.hubspot.com/docs/api/crm/contacts
2. Primer algoritmo que por cada contacto:
    Revisar si tienen phone number
    En el caso que no tengan aplicar el:
    660049971

    # Solución
    Requerimientos previos:
    - VirtualEnv
    - Python 3.7
    <br /> 
    <br />     
    1. Crear un entorno virtual y activar en entorno virtual. En una terminal (En Windows):
        - Crear entorno virtual
        ```
        virtualenv -p  C:\Users\Home\AppData\Local\Programs\Python\Python37\python.exe  venv
        ```
        - Activar el entorno virtual
        ```
        .\venv\Scripts\activate
        ```
    2. Ejecutar en la terminal:
        ```
        python main.py
        ```

3. Segundo algoritmo: Crear un deal (objeto CRM Hubspot) vinculado a cada uno de los con datos dummy
    - Sin solución
4. Hacer propuesta de ¿cómo podríamos hacer que este proceso se organizara como una API?
    - Con el uso de microservicios con el uso de librerias como 'http_handler', 'http', 'request', y 'wsgiref'. Con ello, el servidor que gestioana las acciones HTTP (Ej; POST, GET). Y para la respuesta se podría usar una estructura de datos como JSON o XML.
5. Hacer una propuesta de cómo crees que se puede crear una BD de datos que sirva como respaldo para estos procesos.