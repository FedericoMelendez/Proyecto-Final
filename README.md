#### 馃捇Bienvenidos al repositorio de nuestra pagina web馃捇
**Requerimientos:**
- Python 3.10
- Django 4.0.4
- Pillow  9.2.0

Alumno 
**Federico Melendez**. 

Realiz贸 las siguientes tareas

Desarrollo:

- **Creacion del proyecto con todos los modelos y elementos**
- **Creacion de todo lo que refiere a Media**
- **Creacion de Nuevo articulo, edicion y borrar (Tanto para Notebooks, Monitores y Perifericos**
- **Detalle de cada articulo**
- **Listado de productos por tipo de producto**
- **Listado de todos los productos**
- **Busqueda de producto**
- **Visual con HTML, CSS y JavaScript**
- **Herencias de HTML con Navbar y Footer**
- **Creacion de todos los Models y Formularios**
- **Creacion del About con su respectivos Templates**
- **Creacion de Templates para todos los articulos, junto con su creacion, edicion y delete**
- **Creacion del Profile**
- **Creacion del Index**
- **Configuracion en el Settings para el correcto funcionamiento**
- **Creacion y descripcion del README**
- **Creacion del Video**


--------------------------------------------------------------------------------------
**Federico L贸pez**
Realiz贸 las siguientes tareas

Desarrollo:

**Creacion de Login, Logout y Register**
**Creaci贸n del about y su template inicial**
**Creaci贸n del Readme inicial**

--------------------------------------------------------------------------------------
**Datos:**
-  user: useradmin1
-  pass: admin123
-  admin@admin.com
-  Para Registrarse la contrase帽a debe contener una letra mayuscula y un numero .


#### Informacion: 
脡sta p谩gina web es el trabajo final del curso de Python de la plataforma [Coderhouse](https://www.coderhouse.com.uy/?utm_term=coder&utm_campaign=0&utm_source=google_search_brand&utm_medium=cpc&gclid=CjwKCAjw3K2XBhAzEiwAmmgrApaOKUH3xckHPTtz6bv8fBl3-BFM6GCu1jZ-5263s5_ZduW0eYb_2xoCM-4QAvD_BwE "Coderhouse")(comisi贸n #31090). Tratamos de abarcar todo lo dado durante el curso para realizarla.
Nuestro proyecto es un ecommerce creado para la venta de insumos inform谩ticos asi como Notebooks, Monitores  y Perifericos.

Para la parte visual utilizamos una plantilla de la pagina https://templatemo.com/ la cual contiene css, javascript, fonts y algunos HTML los cuales fueron modificados y adaptados a nuestra idea para contar con una mejor visual. Fue modificado settings.py para el uso de estos , mediante ayuda de tutoriales en Youtube debido a la falta de conocimiento para poder hacerlo. Por suerte pudimos lograrlo.

Contamos con distintos tipos de insumos a la venta que se pueden agregar y modificar desde el admin o desde la parte de crear articulos si es que se est谩 registrado como administrador.

Podemos crear un articulo nuevo a partir de un formulario, una vez creada la publicaci贸n, nos redirecciona a la lista del art铆culo.

**URLS**

admin/ Es para ingresar al panel de administrador. Podemos crear un usuario con "python manage.py createsuperuser".

index/ o "/"  Nos lleva a la pagina de Inicio. Tambien desde all铆 podremos direccionarnos a otras urls haciendo click en las diferentes opciones.

users/ Nos lleva a todas las opciones de Usuarios. Tanto Register, Login o Logout.

about/ Nos lleva al about del sitio.

products/ Nos indica las distintas opciones que podemos hacer con los productos. Podemos crear, editar o borrar un producto. 

- products/new-notebook **Crea una notebook**
- products/list-notebooks **Listado de notebooks**
- products/delete-notebook **Borrar una notebook**
- products/update-notebook **Editar una notebook**
- procucts/detail-notebook **Detalle de una notebook**

Esto lo podemos repetir tanto en los monitores como tambien en los perifericos.

search-products/ Realiza la busqueda del articulo que uno desea por nombre entre todos los articulos.

all-products/ Muestra todos los articulos disponibles.


Video de explicacion del sitio: 

https://www.youtube.com/watch?v=WeEa2KAmxE0

**Proximos cambios a realizar:**

- Correccion de la creacion de Perfiles.
- Correccion en la edicion de Perfiles.
- Agregar la opcion para borrar Perfil.

