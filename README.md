README – Práctica 03 (Pruebas Automatizadas)

Karen Dayana Cabascango Alba
Universidad Politécnica Salesiana
Carrera: Negocios Digitales

📌 Descripción

Este proyecto implementa análisis de datos del archivo sri_ventas_2024.csv mediante un módulo en Python, utilizando pruebas unitarias para validar su funcionamiento.
Incluye además dos estadísticas adicionales, uso de la librería coverage y un reporte de cobertura.

🧪 Ejecución de la Aplicación

La ejecución del programa principal (app.py) muestra un resumen de ventas por provincia y permite consultar una provincia específica.

Ejemplo de salida:

Ventas totales por provincia:
    SANTA ELENA: $1473997045.48
    LOJA: $2181115159.20
    ...
Consulta por provincia:
    Ventas de CHIMBORAZO: $1,788,637,781.38

🔧 Funciones Principales (procesador.py)

Cálculo de ventas totales por provincia

Consulta de ventas por provincia

Exportaciones totales por mes (nueva)

Provincia con mayor volumen de importaciones (nueva)

Todas las funciones están validadas mediante pruebas unitarias.

🧪 Pruebas Unitarias

Las pruebas están ubicadas en tests/test_procesador.py y verifican:

Retorno correcto de diccionarios

Cantidad esperada de provincias

Valores positivos en ventas

Manejo de provincias inexistentes

Nuevas estadísticas implementadas

Para ejecutarlas:

python -m unittest discover

📊 Cobertura de Código (coverage)

Ejecución:

coverage run -m unittest discover
coverage report


Resultado obtenido:

TOTAL: 96% de cobertura


También se genera un reporte HTML con:

coverage html

📁 Estructura del Proyecto
practica-03/
├── datos/
│   └── sri_ventas_2024.csv
├── src/
│   └── procesador.py
├── tests/
│   └── test_procesador.py
├── venv/
├── app.py
└── README.md

✔️ Conclusión

La práctica demuestra el uso adecuado de pruebas unitarias en Python, validación de datos y medición de cobertura de código. Se implementaron correctamente dos estadísticas adicionales y se alcanzó un nivel de cobertura superior al requerido.


