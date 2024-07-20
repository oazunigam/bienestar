import streamlit as st
import pandas as pd
import pickle
import os
import json

st.set_page_config(
    page_title="Bienestar",
    page_icon="👋",
)

# Diccionario de preguntas y opciones
with open('data/preguntas.json', 'r') as f:
    questions = json.load(f)

# Título del formulario
st.title('Encuesta de Bienestar')

# Crear un formulario
responses = {}
with st.form(key='survey_form'):
    responses['Edad'] = st.number_input('¿Cuál es su edad?', min_value=0, max_value=120, step=1, format='%d')
    for question, options in questions.items():
        responses[question] = st.selectbox(question, options)
    submit_button = st.form_submit_button(label='Enviar')

# Mostrar respuestas después de enviar el formulario
if submit_button:
    # Convertir respuestas a DataFrame
    df_responses = pd.DataFrame([responses])
    
    # Cargar el modelo de clasificación
    try:
        with open('data/bienestar_model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        
        # Hacer predicciones
        prediction = model.predict(df_responses)
        prediction_proba = model.predict_proba(df_responses)

        # Crear una nueva página para mostrar resultados
        st.write("## Resultados de la Predicción")
        st.write("### Predicción:")
        st.write(prediction[0])
        st.write("### Probabilidades:")
        st.write('[Alto,Bajo,Medio]')
        st.write(prediction_proba)
    except ValueError as e:
        st.error(f"Error al cargar el modelo: {e}")
        st.error("Asegúrate de que el archivo 'bienestar_model.pkl' es compatible con la versión actual de scikit-learn.")

    st.write("## Respuestas:")
    for question, response in responses.items():
        st.write(f"**{question}:** {response}")
