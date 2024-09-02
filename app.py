import streamlit as st
from textblob import TextBlob
from googletrans import Translator

translator = Translator()
st.title('Uso de textblob')

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.write("""
        Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
        Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
        
        Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
        (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:
        # Traduce el texto al inglés
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        
        # Analiza el texto traducido
        blob = TextBlob(trans_text)
        
        # Muestra la polaridad y subjetividad
        polaridad = round(blob.sentiment.polarity, 2)
        subjetividad = round(blob.sentiment.subjectivity, 2)
        
        st.write('Polaridad: ', polaridad)
        st.write('Subjetividad: ', subjetividad)
        
        # Muestra imágenes según la subjetividad
        if subjetividad >= 0.7:
            st.image("P1.jpg", caption="Alta Subjetividad", use_column_width=True)
        elif subjetividad <= 0.6:
            st.image("P0.jpg", caption="Baja Subjetividad", use_column_width=True)
        
        # Muestra imágenes según la polaridad
        if polaridad >= 0.5:
            st.image("HF.jpg", caption="Sentimiento Positivo", use_column_width=True)
        elif polaridad <= 0.4:
            st.image("SF.jpg", caption="Sentimiento Negativo", use_column_width=True)

        # Determina el sentimiento y muestra el mensaje correspondiente
        if polaridad >= 0.5:
            st.write('Es un sentimiento Positivo 😊')
        elif polaridad <= -0.5:
            st.write('Es un sentimiento Negativo 😔')
        else:
            st.write('Es un sentimiento Neutral 😐')

with st.expander('Corrección en inglés'):
    text2 = st.text_area('Escribe por favor: ', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write(blob2.correct())



