# =============================================================================
# ARCHIVO: graficas.py
# DESCRIPCIÓN: Módulo de visualización con Plotly.
# Tipografía incrementada, cuadrículas activas y fondos transparentes.
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
        line=dict(color='#0F766E', width=4)
    ))
    
    fig.add_trace(go.Scatter(
        x=[q_usuario], y=[pwf_usuario], 
        mode='markers', name='Punto Operativo', 
        marker=dict(color='#A3E635', size=16, line=dict(color='#1F2933', width=2))
    ))
    
    fig.update_layout(
        title=dict(text="<b>Desempeño de Afluencia (IPR)</b>", font=dict(size=26, color='#0B3C49')),
        xaxis_title=dict(text="<b>Caudal (q) [STB/d]</b>", font=dict(size=18)),
        yaxis_title=dict(text="<b>Presión de Fondo (Pwf) [psi]</b>", font=dict(size=18)),
        font=dict(color='#1F2933', size=16),
        plot_bgcolor='#FFFFFF',
        paper_bgcolor='rgba(0,0,0,0)', 
        xaxis=dict(showgrid=True, gridcolor='#D1D5DB', gridwidth=1, zeroline=False),
        yaxis=dict(showgrid=True, gridcolor='#D1D5DB', gridwidth=1, zeroline=False),
        legend=dict(font=dict(size=15), bgcolor='rgba(255,255,255,0.9)', bordercolor='#D1D5DB', borderwidth=1),
        margin=dict(l=60, r=40, t=60, b=60)
    )
    return fig


def graficar_hidrostatica(mw, tvd_usuario, ph_usuario):
    tvd_array = np.linspace(0, tvd_usuario * 1.1, 20)
    ph_array = 0.052 * mw * tvd_array
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=ph_array, y=tvd_array, 
        mode='lines', name='Gradiente de Lodo', 
        line=dict(color='#0F766E', width=4)
    ))
    
    fig.add_trace(go.Scatter(
        x=[ph_usuario], y=[tvd_usuario], 
        mode='markers', name='Profundidad Actual', 
        marker=dict(color='#A3E635', size=16, line=dict(color='#1F2933', width=2))
    ))
    
    fig.update_layout(
        title=dict(text="<b>Perfil de Presión Hidrostática</b>", font=dict(size=26, color='#0B3C49')),
        xaxis_title=dict(text="<b>Presión (Ph) [psi]</b>", font=dict(size=18)),
        yaxis_title=dict(text="<b>Profundidad (TVD) [ft]</b>", font=dict(size=18)),
        font=dict(color='#1F2933', size=16),
        plot_bgcolor='#FFFFFF',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=True, gridcolor='#D1D5DB', gridwidth=1, zeroline=False),
        yaxis=dict(autorange="reversed", showgrid=True, gridcolor='#D1D5DB', gridwidth=1, zeroline=False),
        legend=dict(font=dict(size=15), bgcolor='rgba(255,255,255,0.9)', bordercolor='#D1D5DB', borderwidth=1),
        margin=dict(l=60, r=40, t=60, b=60)
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
        title=dict(text="<b>Distribución del Petróleo Original en Sitio</b>", font=dict(size=26, color='#0B3C49')),
        yaxis_title=dict(text="<b>Volumen [MMSTB]</b>", font=dict(size=18)),
        font=dict(color='#1F2933', size=16),
        plot_bgcolor='#FFFFFF',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=True, gridcolor='#D1D5DB', gridwidth=1, zeroline=False),
        legend=dict(font=dict(size=15), bgcolor='rgba(255,255,255,0.9)', bordercolor='#D1D5DB', borderwidth=1),
        margin=dict(l=60, r=40, t=60, b=60),
        width=500
    )
    return fig