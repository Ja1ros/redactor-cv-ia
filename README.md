# Redactor de CV con IA

Generador y optimizador de curriculums vitae (CV) y cartas de presentacion usando Inteligencia Artificial (OpenAI GPT-4o-mini).

## Descripcion

Esta aplicacion permite ingresar informacion personal, experiencia laboral, educacion y habilidades, para generar automaticamente un CV profesional o una carta de presentacion personalizada, adaptada al puesto de trabajo deseado y al tono elegido por el usuario.

## Caracteristicas

- Generacion de CV profesional estructurado por secciones.
- Generacion de cartas de presentacion persuasivas y personalizadas.
- Seleccion de tono: Profesional, Creativo, Formal o Conciso.
- Descarga del documento generado en formato de texto.
- Interfaz simple e intuitiva construida con Streamlit.

## Tecnologias utilizadas

- Python
- Streamlit
- OpenAI API (GPT-4o-mini)
- python-dotenv

## Instalacion

1. Clonar el repositorio:
```
git clone https://github.com/Ja1ros/redactor-cv-ia.git
cd redactor-cv-ia
```

2. Instalar dependencias:
```
pip install -r requirements.txt
```

3. Configurar variables de entorno:
```
cp .env.example .env
```
Luego edita el archivo `.env` y agrega tu API Key de OpenAI.

## Uso

Ejecuta la aplicacion con:
```
streamlit run app.py
```

Luego abre tu navegador en `http://localhost:8501`, completa tus datos profesionales y genera tu CV o carta de presentacion optimizada con IA.

## Licencia

Este proyecto es de uso libre para fines educativos y de portafolio.
