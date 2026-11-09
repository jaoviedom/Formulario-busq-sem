# Buscador semántico de productos

Aplicación web desarrollada como parte de la materia **Optativa I** en el
campus **Ibagué** de la **Universidad Cooperativa de Colombia**. El proyecto
permite buscar productos mediante una consulta en lenguaje natural y muestra
los resultados más similares usando embeddings y FAISS.

## Requisitos

- Python 3.13 (versión utilizada para el desarrollo).
- Conexión a Internet la primera vez que se inicia la aplicación, para
  descargar el modelo `sentence-transformers/all-MiniLM-L6-v2` si aún no está
  disponible localmente.

## Instalación

Desde la carpeta del proyecto, crea y activa un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows PowerShell, activa el entorno con:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```bash
python -m pip install Django pandas faiss-cpu sentence-transformers
```

Prepara la base de datos y ejecuta el servidor de desarrollo:

```bash
python manage.py migrate
python manage.py runserver
```

Abre [http://127.0.0.1:8000/buscar/](http://127.0.0.1:8000/buscar/) en el
navegador.

## Uso

1. En la página **Buscar productos**, escribe una descripción o términos que
   representen lo que necesitas; por ejemplo, `equipo para entrenamiento de
   inteligencia artificial`.
2. Selecciona **Buscar** para ver hasta cinco resultados relacionados.
3. Selecciona el nombre de un producto para consultar su descripción y precio.
   Usa **Volver** para regresar a la búsqueda.

La interfaz de administración de Django está disponible en
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). Para crear un
usuario administrador local:

```bash
python manage.py createsuperuser
```

## Datos y archivos del buscador

- El catálogo utilizado por la búsqueda está en
  `core/ia/artefactos/productos.csv`.
- La configuración y el índice FAISS precalculado están en
  `core/ia/artefactos/config.json` y `core/ia/artefactos/faiss.index`.
- Los productos que se muestran en la página de detalle se consultan desde la
  base de datos SQLite (`db.sqlite3`).

Para que los enlaces a los detalles funcionen, los productos guardados en la
base de datos deben tener los mismos identificadores que las filas
correspondientes del catálogo CSV. Si no existen, agrega los productos desde el
administrador de Django y asegúrate de que sus identificadores coincidan.

## Tecnologías

- Django
- Sentence Transformers
- FAISS
- pandas
- SQLite
