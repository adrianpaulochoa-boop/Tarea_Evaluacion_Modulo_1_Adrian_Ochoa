# =============================================================================
# ARCHIVO: estilos.py
# DESCRIPCIÓN: Módulo unificado de diseño visual interactivo (HTML, CSS, JS).
# Contiene estilos globales y componentes avanzados para Streamlit.
# =============================================================================

import streamlit as st
import streamlit.components.v1 as components

def cargar_css_global():
    """
    Inyecta las reglas CSS globales para el fondo de la aplicación, 
    barra lateral, colores de texto y botones nativos.
    """
    css = """
    <style>
    /* 1. Fondo principal de la aplicación */
    .stApp {
        background-color: #0B3C49;
    }
    
    h1, h2, h3, p, span, label {
        color: #F1FAF7 !important;
    }
    
    header {
    background-color: transparent !important;
    }
    
    /* 2. Personalización de la Barra Lateral */
    [data-testid="stSidebar"] {
        background-color: #072A34 !important; /* Tono ligeramente más oscuro para dar profundidad */
        border-right: 1px solid #0F766E !important; /* Línea divisoria de acento */
    }
    
    /* Forzar el color de los textos, títulos y opciones dentro del Sidebar */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: #F1FAF7 !important;
    }
    
    /* Mejorar el contraste de los botones de radio inactivos y activos en el sidebar */
    .stRadio div[role="radiogroup"] label {
        color: #F1FAF7 !important;
    }

    /* 3. Personalización de Botones Nativos */
    .stButton>button {
        background-color: #0F766E !important;
        color: #F1FAF7 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        font-weight: bold !important;
        width: 100%;
        transition: all 0.3s ease !important;
    }
    
    [data-testid="stPlotlyChart"] {
        background-color: #FFFFFF !important;
        border-radius: 16px !important;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2) !important;
        padding: 15px !important;
        border: 1px solid #E5E7EB;
    }
    
    .stButton>button:hover {
        background-color: #A3E635 !important;
        color: #1F2933 !important;
        transform: scale(1.02);
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def generar_tarjeta_interactiva(titulo, valor, descripcion="", es_alerta=False, altura=220):
    """
    Tarjeta con borde neón giratorio y halo radial acoplado al movimiento del cursor.
    """
    color_valor = "#A3E635" if es_alerta else "#0F766E"
    
    html_code = f"""
    <style>
    html, body {{ margin: 0; padding: 10px; background: transparent; font-family: Arial, sans-serif; }}
    .shell {{
        position: relative; padding: 4px; border-radius: 12px; overflow: hidden;
        clip-path: inset(0 round 12px); background: #0B3C49; box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }}
    .shell::before {{
        content: ""; position: absolute; width: 180%; height: 180%; left: -40%; top: -40%;
        background: conic-gradient(from 0deg, transparent 0deg 220deg, #A3E635 275deg, #0F766E 320deg, transparent 360deg);
        opacity: 0; transition: opacity 0.3s ease;
    }}
    .shell.active::before {{ opacity: 1; animation: spin 1.5s linear infinite; }}
    .card {{
        --x: 50%; --y: 50%; position: relative; z-index: 1; min-height: 140px;
        border-radius: 10px; overflow: hidden; clip-path: inset(0 round 10px); padding: 20px;
        background: radial-gradient(circle at var(--x) var(--y), rgba(163, 230, 53, 0.15), rgba(241, 250, 247, 0) 40%), #F1FAF7;
        color: #1F2933;
    }}
    .card h4 {{ margin-top: 0; border-bottom: 1px solid #ccc; padding-bottom: 5px; color: #1F2933; }}
    .valor {{ font-size: 26px; font-weight: 800; color: {color_valor}; }}
    .desc {{ margin-bottom: 0; font-size: 14px; opacity: 0.8; margin-top: 10px; color: #1F2933; }}
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
    </style>

    <div id="shell" class="shell">
        <div id="card" class="card">
            <h4>{titulo}</h4>
            <div class="valor">{valor}</div>
            <p class="desc">{descripcion}</p>
        </div>
    </div>

    <script>
    const shell = document.getElementById("shell");
    const card = document.getElementById("card");

    shell.addEventListener("mouseenter", () => shell.classList.add("active"));
    shell.addEventListener("mouseleave", () => {{
        shell.classList.remove("active");
        card.style.setProperty("--x", "50%");
        card.style.setProperty("--y", "50%");
    }});
    card.addEventListener("mousemove", (event) => {{
        const rect = card.getBoundingClientRect();
        card.style.setProperty("--x", (((event.clientX - rect.left) / rect.width) * 100) + "%");
        card.style.setProperty("--y", (((event.clientY - rect.top) / rect.height) * 100) + "%");
    }});
    </script>
    """
    components.html(html_code, height=altura)


def tarjeta_onda_expansiva(titulo, valor, descripcion="Haz clic en la tarjeta", altura=160):
    """
    Tarjeta con efecto visual de onda expansiva (Ripple Effect) al hacer clic.
    """
    html = f"""
    <style>
    body {{ margin: 0; padding: 10px; font-family: Arial, sans-serif; background: transparent; }}
    .ripple-card {{
        position: relative; overflow: hidden; background: #F1FAF7; border-left: 5px solid #0F766E;
        border-radius: 12px; padding: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        cursor: pointer; color: #1F2933; transition: transform 0.2s;
    }}
    .ripple-card:active {{ transform: scale(0.98); }}
    .ripple-card span.ripple {{
        position: absolute; background: rgba(15, 118, 110, 0.4); transform: translate(-50%, -50%);
        pointer-events: none; border-radius: 50%; animation: animate 1s linear infinite;
    }}
    @keyframes animate {{
        0% {{ width: 0px; height: 0px; opacity: 0.5; }}
        100% {{ width: 500px; height: 500px; opacity: 0; }}
    }}
    .valor {{ font-size: 26px; font-weight: 800; color: #0F766E; margin: 10px 0; }}
    </style>
    
    <div class="ripple-card" id="card">
        <h4 style="margin:0; border-bottom: 1px solid #ccc; padding-bottom: 5px;">{titulo}</h4>
        <div class="valor">{valor}</div>
        <p style="margin:0; font-size:14px; opacity: 0.8;">{descripcion}</p>
    </div>
    
    <script>
    document.getElementById('card').addEventListener('click', function(e) {{
        let x = e.clientX - e.target.getBoundingClientRect().left;
        let y = e.clientY - e.target.getBoundingClientRect().top;
        let ripples = document.createElement('span');
        ripples.classList.add('ripple');
        ripples.style.left = x + 'px';
        ripples.style.top = y + 'px';
        this.appendChild(ripples);
        setTimeout(() => ripples.remove(), 1000);
    }});
    </script>
    """
    components.html(html, height=altura)


def tarjeta_fluido_ondulante(titulo, valor, porcentaje_llenado, altura=180):
    """
    Tarjeta que simula dinámicamente un nivel de fluido o tanque.
    """
    html = f"""
    <style>
    body {{ margin: 0; padding: 10px; font-family: Arial, sans-serif; background: transparent; }}
    .wave-card {{
        position: relative; overflow: hidden; background: #1F2933; border-radius: 12px;
        padding: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); color: #F1FAF7; z-index: 1;
    }}
    .wave {{
        position: absolute; bottom: 0; left: 0; width: 100%; height: {porcentaje_llenado}%;
        background: #0F766E; z-index: -1; transition: height 0.5s;
    }}
    .wave::before, .wave::after {{
        content: ""; position: absolute; width: 200%; height: 200%;
        top: -50%; left: 50%; transform: translate(-50%, -75%); background: #1F2933;
    }}
    .wave::before {{ border-radius: 45%; animation: animate 5s linear infinite; }}
    .wave::after {{ border-radius: 40%; background: rgba(31, 41, 51, 0.5); animation: animate 10s linear infinite; }}
    @keyframes animate {{
        0% {{ transform: translate(-50%, -75%) rotate(0deg); }}
        100% {{ transform: translate(-50%, -75%) rotate(360deg); }}
    }}
    .valor {{ font-size: 26px; font-weight: 800; color: #A3E635; margin: 10px 0; text-shadow: 1px 1px 2px #000; }}
    </style>
    
    <div class="wave-card">
        <h4 style="margin:0; border-bottom: 1px solid rgba(255,255,255,0.2); padding-bottom: 5px;">{titulo}</h4>
        <div class="valor">{valor}</div>
        <p style="margin:0; font-size:14px; opacity: 0.8;">Nivel operativo: {porcentaje_llenado}%</p>
        <div class="wave"></div>
    </div>
    """
    components.html(html, height=altura)


def tarjeta_cyber_glitch(titulo, valor, descripcion="Pasa el cursor para desencriptar", altura=160):
    """
    Tarjeta con efecto de revelado de datos mediante animación secuencial.
    """
    html = f"""
    <style>
    body {{ margin: 0; padding: 10px; font-family: 'Courier New', Courier, monospace; background: transparent; }}
    .glitch-card {{
        background: #0B3C49; border: 1px solid #A3E635; border-radius: 8px; padding: 20px;
        color: #F1FAF7; box-shadow: inset 0 0 10px rgba(163, 230, 53, 0.2);
    }}
    .valor-glitch {{
        font-size: 24px; font-weight: bold; color: #A3E635; margin: 10px 0; min-height: 28px;
    }}
    </style>
    
    <div class="glitch-card" id="glitch-container">
        <h4 style="margin:0; border-bottom: 1px dashed #A3E635; padding-bottom: 5px;">{titulo}</h4>
        <div class="valor-glitch" id="val" data-target="{valor}">[PASE EL CURSOR]</div>
        <p style="margin:0; font-size:12px; opacity: 0.7;">{descripcion}</p>
    </div>
    
    <script>
    const container = document.getElementById('glitch-container');
    const valElement = document.getElementById('val');
    const targetText = valElement.getAttribute('data-target');
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*';
    
    container.addEventListener('mouseenter', () => {{
        let iteraciones = 0;
        clearInterval(valElement.interval);
        
        valElement.interval = setInterval(() => {{
            valElement.innerText = targetText.split('').map((letra, indice) => {{
                if(indice < iteraciones) return targetText[indice];
                return chars[Math.floor(Math.random() * chars.length)];
            }}).join('');
            
            if(iteraciones >= targetText.length) clearInterval(valElement.interval);
            iteraciones += 1/3;
        }}, 30);
    }});
    </script>
    """
    components.html(html, height=altura)
    
def tarjeta_hover_simple(titulo, descripcion, altura=180):
    """
    Renderiza una tarjeta informativa amplia con un efecto hover sutil,
    ideal para descripciones largas o propósitos de la aplicación.
    """
    html = f"""
    <style>
    body {{ margin: 0; padding: 10px; font-family: Arial, sans-serif; background: transparent; }}
    .hover-card {{
        background-color: #1F2933;
        padding: 25px;
        border-radius: 12px;
        border-left: 5px solid #0F766E;
        color: #F1FAF7;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }}
    .hover-card:hover {{
        transform: translateY(-5px);
        border-left-color: #A3E635;
        box-shadow: 0 10px 25px rgba(163, 230, 53, 0.2);
    }}
    .hover-titulo {{
        color: #F1FAF7;
        margin-top: 0;
        font-size: 20px;
        margin-bottom: 15px;
    }}
    .hover-desc {{
        font-size: 15px;
        line-height: 1.6;
        margin: 0;
        opacity: 0.9;
    }}
    </style>
    
    <div class="hover-card">
        <h4 class="hover-titulo">{titulo}</h4>
        <p class="hover-desc">{descripcion}</p>
    </div>
    """
    components.html(html, height=altura)
