# =============================================================================
# ARCHIVO: home.py
# DESCRIPCIÓN: Módulo de la vista inicial (Home) - Versión Nativa.
# =============================================================================

import streamlit as st

def renderizar_home():
    # Encabezados nativos de Streamlit
    st.title("Plataforma Integral Oil & Gas")
    st.subheader("Bootcamp Data Analytics for Oil & Gas")
    
    st.divider()
    
    # Uso de st.metric nativo para simular temporalmente las tarjetas de resultados
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Desarrollador", value="Adrian Paul Ochoa Daza")
        
    with col2:
        st.metric(label="Módulos Técnicos", value="Producción, Perforación, Reservorios")
        
    # Contenedor nativo para la descripción del proyecto
    st.markdown("### Propósito Técnico de la Aplicación")
    st.info(
        "Esta herramienta modular automatiza cálculos de ingeniería petrolera. "
        "Facilita la evaluación del desempeño de afluencia (IPR), el balance hidrostático "
        "de perforación y la estimación volumétrica del Petróleo Original en Sitio (POES)."
    )
    
    