# =============================================================================
# ARCHIVO: app.py
# DESCRIPCIÓN: Script principal con integración de estilos globales.
# =============================================================================

import streamlit as st
import home
import ejercicios
import estilos

st.set_page_config(
    page_title="Plataforma Oil & Gas",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

estilos.cargar_css_global()

def main():
    st.sidebar.title("Menú de Navegación")
    
    opciones_navegacion = ["Home", "Ejercicios"]
    vista_seleccionada = st.sidebar.radio("Seleccione un módulo:", opciones_navegacion)
    
    # 1. Declaración del marcador de posición vacío
    contenedor_principal = st.empty()
    
    # 2. Encapsulamiento del renderizado dentro del contenedor forzado
    with contenedor_principal.container():
        if vista_seleccionada == "Home":
            home.renderizar_home()
        elif vista_seleccionada == "Ejercicios":
            ejercicios.renderizar_ejercicios()

if __name__ == "__main__":
    main()
