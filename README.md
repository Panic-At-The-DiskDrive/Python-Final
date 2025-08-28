# Python - Entrega Final

## En forma individual, crearás una aplicación web estilo blog programada en Python en Django. Esta web tendrá admin, perfiles, registro, páginas y formularios.

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/Panic-At-The-DiskDrive/Python-Entrega_Final
   ```

2. **Entrar a la carpeta del proyecto**  
   ```bash
   cd Python-Entrega_Final
   ```

3. **Crear y activar entorno virtual**  
   ```bash
   python -m venv venv
   source venv/bin/activate   ### En Linux/Mac
   venv\Scripts\activate      ### En Windows
   ```

4. **Instalar dependencias**  
   ```bash
   pip install -r requirements.txt
   ```   

5. **Ejecutar migraciones iniciales**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   
6. **Crear superusuario (opcional, para acceder al admin)**  
   ```bash
   python manage.py createsuperuser
   ```

7. **Iniciar el servidor de desarrollo**  
   ```bash
   python manage.py runserver
   ```
   
8. **Abrir en el navegador**  
   ```bash
   http://127.0.0.1:8000/
   ```     

## Demo del Proyecto

https://drive.google.com/file/d/10C2HBhfAtlH9ZWnaCqdDv-sPhbAfteDF/view?usp=sharing

## Funcionalidades

+ Agregar juegos, desarrolladores y plataformas a la base de datos mediante formularios.
+ Listar juegos con búsqueda por título.
+ Navegación sencilla con herencia de plantillas.

## Objetivos
User story/brief:

+ Contar con algún acceso visible a la vista de "Acerca de mí" donde se contará acerca del dueño de la página manejado en el route about/.

+ Contar con algún acceso visible a la vista de blogs que debe alojarse en el route pages/. (Es decir un html que permite listar todos los blogs de la BD, con una información mínima de dicho blog)

+ Acceder a una pantalla que contendrá las páginas. Al clickear en “Leer más” debe navegar al detalle de la page mediante un route pages/<pageId>. (Al hacer clic se ven más detalle de lo que se veía en el apartado anterior) 

+ Si no existe ninguna página mostrar un "No hay páginas aún". (Aclarando, si en la página hacemos clic en algún lugar que no existe que diga eso, o que lleve a un html con esos mensaje, no dejar botones que no responden)

+ Para editar o borrar pages debes estar logueado y registrado como Administrador.

+ Cada blog, es decir cada model Blog debe tener como mínimo, un título, subtítulo, cuerpo, autor, fecha y una imagen (mínimo y obligatorio, puede tener más).

## Piezas sugeridas

Te recomendamos incluir:

+ NavBar

+ Home

+ About

+ Pages

+ Login

+ Signup

+ Messages

+ Profile

+ Logout

+ Get pages

+ Get page

+ Create page

+ Update Page

+ Delete page

+ Get profile

+ Update profile

## Requisitos

Los requisitos base serán parte de los criterios de evaluación para aprobar el proyecto.

Tener en cuenta que los requisitos están nombran un modelo principal para que uds en caso de querer cambiar de blog a otra temática puedan siempre y cuando cumplan los requisitos:

+ No agregar la Base de datos (el archivo db.sqlite3) en la entrega. Debería estar en el .gitignore.

+ Uso de herencia de templates. En el template base implementar la etiqueta nav de navegación que contenga los accesos que se crean necesarios para su página.

+ Existencia del archivo requirements.txt actualizado.

+ Tener en cuenta al manejar forms con imágenes hay que adaptar el template, y la vista...no solo el modelo y el formulario.

+ Uso de mínimo 2 clases basadas en vista.

+ Uso de mínimo un mixin en una CBV y un decorador en una view común.

+ Una vista de inicio/home.

+ Acceso a una vista "Acerca de mí"/"About".

+ Crear un modelo principal (Blog/Post/Auto/Vendedor/Docente/etc) que contenga los siguiente campos como mínimo: 2 Charfield, 1 de texto enriquecido (usando ckeditor), 1 campo de imagen, 1 de fecha.

+ Vista de listado de los objetos del modelo principal (modelo a elección). En la cual cada objeto mostrará solo algunos de sus datos.

+ Mensaje que da aviso en caso de no haber ningún objeto creado o al utilizar el buscador no encontrar tampoco algún objeto.

+ Desde el listado:

1 - poder acceder a una vista que muestre el detalle de el objeto seleccionado
2 - poder acceder a una vista de creación, una de edición y una de borrado de objetos.

+ Registrar en el apartado de admin todos los modelos creados.

+ Tener una app (accounts/cuentas/etc) para el manejo de todas las vistas relacionadas al usuario/autenticación.

+ Desarrollar las vistas para un login, un logout y un registro para usuarios. En este último se debe solicitar: username, email, password.

+ Crear una vista de perfil donde se muestran los datos del usuario:

1 - Nombre
2 - Apellido
3 - Email
4 - Avatar
5 - Biografia/link/fecha de cumpleaños/etc.

+ Desde el perfil, crear un acceso a una vista de edición de estos datos. Agregar el cambio de password.

+ Crear una app de mensajería con todo lo necesario para que los usuarios puedan comunicarse entre sí por mensajes. Todo en esta app queda a criterio del alumno/a siempre y cuando funcione correctamente.

+ Exista gitignore con:

- pycache
- db.sqlite3
- media

Estos últimos son por el hecho de no compartir la info de tu bd y, aparte, las imágenes son archivos muy pesados que no es recomendable tenerlos en el repo. En cambio, las imágenes que sean parte del código del proyecto deberían guardarse en la carpeta static.


## Recomendaciones

+ Que no se rompa :P

## Contenidos adicionales  

+ Messenger y like - integración otra db

### Criterios de evaluación
+ Cumplimientode consigna: Cumple con todos los Estándares de Django, el proyecto está subdividido en varias
App y ambas están internamente bien diseñadas y funcionales. No se encuentran
errores ni incongruencias

+ Aplicación de lo aprendido: Cumple con todos los requisitos que hacen al curso. No se encontraron déficit
importantes en cuanto al diagramado, estructura y desarrollo del proyecto general
y su evolución.

+ Aspectos estéticos: Excelente los aspectos estéticos, todo funciona correctamente, respeta MVT y
además usó las funcionalidades mínimas de Bootstrap o algún otro framework similar.


---

## Tecnologías utilizadas

- **Python**
- **Django**