import streamlit as st
import pandas as pd

st.title("Catalogo de Productos")

#Carga de datos
@st.cache_data
def cargar_datos():
    return pd.read_csv("catalogo.csv")

df = cargar_datos()

st.subheader("Catalogo")
st.dataframe(df)

#Filtros
st.sidebar.header("Filtros")
#Por categoria
categorias = df['tipo'].unique()
categoria_selec = st.sidebar.selectbox(
    "Elegir Categoria",
    options=["Todas"] + list(categorias)
)
#Por precio
precio_min, precio_max = st.sidebar.slider(
    "Rango de Precios",
    float(df['precio'].min()),
    float(df['precio'].max()),
    (float(df['precio'].min()), float(df['precio'].max()))
)

#Copia para filtrar
df_filtrado = df.copy()

#Muestra de resultados
if categoria_selec == "Todas":
    df_filtrado = df_filtrado[(df_filtrado['precio'] >= precio_min) & (df_filtrado['precio'] <= precio_max)]

if categoria_selec != "Todas":
    df_filtrado = df_filtrado[df_filtrado['tipo'] == categoria_selec]

    df_filtrado = df_filtrado[(df_filtrado['precio'] >= precio_min) & (df_filtrado['precio'] <= precio_max)]

st.subheader("Productos Filtrados")
st.dataframe(df_filtrado)

#Metricas
st.subheader("Metricas")

producto_caro = df.loc[df['precio'].idxmax()]
producto_barato = df.loc[df['precio'].idxmin()]
precio_promedio = df['precio'].mean()
cantidad_total = df['cantidad'].sum()

#Creacion y definicion de las columnas
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Producto mas caro",
    producto_caro["nombre"],
    f"${producto_caro['precio']}"
)

col2.metric(
    "Producto mas barato",
    producto_barato["nombre"],
    f"${producto_barato['precio']}"
)

col3.metric("Promdio de los precios", f"${precio_promedio:.2f}")

col4.metric("Stock Total", cantidad_total)