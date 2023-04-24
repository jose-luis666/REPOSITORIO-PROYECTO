#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def clean_dataframe(dataframe):
    """
    Esta función toma como entrada un dataframe de Pandas y realiza la limpieza de los datos.

    Parámetros:
        dataframe (pd.DataFrame): Un dataframe de Pandas desordenado y posiblemente sucio.

    Retorna:
        pd.DataFrame: Un dataframe de Pandas ordenado y limpio.
    """
    # Eliminar filas duplicadas
    dataframe.drop_duplicates(inplace=True)

    # Eliminar columnas con valores nulos
    dataframe.dropna(inplace=True)

    # Ordenar el dataframe por una o varias columnas
    dataframe.sort_values(by=['columna1', 'columna2'], ascending=[True, False], inplace=True)

    # Resetear los índices del dataframe
    dataframe.reset_index(drop=True, inplace=True)

    return dataframe

if __name__ == '__main__':
    # Ejemplo de uso de la función
    df = pd.read_csv('ruta/al/archivo.csv')
    df_limpio = clean_dataframe(df)
    print(df_limpio.head())

