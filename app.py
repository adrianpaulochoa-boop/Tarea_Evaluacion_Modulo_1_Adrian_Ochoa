# =============================================================================
# ARCHIVO: app.py
# DESCRIPCIÓN: Script principal con integración de estilos globales.
# =============================================================================

import streamlit as st
import home
import ejercicios
import estilos  

# Configuración global de la página
st.set_page_config(
    page_title="Plataforma Oil & Gas",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inyección de las reglas CSS globales (Fondo, tipografía, botones)
estilos.cargar_css_global()

def main():
    st.sidebar.title("Menú de Navegación")
    
    opciones_navegacion = ["Home", "Ejercicios"]
    vista_seleccionada = st.sidebar.radio("Seleccione un módulo:", opciones_navegacion)
    
    if vista_seleccionada == "Home":
        home.renderizar_home()
    elif vista_seleccionada == "Ejercicios":
        ejercicios.renderizar_ejercicios()

if __name__ == "__main__":
    main()
