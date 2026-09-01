# =============================================================================
# ARCHIVO: graficas.py
# DESCRIPCIÓN: Módulo de visualización de datos utilizando Plotly.
# Configurado con fondo blanco y alto contraste para legibilidad.
# =============================================================================

import plotly.graph_objects as go
import numpy as np

def graficar_ipr(pr, pb, j, pwf_usuario, q_usuario):
    pwf_array = np.linspace(0, pr, 50)
    q_array = []
    
    for pwf in pwf_array:
        if pwf >= pb:
            q = j * (pr - pwf)
        else:
            qb = j * (pr - pb)
            termino_vogel = (j * pb) / 1.8
            relacion = pwf / pb
            q = qb + termino_vogel * (1 - 0.2 * relacion - 0.8 * (relacion ** 2))
        q_array.append(q)
        
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=q_array, y=pwf_array, 
        mode='lines', name='Curva IPR', 
        line=dict(color='#0F766E', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=[q_usuario], y=[pwf_usuario], 
        mode='markers', name='Punto Operativo', 
        marker=dict(color='#A3E635', size=12, line=dict(color='#1F2933', width=2))
    ))
    
    fig.update_layout(
        title="Desempeño de Afluencia (IPR)",
        xaxis_title="Caudal (q) [STB/d]",
        yaxis_title="Presión de Fondo (Pwf) [psi]",
        plot_bgcolor='#FFFFFF',
        paper_bgcolor='#FFFFFF',
        font=dict(color='#1F2933'),
        xaxis=dict(gridcolor='#E5E7EB', zerolinecolor='#E5E7EB'),
        yaxis=dict(gridcolor='#E5E7EB', zerolinecolor='#E5E7EB'),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    return fig


def graficar_hidrostatica(mw, tvd_usuario, ph_usuario):
    tvd_array = np.linspace(0, tvd_usuario * 1.1, 20)
    ph_array = 0.052 * mw * tvd_array
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=ph_array, y=tvd_array, 
        mode='lines', name='Gradiente de Lodo', 
        line=dict(color='#0F766E', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=[ph_usuario], y=[tvd_usuario], 
        mode='markers', name='Profundidad Actual', 
        marker=dict(color='#A3E635', size=12, line=dict(color='#1F2933', width=2))
    ))
    
    fig.update_layout(
        title="Perfil de Presión Hidrostática",
        xaxis_title="Presión (Ph) [psi]",
        yaxis_title="Profundidad (TVD) [ft]",
        yaxis=dict(autorange="reversed", gridcolor='#E5E7EB', zerolinecolor='#E5E7EB'),
        xaxis=dict(gridcolor='#E5E7EB', zerolinecolor='#E5E7EB'),
        plot_bgcolor='#FFFFFF',
        paper_bgcolor='#FFFFFF',
        font=dict(color='#1F2933'),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    return fig


def graficar_poes(poes_mmstb, volumen_recuperable_mmstb):
    volumen_no_recuperable = poes_mmstb - volumen_recuperable_mmstb
    
    fig = go.Figure(data=[
        go.Bar(
            name='Volumen Recuperable', 
            x=['Análisis Volumétrico'], 
            y=[volumen_recuperable_mmstb], 
            marker_color='#A3E635'
        ),
        go.Bar(
            name='Volumen Remanente', 
            x=['Análisis Volumétrico'], 
            y=[volumen_no_recuperable], 
            marker_color='#0F766E'
        )
    ])
    
    fig.update_layout(
        barmode='stack',
        title="Distribución del Petróleo Original en Sitio (POES)",
        yaxis_title="Volumen [MMSTB]",
        plot_bgcolor='#FFFFFF',
        paper_bgcolor='#FFFFFF',
        font=dict(color='#1F2933'),
        yaxis=dict(gridcolor='#E5E7EB', zerolinecolor='#E5E7EB'),
        xaxis=dict(gridcolor='#FFFFFF', zerolinecolor='#FFFFFF'),
        margin=dict(l=40, r=40, t=40, b=40),
        width=500
    )
    return fig
