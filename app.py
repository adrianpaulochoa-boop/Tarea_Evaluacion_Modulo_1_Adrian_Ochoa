# =============================================================================
# ARCHIVO: app.py
# DESCRIPCIÓN: Script principal y enrutador de la aplicación.
# Gestiona la configuración de página y la navegación modular.
# =============================================================================

import streamlit as st

# Importación de los módulos de vista previamente desarrollados
import home
import ejercicios

# 1. Configuración global de la página (debe ser el primer comando de Streamlit)
st.set_page_config(
    page_title="Plataforma Oil & Gas",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """
    Función principal que controla el flujo de ejecución y el menú lateral.
    """
    # 2. Configuración de la barra lateral (Navegación principal)
    st.sidebar.title("Menú de Navegación")
    
    # Restricción de opciones de navegación según los requerimientos técnicos
    opciones_navegacion = ["Home", "Ejercicios"]
    vista_seleccionada = st.sidebar.radio("Seleccione un módulo:", opciones_navegacion)
    
    # 3. Lógica de enrutamiento hacia los scripts externos
    if vista_seleccionada == "Home":
        home.renderizar_home()
    elif vista_seleccionada == "Ejercicios":
        ejercicios.renderizar_ejercicios()

if __name__ == "__main__":
    main()