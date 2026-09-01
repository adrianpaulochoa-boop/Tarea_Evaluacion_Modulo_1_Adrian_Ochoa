# =============================================================================
# ARCHIVO: ejercicios.py
# DESCRIPCIÓN: Módulo técnico con integración de tarjetas JS/CSS personalizadas.
# =============================================================================

import streamlit as st
import funciones_calculos
import graficas
import estilos  # Importación de las tarjetas interactivas

def renderizar_ejercicios():
    st.title("Módulos de Cálculo de Ingeniería")
    st.markdown("Ingrese los parámetros requeridos en cada sección.")

    tab_produccion, tab_perforacion, tab_reservorios = st.tabs(["Producción", "Perforación", "Reservorios"])

    with tab_produccion:
        st.header("IPR Compuesta con Punto de Burbuja")
        
        col1, col2 = st.columns(2)
        with col1:
            pr = st.number_input("Presión promedio (Pr) [psi]", min_value=0.0, value=3000.0, step=10.0)
            pb = st.number_input("Presión de burbuja (Pb) [psi]", min_value=0.0, value=2000.0, step=10.0)
        with col2:
            j = st.number_input("Índice de productividad (J) [STB/d/psi]", min_value=0.01, value=1.5, step=0.1)
            pwf = st.number_input("Presión de fondo fluyente (Pwf) [psi]", min_value=0.0, value=1500.0, step=10.0)

        if st.button("Calcular Desempeño IPR"):
            try:
                if pr <= pb:
                    st.error("Error: El reservorio debe ser subsaturado (Pr > Pb).")
                else:
                    resultados = funciones_calculos.calcular_produccion_ipr(pr, pb, j, pwf)
                    
                    # Implementación de Tarjetas Interactivas
                    c1, c2 = st.columns(2)
                    with c1:
                        estilos.generar_tarjeta_interactiva(
                            titulo="Caudal Operativo", 
                            valor=f"{resultados['caudal_operativo_stbd']} STB/d", 
                            descripcion=f"Régimen: {resultados['estado_regimen']}"
                        )
                    with c2:
                        estilos.generar_tarjeta_interactiva(
                            titulo="Caudal Máximo", 
                            valor=f"{resultados['caudal_maximo_stbd']} STB/d", 
                            descripcion="Potencial absoluto del pozo",
                            es_alerta=True
                        )
                    
                    figura_ipr = graficas.graficar_ipr(pr, pb, j, pwf, resultados['caudal_operativo_stbd'])
                    st.plotly_chart(figura_ipr, use_container_width=True,theme=None)
            except Exception as e:
                st.error(f"Error: {e}")

    with tab_perforacion:
        st.header("Cálculo de Presión Hidrostática")
        
        col1, col2 = st.columns(2)
        with col1:
            mw = st.number_input("Peso del lodo (MW) [ppg]", min_value=0.01, value=10.0, step=0.1)
            md = st.number_input("Profundidad medida (MD) [ft]", min_value=1.0, value=10000.0, step=100.0)
        with col2:
            tvd = st.number_input("Profundidad vertical (TVD) [ft]", min_value=1.0, value=9500.0, step=100.0)
            pform = st.number_input("Presión de formación (Pform) [psi]", min_value=0.0, value=4800.0, step=50.0)

        if st.button("Evaluar Balance del Pozo"):
            try:
                resultados = funciones_calculos.calcular_presion_hidrostatica(mw, md, tvd, pform)
                
                # Implementación de Tarjeta con Fluido Ondulante para Perforación
                estilos.tarjeta_fluido_ondulante(
                    titulo="Presión Hidrostática (Ph)", 
                    valor=f"{resultados['presion_hidrostatica_psi']} psi", 
                    porcentaje_llenado=75
                )
                
                figura_hidrostatica = graficas.graficar_hidrostatica(mw, tvd, resultados['presion_hidrostatica_psi'])
                st.plotly_chart(figura_hidrostatica, use_container_width=True,theme=None)
            except ValueError as ve:
                st.error(str(ve))
            except Exception as e:
                st.error(f"Error inesperado: {e}")

    with tab_reservorios:
        st.header("Estimación Volumétrica del POES")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            area = st.number_input("Área (A) [acres]", min_value=0.1, value=500.0, step=10.0)
            h_bruto = st.number_input("Espesor bruto (h) [ft]", min_value=0.1, value=150.0, step=5.0)
            ntg = st.number_input("Net-to-gross (NTG)", min_value=0.01, max_value=1.0, value=0.75, step=0.05)
        with col2:
            porosidad = st.number_input("Porosidad (φ)", min_value=0.01, max_value=1.0, value=0.20, step=0.01)
            swi = st.number_input("Saturación de agua (Swi)", min_value=0.0, max_value=1.0, value=0.25, step=0.05)
        with col3:
            boi = st.number_input("Factor volumétrico (Boi)", min_value=0.1, value=1.2, step=0.05)
            fr = st.number_input("Factor de recobro (FR)", min_value=0.01, max_value=1.0, value=0.30, step=0.05)

        if st.button("Estimar Volumen POES"):
            try:
                resultados = funciones_calculos.calcular_volumetria_poes(area, h_bruto, ntg, porosidad, swi, boi, fr)
                
                # Implementación de Tarjetas Cyber-Glitch para Resultados Críticos
                c1, c2 = st.columns(2)
                with c1:
                    estilos.tarjeta_cyber_glitch(
                        titulo="POES", 
                        valor=f"{resultados['poes_mmstb']} MMSTB", 
                        descripcion="Petróleo Original en Sitio"
                    )
                with c2:
                    estilos.tarjeta_cyber_glitch(
                        titulo="Volumen Recuperable", 
                        valor=f"{resultados['volumen_recuperable_mmstb']} MMSTB", 
                        descripcion=f"Factor de recobro: {fr*100}%"
                    )
                
                figura_poes = graficas.graficar_poes(resultados['poes_mmstb'], resultados['volumen_recuperable_mmstb'])
                st.plotly_chart(figura_poes, use_container_width=True,theme=None)
            except ValueError as ve:
                st.error(str(ve))
            except Exception as e:
                st.error(f"Error inesperado: {e}")
