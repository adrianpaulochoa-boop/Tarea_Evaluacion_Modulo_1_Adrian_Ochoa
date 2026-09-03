# =============================================================================
# ARCHIVO: home.py
# DESCRIPCIÓN: Módulo de la vista inicial (Home).
# Interfaz optimizada con encabezados centrados y tarjetas interactivas.
# =============================================================================

import streamlit as st
import estilos

def renderizar_home():
    # 1. Encabezados centrados
    st.markdown("<h1 style='text-align: center; color: #F1FAF7;'>Suite Computacional de Cálculos Petroleros</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #F1FAF7; opacity: 0.9;'>Bootcamp Data Analytics for Oil & Gas</h3>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 2. Tarjetas superiores (Onda Expansiva)
    col1, col2 = st.columns(2)
    
    with col1:
        estilos.tarjeta_onda_expansiva(
            titulo="Desarrollador",
            valor="Adrian Paul Ochoa Daza",
            descripcion="Ingeniería y Desarrollo Frontend",
            altura=160
        )
        
    with col2:
        estilos.tarjeta_onda_expansiva(
            titulo="Módulos Técnicos",
            valor="Producción, Perforación, Reservorios",
            descripcion="Modelamiento SPE Interactivo",
            altura=160
        )
        
    # 3. Tarjeta inferior (Hover simple)
    st.markdown("<br>", unsafe_allow_html=True)
    
    texto_proposito = (
        "Esta herramienta modular automatiza cálculos de ingeniería petrolera. "
        "Facilita la evaluación del desempeño de afluencia (IPR), el balance hidrostático "
        "de perforación y la estimación volumétrica del Petróleo Original en Sitio (POES)."
    )
    
    estilos.tarjeta_hover_simple(
        titulo="Propósito Técnico de la Aplicación",
        descripcion=texto_proposito,
        altura=180
    )
    
    
