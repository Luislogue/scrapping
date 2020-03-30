# Paso a Paso, para que la app funcione en cualquier sistema.
# Alpine -> Un mini OS de LINUX como base o capa principal de docker.
FROM alpine:3.11.2

# Instalar python3 y la ultima version de pip
RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

    # Montar imagen de docker con el alpine
# docker build -t <nombre que le queramos dar a la imagen>
    # Entrar dentro del sistema del linux de docker alpine
# docker run -it -p 7000:5000 -d <nombreDeLaImagen>

    # Crear una carpeta dentro del sistema operativo de linux para poder almacenar nuestra app

WORKDIR /app

    # Copiar todos los archivos a la carpeta /app para poder almacenar nuestra app
COPY . /app
    # Instalar dependencias del proyecto
RUN pip3 --no-cache install -r requirements.txt

# Lista de ejecuciones
CMD ["python3", "src/main.py"]

# docker container ls -> Para ver que containers se estan ejecutando
# docker images -> ver las imagenes dispopnibles
# docker stop <containerID> -> parar containers que estan ejecutandose
# si tenemos el container arrancado y nos queremos meter dentro del shell de linux dentro del container :
    #  docker ps -> para ver que containers estan corriendo,
    # docker exec -it <id del container> /bin/sh
# VOLUMEN -> Es una conexion con una rama local a un docker image para no tener que hacer builds
    # docker run -it -p 7000:5000 -d -v D:\WORK\Muevete\python\Template_Flask\src: /app/src flask_app