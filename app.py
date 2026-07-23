import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Redactor de CV con IA", page_icon="\U0001F4C4", layout="wide")

st.title("Redactor y Optimizador de CV con IA")
st.write("Genera o mejora tu curriculum vitae y carta de presentacion usando inteligencia artificial.")

with st.sidebar:
    st.header("Configuracion")
    api_key_input = st.text_input("OpenAI API Key (opcional si ya esta en .env)", type="password")
    if api_key_input:
        openai.api_key = api_key_input
    modo = st.radio("Que deseas generar?", ["Curriculum (CV)", "Carta de presentacion"])

st.subheader("Informacion personal y profesional")

col1, col2 = st.columns(2)
with col1:
    nombre = st.text_input("Nombre completo")
    puesto = st.text_input("Puesto al que aplicas")
    experiencia = st.text_area("Experiencia laboral (resumen)", height=150)
with col2:
    educacion = st.text_area("Educacion", height=100)
    habilidades = st.text_area("Habilidades y competencias", height=100)
    idiomas = st.text_input("Idiomas")

tono = st.selectbox("Tono del documento", ["Profesional", "Creativo", "Formal", "Conciso"])

if st.button("Generar con IA"):
    if not nombre or not puesto:
        st.warning("Por favor completa al menos el nombre y el puesto deseado.")
    else:
        with st.spinner("Generando documento..."):
            try:
                if modo == "Curriculum (CV)":
                    prompt = f"Redacta un curriculum vitae profesional en espanol con tono {tono} para {nombre}, que aplica al puesto de {puesto}. Experiencia: {experiencia}. Educacion: {educacion}. Habilidades: {habilidades}. Idiomas: {idiomas}. Estructura el CV con secciones claras: Perfil profesional, Experiencia, Educacion, Habilidades e Idiomas."
                else:
                    prompt = f"Redacta una carta de presentacion profesional en espanol con tono {tono} para {nombre}, que aplica al puesto de {puesto}. Experiencia: {experiencia}. Educacion: {educacion}. Habilidades: {habilidades}. La carta debe ser persuasiva, concisa y destacar el valor que aportaria al puesto."

                response = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Eres un experto en redaccion de documentos profesionales de busqueda de empleo."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.6
                )

                resultado = response.choices[0].message.content
                st.subheader("Resultado generado")
                st.markdown(resultado)
                st.download_button("Descargar como texto", resultado, file_name="documento_generado.txt")

            except Exception as e:
                st.error(f"Error al generar el documento: {e}")
