Participantes: Alejandro Uribe Pino

Este es un blog realizado completamente en Django.

Para poder ejecutarlo necesitaras:
1.Clonar el repositorio
2.Crea un entorno virtual.
que en Windows puedes crearlo utlizando este comando: python -m venv venv
.\venv\Scripts\activate
3. luego de haber creado el entorno virtual descarga las dependecias que tiene el proyecto.
utilizando este comando: pip install django si no lo tienes instalado, muy importante debes tener ya Python descargado para que 
pueda funcionar
4. luego de realizar esto realiza las migraciones.
python manage.py migrate
5. ya con esto hecho puedes hecharlo andar utilizando el siguiente comando.
python manage.py runserver
6. luego de haberlo iniciado utiliza esta direccion para poder visualizar el blog: http://127.0.0.1:8000/ 

El blog es uno en el que con el simple enlace puedes entrar y publicar tu blog, no cuenta con algun diseño en particular ya que lo estaba haciendo con CSS y me parecio bastante feo el resultado por eso
lo termine dejando asi.
