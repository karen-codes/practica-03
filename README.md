# 🧪 Práctica 03 – Pruebas Automatizadas y Cobertura de Código

Este proyecto corresponde a la **Práctica 03 de la asignatura Gestión de la Calidad de Software**, donde se implementan funciones de análisis tributario usando Python, se construyen pruebas unitarias con `unittest` y se mide la cobertura del código mediante `coverage`.

---

## 📁 Estructura del Proyecto

PRACTICA-03/
│── app.py
│── README.md
│── .gitignore
│── .coverage
│── datos/
│ └── sri_ventas_2024.csv
│── src/
│ ├── procesador.py
│ └── init.py
│── tests/
│ ├── test_procesador.py
│ └── init.py
│── htmlcov/
│ ├── index.html
│ ├── style_cb_8432e98f.css
│ ├── coverage_html_cb_bcae5fc4.js
│ ├── status.json
│ └── (otros archivos generados por coverage)
│── venv/
│ ├── bin/
│ ├── lib/
│ └── (entorno virtual)


---

## ⚙️ Instalación y Configuración

### 1️⃣ Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate

2️⃣ Instalar herramienta de cobertura

pip install coverage

🧪 Ejecución de Pruebas Unitarias

python3 -m unittest discover

📊 Medición de Cobertura
Ejecutar coverage

coverage run -m unittest discover
coverage report

Generar reporte HTML

coverage html

El archivo principal del reporte está en:

htmlcov/index.html

📈 Resumen de Cobertura Obtenido

Name                       Stmts   Miss  Cover
----------------------------------------------
src/procesador.py             29      2    93%
tests/test_procesador.py      22      0   100%
----------------------------------------------
TOTAL                         51      2    96%

📌 Cobertura total del proyecto: 96%
🧠 Funciones Principales
✔ ventas_totales_por_provincia()

Devuelve un diccionario donde cada clave es una provincia y el valor es el total de ventas registradas.
✔ ventas_por_provincia(nombre)

Retorna el total de ventas para una provincia indicada.
Lanza KeyError si la provincia no existe en los datos.
🧪 Pruebas Implementadas

Las pruebas unitarias verifican que:

    El resumen total sea un diccionario.

    Existan 24 provincias.

    Todas las ventas sean mayores a 5000.

    Se lance error para provincias inexistentes.

    Provincias válidas devuelvan valores positivos.

👩‍💻 Autora

Karen Dayana Cabascango Alba
Universidad Politécnica Salesiana
Carrera: Negocios Digitales
Práctica Nº 03 – Gestión de la Calidad de Software