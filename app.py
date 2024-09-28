import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Set the overall theme for the app
st.set_page_config(page_title="Análisis de Sentimientos", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .title {
        color: #FF6347;
        font-size: 48px;
        text-align: center;
    }
    .subtitle {
        color: #FFA07A;
        font-size: 24px;
        text-align: center;
    }
    .sidebar-content {
        background-color: #f5f5f5;
        padding: 10px;
        border-radius: 10px;
    }
    .result-box {
        background-color: #e6f7ff;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        color: #333;
    }
    .positive {
        background-color: #d4edda;
        border-left: 6px solid #28a745;
    }
    .negative {
        background-color: #f8d7da;
        border-left: 6px solid #dc3545;
    }
    .neutral {
        background-color: #fff3cd;
        border-left: 6px solid #ffc107;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown('<h1 class="title">Análisis de Sentimientos con TextBlob</h1>', unsafe_allow_html=True)

# Subtitle
st.markdown('<h2 class="subtitle">¡Descubre la polaridad y subjetividad de tus textos!</h2>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.subheader("Información sobre Polaridad y Subjetividad 📊")
    st.write("""
        **Polaridad**: Mide si el sentimiento es positivo, negativo o neutral. 
        Rango: -1 (muy negativo) a 1 (muy positivo), con 0 siendo neutral.
        
        **Subjetividad**: Mide si el contenido es subjetivo (opiniones/emociones) o objetivo (hechos). 
        Rango: 0 (completamente objetivo) a 1 (completamente subjetivo).
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Main Content
with st.expander('📈 Analizar Polaridad y Subjetividad en un Texto', expanded=True):
    text1 = st.text_area('Escribe tu texto aquí:', placeholder="Escribe algo para analizar...", height=150)
    
    if text1:
        # Translate text to English
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        
        # Analyze the translated text
        blob = TextBlob(trans_text)
        
        # Get sentiment analysis results
        polaridad = round(blob.sentiment.polarity, 2)
        subjetividad = round(blob.sentiment.subjectivity, 2)
        
        # Display results
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.write('**Polaridad:**', polaridad)
        st.write('**Subjetividad:**', subjetividad)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Display images based on sentiment analysis
        st.markdown('<h3 class="subtitle">Resultados Visuales</h3>', unsafe_allow_html=True)
        
        if subjetividad >= 0.7:
            st.image("P1.jpg", caption="Alta Subjetividad", use_column_width=True)
        else:
            st.image("P0.jpg", caption="Baja Subjetividad", use_column_width=True)
        
        if polaridad >= 0.5:
            st.image("HF.jpg", caption="Sentimiento Positivo", use_column_width=True)
            st.markdown('<div class="result-box positive">Es un sentimiento Positivo 😊</div>', unsafe_allow_html=True)
        elif polaridad <= -0.5:
            st.image("SF.jpg", caption="Sentimiento Negativo", use_column_width=True)
            st.markdown('<div class="result-box negative">Es un sentimiento Negativo 😔</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-box neutral">Es un sentimiento Neutral 😐</div>', unsafe_allow_html=True)

# Text Correction Section
with st.expander('📝 Corrección de Texto en Inglés'):
    text2 = st.text_area('Escribe tu texto en inglés para corrección:', key='4', placeholder="Escribe un texto en inglés...")
    
    if text2:
        blob2 = TextBlob(text2)
        corrected_text = blob2.correct()
        
        st.write("**Texto Original:**", text2)
        st.write("**Texto Corregido:**", corrected_text)




