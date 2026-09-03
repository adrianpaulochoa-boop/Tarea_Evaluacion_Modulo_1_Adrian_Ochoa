# =============================================================================
# ARCHIVO: graficas.py
# DESCRIPCIÓN: Módulo de visualización con Plotly.
# Leyendas ancladas al interior del gráfico y textos optimizados.
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
        mode='markers', name='Operativo', 
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
        # 1. Configuración de Leyenda Horizontal Responsiva
        legend=dict(
            orientation="h",       # Leyenda dispuesta horizontalmente
            xanchor="center",      # Anclada desde su propio centro
            x=0.5,                 # Ubicada exactamente a la mitad del gráfico (50%)
            yanchor="top",         # Anclada desde su borde superior
            y=-0.25,               # Desplazada hacia abajo, fuera de la cuadrícula
            font=dict(size=14), 
            bgcolor='rgba(255,255,255,0.9)', 
            bordercolor='#D1D5DB', 
            borderwidth=1
        ),
        # 2. Ajuste de Márgenes (Aumento del margen inferior 'b' para acomodar la leyenda)
        margin=dict(l=60, r=40, t=60, b=100)
    )
    return fig


def graficar_hidrostatica(mw, tvd_usuario, ph_usuario):
    # Generación de datos matemáticos
    tvd_array = np.linspace(0, tvd_usuario * 1.1, 20)
    ph_array = 0.052 * mw * tvd_array
    
    fig = go.Figure()
    
    # Trazo 1: Línea del gradiente hidrostático
    fig.add_trace(go.Scatter(
        x=ph_array, y=tvd_array, 
        mode='lines', name='Gradiente', 
        line=dict(color='#0F766E', width=4)
    ))
    
    # Trazo 2: Punto exacto evaluado por el usuario
    fig.add_trace(go.Scatter(
        x=[ph_usuario], y=[tvd_usuario], 
        mode='markers', name='Prof. Actual', 
        marker=dict(color='#A3E635', size=16, line=dict(color='#1F2933', width=2))
    ))
    
    # Configuración del lienzo corregida
    fig.update_layout(
        title=dict(text="<b>Perfil de Presión Hidrostática</b>", font=dict(size=26, color='#0B3C49')),
        xaxis_title=dict(text="<b>Presión (Ph) [psi]</b>", font=dict(size=18)),
        yaxis_title=dict(text="<b>Profundidad (TVD) [ft]</b>", font=dict(size=18)),
        font=dict(color='#1F2933', size=16),
        plot_bgcolor='#FFFFFF',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=True, gridcolor='#D1D5DB', gridwidth=1, zeroline=False),
        # Se aplica autorange="reversed" para que la profundidad descienda visualmente
        yaxis=dict(autorange="reversed", showgrid=True, gridcolor='#D1D5DB', gridwidth=1, zeroline=False),
        legend=dict(
            orientation="h",
            xanchor="center",
            x=0.5,
            yanchor="top",
            y=-0.25,
            font=dict(size=14),
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#D1D5DB',
            borderwidth=1
        ),
        margin=dict(l=60, r=40, t=60, b=100)
    )
    return fig


def graficar_poes(poes_mmstb, volumen_recuperable_mmstb):
    # Cálculos aislados de la lógica visual
    volumen_no_recuperable = poes_mmstb - volumen_recuperable_mmstb
    
    fig = go.Figure(data=[
        go.Bar(
            name='Recuperable', 
            x=['Análisis Volumétrico'], 
            y=[volumen_recuperable_mmstb], 
            marker_color='#A3E635'
        ),
        go.Bar(
            name='Remanente', 
            x=['Análisis Volumétrico'], 
            y=[volumen_no_recuperable], 
            marker_color='#0F766E'
        )
    ])
    
    fig.update_layout(
        barmode='stack',
        title=dict(text="<b>Distribución del Petróleo Original en Sitio</b>", font=dict(size=26, color='#0B3C49')),
        # Ejes corregidos para análisis volumétrico
        xaxis_title=dict(text="<b>Parámetros de Contribución</b>", font=dict(size=18)),
        yaxis_title=dict(text="<b>Volumen [MMSTB]</b>", font=dict(size=18)),
        font=dict(color='#1F2933', size=16),
        plot_bgcolor='#FFFFFF',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=True, gridcolor='#D1D5DB', gridwidth=1, zeroline=False),
        legend=dict(
            orientation="h",
            xanchor="center",
            x=0.5,
            yanchor="top",
            y=-0.25,
            font=dict(size=14),
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#D1D5DB',
            borderwidth=1
        ),
        margin=dict(l=60, r=40, t=60, b=100),
        width=500
    )
    return fig
    return fig
