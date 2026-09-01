# =============================================================================
# ARCHIVO: ejercicios.py
# DESCRIPCIÓN: Módulo de la vista de ejercicios (Producción, Perforación, Reservorios).
# Versión inicial con componentes nativos de Streamlit para validación lógica.
# =============================================================================

import streamlit as st
import funciones_calculos

def renderizar_ejercicios():
    st.title("Módulos de Cálculo de Ingeniería")
    st.markdown("Ingrese los parámetros requeridos en cada sección para ejecutar las evaluaciones.")

    # Creación de los tres tabs técnicos requeridos
    tab_produccion, tab_perforacion, tab_reservorios = st.tabs(["Producción", "Perforación", "Reservorios"])

    with tab_produccion:
        st.header("IPR Compuesta con Punto de Burbuja")
        
        col1, col2 = st.columns(2)
        with col1:
            pr = st.number_input("Presión promedio del reservorio (Pr) [psi]", min_value=0.0, value=3000.0, step=10.0)
            pb = st.number_input("Presión de burbuja (Pb) [psi]", min_value=0.0, value=2000.0, step=10.0)
        with col2:
            j = st.number_input("Índice de productividad (J) [STB/d/psi]", min_value=0.01, value=1.5, step=0.1)
            pwf = st.number_input("Presión de fondo fluyente (Pwf) [psi]", min_value=0.0, value=1500.0, step=10.0)

        if st.button("Calcular Desempeño IPR"):
            try:
                # Validar condición inicial del modelo
                if pr <= pb:
                    st.error("Error: El modelo asume un reservorio subsaturado (Pr > Pb).")
                else:
                    resultados = funciones_calculos.calcular_produccion_ipr(pr, pb, j, pwf)
                    
                    st.success(f"Régimen detectado: {resultados['estado_regimen']}")
                    st.metric(label="Caudal Operativo (qo)", value=f"{resultados['caudal_operativo_stbd']} STB/d")
                    st.metric(label="Caudal a Presión de Burbuja (qb)", value=f"{resultados['caudal_burbuja_stbd']} STB/d")
                    st.metric(label="Caudal Máximo Teórico (q_max)", value=f"{resultados['caudal_maximo_stbd']} STB/d")
                    
                    # Espacio reservado para la futura gráfica de la curva IPR
                    st.info("Gráfica de la curva IPR se insertará aquí en la siguiente fase de desarrollo.")
            except Exception as e:
                st.error(f"Error en la ejecución: {e}")

    with tab_perforacion:
        st.header("Cálculo de Presión Hidrostática")
        
        col1, col2 = st.columns(2)
        with col1:
            mw = st.number_input("Peso del lodo (MW) [ppg]", min_value=0.01, value=10.0, step=0.1)
            md = st.number_input("Profundidad medida (MD) [ft]", min_value=1.0, value=10000.0, step=100.0)
        with col2:
            tvd = st.number_input("Profundidad vertical verdadera (TVD) [ft]", min_value=1.0, value=9500.0, step=100.0)
            pform = st.number_input("Presión de formación (Pform) [psi]", min_value=0.0, value=4800.0, step=50.0)

        if st.button("Evaluar Balance del Pozo"):
            try:
                resultados = funciones_calculos.calcular_presion_hidrostatica(mw, md, tvd, pform)
                
                st.success(f"Condición de pozo: {resultados['estado_balance']}")
                st.metric(label="Gradiente Hidrostático (Gh)", value=f"{resultados['gradiente_hidrostatico_psi_ft']} psi/ft")
                st.metric(label="Presión Hidrostática (Ph)", value=f"{resultados['presion_hidrostatica_psi']} psi")
                st.metric(label="Diferencial de Presión (ΔP)", value=f"{resultados['diferencial_presion_psi']} psi")
            except ValueError as ve:
                # Captura específica de los errores lógicos definidos en backend
                st.error(str(ve))
            except Exception as e:
                st.error(f"Error inesperado: {e}")

    with tab_reservorios:
        st.header("Estimación Volumétrica del POES")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            area = st.number_input("Área (A) [acres]", min_value=0.1, value=500.0, step=10.0)
            h_bruto = st.number_input("Espesor bruto (h) [ft]", min_value=0.1, value=150.0, step=5.0)
            ntg = st.number_input("Net-to-gross (NTG) [fracción]", min_value=0.01, max_value=1.0, value=0.75, step=0.05)
        with col2:
            porosidad = st.number_input("Porosidad (φ) [fracción]", min_value=0.01, max_value=1.0, value=0.20, step=0.01)
            swi = st.number_input("Saturación de agua (Swi) [fracción]", min_value=0.0, max_value=1.0, value=0.25, step=0.05)
        with col3:
            boi = st.number_input("Factor volumétrico (Boi) [rb/STB]", min_value=0.1, value=1.2, step=0.05)
            fr = st.number_input("Factor de recobro (FR) [fracción]", min_value=0.01, max_value=1.0, value=0.30, step=0.05)

        if st.button("Estimar Volumen POES"):
            try:
                resultados = funciones_calculos.calcular_volumetria_poes(area, h_bruto, ntg, porosidad, swi, boi, fr)
                
                st.success("Cálculo volumétrico completado")
                st.write(f"**Espesor neto (hn):** {resultados['espesor_neto_ft']} ft")
                
                st.subheader("Resultados Principales")
                c1, c2 = st.columns(2)
                c1.metric(label="POES [MMSTB]", value=resultados['poes_mmstb'])
                c2.metric(label="Volumen Recuperable [MMSTB]", value=resultados['volumen_recuperable_mmstb'])
                
                # Espacio para visualización volumétrica futura
                st.info("Gráfico comparativo de volúmenes se implementará aquí.")
            except ValueError as ve:
                st.error(str(ve))
            except Exception as e:
                st.error(f"Error inesperado: {e}")