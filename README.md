# 🛒 Tienda Libre

Ecommerce didáctico desarrollado con **Django** como proyecto integrador de **Programación III** (6.° año, ITS Villada).

Este repositorio se construye **clase a clase** durante el ciclo lectivo, incorporando progresivamente los conceptos fundamentales del desarrollo web con Django: modelos y ORM, patrón MTV, vistas basadas en clases, formularios, autenticación y CRUD completo.

---

## Stack tecnológico

- **Python** 3.12+
- **Django** 5.x
- **SQLite** (base de datos de desarrollo)
- **Bootstrap 5** (via CDN)
- HTML5 / CSS3 / JavaScript

## Requisitos previos

- WSL2 con Ubuntu (Windows) o Linux/macOS
- `pyenv` o Python 3.12 o superior
- `git` configurado con clave SSH en GitHub
- Editor: VS Code recomendado (con extensión Remote — WSL si corresponde)

---

## Puesta en marcha

### 1. Cloná el repositorio

```bash
git clone git@github.com:tu-usuario/tienda-libre.git
cd tienda-libre
```

### 2. Creá y activá el entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

Al activarlo, el prompt debería mostrar `(.venv)` al inicio.

### 3. Instalá las dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicá las migraciones

```bash
python manage.py migrate
```

### 5. Creá un superusuario para el admin

```bash
python manage.py createsuperuser
```

### 6. Levantá el servidor de desarrollo

```bash
python manage.py runserver
```

- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

---

## Estructura del proyecto

```
tienda-libre/
├── config/                    # Proyecto Django (settings + URLs raíz)
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── tiendalibre/               # App principal del ecommerce
│   ├── models.py              # Producto, Categoría
│   ├── views.py               # Vistas (FBV y CBV)
│   ├── admin.py               # Configuración del admin site
│   ├── forms.py               # Form y ModelForm
│   ├── urls.py                # URLs de la app
│   ├── migrations/
│   └── templates/
│       └── tiendalibre/
│           ├── base.html
│           ├── home.html
│           ├── catalogo.html
│           └── detalle.html
├── static/                    # CSS y JS propios
├── media/                     # Imágenes subidas por usuarios (no versionado)
├── requirements.txt
├── manage.py
├── .gitignore
└── README.md
```

---

## Roadmap de contenidos

Cada checkbox se marca al cerrar la clase correspondiente.

- [x] **Clase 0** — Setup: `venv`, instalación de Django, primer modelo, admin site
- [ ] **Clase 1** — Modelo `Categoría` + `ForeignKey` + admin personalizado
- [ ] **Clase 2** — Patrón MTV: URLs, vistas y primer template
- [ ] **Clase 3** — Herencia de templates + Bootstrap
- [ ] **Clase 4** — Django Template Language en profundidad
- [ ] **Clase 5** — ORM y Django shell
- [ ] **Clase 6** — Catálogo dinámico conectado con la BD
- [ ] **Clase 7** — Detalle de producto con URLs dinámicas
- [ ] **Clase 8** — Archivos estáticos y media
- [ ] **Clase 9** — Class-Based Views (TemplateView, ListView)
- [ ] **Clase 10** — DetailView y paginación
- [ ] **Clase 11** — Filtrado por categoría y buscador
- [ ] **Clase 12** — Formularios (`forms.Form` + CSRF)
- [ ] **Clase 13** — ModelForm
- [ ] **Clase 14** — CreateView + UpdateView
- [ ] **Clase 15** — DeleteView (CRUD completo)
- [ ] **Clase 16** — Autenticación (login, logout, protección de vistas)
- [ ] **Clase 17** — Registro de usuarios y control de acceso

---

## Convenciones de trabajo

### Git

- Al final de **cada clase** se hace commit descriptivo.
- Formato de mensajes: `tipo: descripción` — `feat`, `fix`, `refactor`, `docs`, `style`, `chore`.
- Ejemplos:
  - `feat: agregar modelo Categoria y ForeignKey en Producto`
  - `refactor: migrar CatalogoView de FBV a CBV`
  - `docs: agregar ejemplos de consultas ORM`
- Trabajo por rama por funcionalidad. `main` siempre estable.

### Qué NO se sube al repositorio

Estos elementos van en `.gitignore` y **no** deben commitearse:

- `.venv/` — entorno virtual
- `db.sqlite3` — base de datos local
- `media/` — archivos subidos por el usuario
- `__pycache__/` — bytecode de Python
- `.env` — variables de entorno con secretos

### Dependencias

Cuando se instala un paquete nuevo con `pip`, hay que regenerar `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

## Comandos útiles

```bash
# Crear una migración a partir de cambios en los modelos
python manage.py makemigrations

# Aplicar migraciones pendientes
python manage.py migrate

# Abrir el shell interactivo de Django
python manage.py shell

# Correr el servidor en otro puerto
python manage.py runserver 8080

# Crear una nueva app
python manage.py startapp <nombre>
```

---

## Contexto académico

| | |
|---|---|
| **Cátedra** | Programación III |
| **Curso** | 6.° Año |
| **Institución** | ITS Villada |
| **Docente** | Prof. Nicolás Ledesma |
| **Contacto** | n.ledesma@itsv.edu.ar |
| **Ciclo lectivo** | 2026 |

---

## Licencia

Proyecto educativo de uso interno de la cátedra. No se autoriza su uso comercial.