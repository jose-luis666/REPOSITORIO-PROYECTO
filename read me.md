# Limpieza de datos de ataques de tiburones a personas

Este proyecto tiene como objetivo limpiar y ordenar un conjunto de datos sobre ataques de tiburones a personas. El dataset cuenta con información sobre el área geográfica en la que ocurrió el ataque, la hora en la que ocurrió, si el ataque fue mortal o no, entre otros datos relevantes.

## Requisitos previos

Para ejecutar este proyecto se necesitan los siguientes paquetes de Python:
- Pandas
- Numpy

## Estructura del proyecto

- **data**: carpeta se encuentra el archivo CSV con los datos sucios del dataframe.
- **output**: Aquí se guardará el dataframe limpio en formato CSV.
- **read me**: explicacion sencilla del proyecto
- **your-code**: con el Jupyter Notebook y el código utilizado
- **img**: carpeta para incluir imágenes
- **src**: carpeta con el código fuente 

## Cómo ejecutar el proyecto

1. Clona este repositorio en tu ordenador.
2. Instala los paquetes necesarios: Pandas y Numpy.
3. El resultado se guardará en la carpeta output como un archivo CSV.

## Detalles de la limpieza de datos

Los datos del dataframe original venían muy desordenados y con valores faltantes. Para limpiarlos, se realizaron las siguientes operaciones:

- Se eliminaron las filas que no contenían información relevante para el estudio.
- Se reemplazaron los valores faltantes con información estimada a partir de otros datos del mismo registro.
- Se eliminaron registros duplicados.
- Se verificaron los tipos de datos de cada columna y se corrigieron aquellos que no correspondían.
- Se eliminaron caracteres especiales y se normalizaron los valores de las columnas.
- Se realizaron cambios de tipos de datos.
- Se cambiaron los nombres de algunas columnas para facilitar su comprensión.
- Se convirtieron algunas columnas irrelevantes o incompletas en 0.
- Se sustituyeron ciertos valores nulos por elementos comunes según la probabilidad.

## Resultados

El dataframe limpio se encuentra en el archivo output/shark_attacks_clean.csv

Con este nuevo dataframe limpio y ordenado, podremos realizar análisis y visualizaciones de datos más precisos y fiables sobre ataques de tiburones a personas.
