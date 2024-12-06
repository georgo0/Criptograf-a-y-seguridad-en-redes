# Criptografia-y-seguridad-en-redes
Aquí es en donde se puede encontrar tanto los códigos y capturas para el desarrollo de los laboratorios del curso

Comentarios para laboratorios:

Laboratorio 1:
  - Para el funcionamiento de la tercera actividad, se recomeinda que el archivo 'diccionario.txt' este en la misma carpeta que 'readv2.py'

Laboratorio 3:
  - La funcion hash encontrada en la pagina web del login de Bsale (https://login.bsale.cl/):
    ```bash
      sha1Hash('')
    ```
Laboratorio 4:  
  - Libreria utilizada
    ```bash
        pip install pycryptodomex
    ```
Laboratorio 5:
  - Se creo el siguiente directorio:
    ```bash
        mkdir -p ~/lab5_cripto/{C1,C2,C3,C4}
    ```
  - Una vez creados y guardados los Dockerfiles, se levantaron los contenedores con:
    ```bash
        cd ~/lab5_cripto/C1
        docker build -t c1_image .
    
        cd ~/lab5_cripto/C2
        docker build -t c2_image .
        
        cd ~/lab5_cripto/C3
        docker build -t c3_image .
        
        cd ~/lab5_cripto/C4S1
        docker build -t c4_s1_image .
    ```
  - Para obtener la IP de cada contenedor se utilizó:
    ```bash
        sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' C1
        sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' C2
        sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' C3
        sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' C4S1
    ```
- Para generar la conexión entre cliente y servidor se utilizó:
    ```bash
        #user: prueba
        #password: prueba
        
        #En el desarrollo de este laboratorio, la IP del servidor corresponde a 172.19.0.5
        
        docker exec -it C1 /bin/bash
        ssh prueba@172.19.0.5
        
        docker exec -it C2 /bin/bash
        ssh prueba@172.19.0.5
        
        docker exec -it C3 /bin/bash
        ssh prueba@172.19.0.5
        
        docker exec -it C4S1 /bin/bash
        ssh prueba@172.19.0.5
    ```



    
