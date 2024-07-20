import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Bienestar",
    page_icon="👋",
)
# Cargar el dataset
file_path = 'data/Bienestar.csv'
df = pd.read_csv(file_path)
df['Edad']=df['Edad'].astype(int)


# Título del dashboard
st.title('Dashboard de Bienestar')

# Crear bins de edad
df['Rango de edad'] = pd.cut(df['Edad'], bins=5)

# Gráfico de barras: cantidad de personas por rango de edad
st.header('Cantidad de personas por rango de edad')
edad_counts = df['Rango de edad'].value_counts().sort_index()
fig, ax = plt.subplots()
edad_counts.plot(kind='bar', ax=ax)
ax.set_xlabel('Rango de edad')
ax.set_ylabel('Cantidad de personas')
st.pyplot(fig)

# Gráfico de barras: distribución de "NIVEL DE SATISFACCIÓN CON LA VIDA" por rango de edad
st.header('Distribución del NIVEL DE SATISFACCIÓN CON LA VIDA por rango de edad')
satisfaccion_edad = df.groupby(['Rango de edad', 'NIVEL DE SATISFACCIÓN CON LA VIDA']).size().unstack().fillna(0)
fig, ax = plt.subplots()
satisfaccion_edad.plot(kind='bar', stacked=True, ax=ax)
ax.set_xlabel('Rango de edad')
ax.set_ylabel('Cantidad de personas')
ax.legend(title='NIVEL DE SATISFACCIÓN CON LA VIDA')
st.pyplot(fig)

# Gráfico de barras: distribución de "NIVEL DE SATISFACCIÓN CON LA VIDA" por género
st.header('Distribución del NIVEL DE SATISFACCIÓN CON LA VIDA por género')
satisfaccion_genero = df.groupby(['Género recodificado dicotómico', 'NIVEL DE SATISFACCIÓN CON LA VIDA']).size().unstack().fillna(0)
fig, ax = plt.subplots()
satisfaccion_genero.plot(kind='bar', stacked=True, ax=ax)
ax.set_xlabel('Género')
ax.set_ylabel('Cantidad de personas')
ax.legend(title='NIVEL DE SATISFACCIÓN CON LA VIDA')
st.pyplot(fig)

# Gráfico de barras: 'NIVEL DE BIENESTAR TOTAL' respecto a la edad
st.header('Relación del NIVEL DE BIENESTAR TOTAL respecto a la edad')

# Verificar si la columna 'NIVEL DE BIENESTAR TOTAL' existe en el DataFrame
if 'NIVEL DE BIENESTAR TOTAL' in df.columns:
    bienestar_edad = df.groupby(['Edad', 'NIVEL DE BIENESTAR TOTAL']).size().unstack().fillna(0).reset_index()

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.histplot(data=df, x='Edad', hue='NIVEL DE BIENESTAR TOTAL', multiple='stack', palette='viridis', binwidth=5)
    ax.set_xlabel('Edad')
    ax.set_ylabel('Cantidad de personas')
    st.pyplot(fig)
else:
    st.error("El DataFrame no contiene la columna 'NIVEL DE BIENESTAR TOTAL'.")

# Heatmap: relación entre "NIVEL DE BIENESTAR TOTAL" y "NIVEL DE SATISFACCIÓN CON LA VIDA"
st.header('Relación entre NIVEL DE BIENESTAR TOTAL y NIVEL DE SATISFACCIÓN CON LA VIDA')
contingency_table = pd.crosstab(df['NIVEL DE BIENESTAR TOTAL'], df['NIVEL DE SATISFACCIÓN CON LA VIDA'])
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(contingency_table, annot=True, fmt='d', cmap='YlGnBu', ax=ax)
ax.set_xlabel('NIVEL DE SATISFACCIÓN CON LA VIDA')
ax.set_ylabel('NIVEL DE BIENESTAR TOTAL')
st.pyplot(fig)

# Gráfico de barras: relación entre "NIVEL DE BIENESTAR TOTAL" y "Nivel educativo"
st.header('Relación entre NIVEL DE BIENESTAR TOTAL y Nivel educativo')
bienestar_educativo = df.groupby(['Nivel educativo', 'NIVEL DE BIENESTAR TOTAL']).size().unstack().fillna(0)
fig, ax = plt.subplots(figsize=(12, 8))
bienestar_educativo.plot(kind='bar', ax=ax)
ax.set_xlabel('Nivel educativo')
ax.set_ylabel('Cantidad de personas')
ax.legend(title='NIVEL DE BIENESTAR TOTAL')
st.pyplot(fig)