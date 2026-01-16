# Trabajo Práctico Final – Python

## Objetivo
Desarrollar una aplicación web sencilla utilizando **Python**, **pandas** y **Streamlit** que permita analizar y visualizar un catálogo de productos a partir de un archivo CSV.

El objetivo del trabajo es integrar los conceptos vistos durante el curso:
- Lectura de archivos
- Manipulación de datos con pandas
- Lógica básica
- Visualización de información con Streamlit

---

## Datos
Se provee un archivo llamado `catalogo.csv` que contiene información de productos, con las siguientes columnas:

- `codigo`: identificador del producto  
- `nombre`: nombre del producto  
- `precio`: precio unitario  
- `tipo`: categoría del producto  
- `cantidad`: stock disponible  

---

## Consigna
Crear una aplicación en **Streamlit** que permita:

### 1. Cargar y mostrar los datos
- Leer el archivo `catalogo.csv` utilizando pandas.
- Mostrar el catálogo completo en una tabla.

### 2. Filtrar productos
- Permitir filtrar los productos por:
  - Tipo de producto
  - Rango de precios

### 3. Análisis del catálogo
La aplicación debe mostrar:
- El **producto más caro**
- El **producto más barato**
- El **precio promedio** de los productos
- La **cantidad total de stock** disponible

### 4. Visualización
- Mostrar los resultados de forma clara utilizando los componentes de Streamlit (`dataframe`, `metric`, etc.).

---

## Requisitos
- Usar Python
- Usar pandas para el manejo de datos
- Usar Streamlit para la interfaz
- El código debe estar ordenado y comentado
- La aplicación debe poder ejecutarse correctamente

---

## Entrega
- Archivo `.py` con el código de la aplicación