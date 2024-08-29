import streamlit as st
from textblob import TextBlob
from textblob_es import PatternAnalyzer

st.title('Análisis de Sentimiento en Español')

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.write("""
        **Polaridad**: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
        Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.

        **Subjetividad**: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
        (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:
        # Usar PatternAnalyzer para español
        blob = TextBlob(text1, analyzer=PatternAnalyzer())
        st.write('Polaridad: ', round(blob.sentiment[0], 2))
        st.write('Subjetividad: ', round(blob.sentiment[1], 2))
        x = round(blob.sentiment[0], 2)
        if x >= 0.5:
            st.write('Es un sentimiento Positivo 😊')
        elif x <= -0.5:
            st.write('Es un sentimiento Negativo 😔')
        else:
            st.write('Es un sentimiento Neutral 😐')

with st.expander('Corrección en español'):
    text2 = st.text_area('Escribe por favor: ', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write(blob2.correct())
