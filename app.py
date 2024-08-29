import streamlit as st
from textblob import TextBlob
from textblob.exceptions import NotTranslated
from spellchecker import SpellChecker

# Inicializar el corrector ortográfico para español
spell = SpellChecker(language='es')

st.title('Análisis de Sentimiento y Corrección en Español')

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar y corregir")

with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.write("""
        **Polaridad**: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
        Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.

        **Subjetividad**: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
        (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

with st.expander('Analizar Polaridad y Subjetividad en un texto en español'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:
        # Analizar sentimiento usando TextBlob
        blob = TextBlob(text1)
        # La polaridad y subjetividad pueden no estar disponibles si el texto no puede ser analizado
        try:
            sentiment = blob.sentiment
            st.write('Polaridad: ', round(sentiment.polarity, 2))
            st.write('Subjetividad: ', round(sentiment.subjectivity, 2))
            x = round(sentiment.polarity, 2)
            if x >= 0.5:
                st.write('Es un sentimiento Positivo 😊')
            elif x <= -0.5:
                st.write('Es un sentimiento Negativo 😔')
            else:
                st.write('Es un sentimiento Neutral 😐')
        except NotTranslated:
            st.write('No se pudo analizar el sentimiento del texto.')

with st.expander('Corrección de texto en español'):
    text2 = st.text_area('Escribe el texto en español que deseas corregir: ', key='4')
    if text2:
        # Corregir el texto usando SpellChecker
        corrected_text = ' '.join(spell.candidates(word) for word in text2.split())
        st.write('Texto corregido: ', corrected_text)

