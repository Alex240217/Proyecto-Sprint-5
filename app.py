import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título del proyecto
st.header('Proyecto sprint 5')

# Crear una casilla de verificación
show_hist = st.checkbox('Mostrar histograma')

# Crear botones
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

# Manejar el evento del botón de histograma
if hist_button:
    if show_hist:
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        fig_hist = px.histogram(car_data, x="odometer")
        st.plotly_chart(fig_hist, use_container_width=True)
    else:
        st.write('Casilla de verificación no seleccionada, no se mostrará el histograma.')

# Manejar el evento del botón de gráfico de dispersión
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color="type")
    st.plotly_chart(fig_scatter, use_container_width=True)
