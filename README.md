# Suite Computacional de Cálculos Petroleros

Esta plataforma web interactiva automatiza la evaluación de parámetros críticos en la ingeniería petrolera. Desarrollada en Python utilizando el framework Streamlit, la herramienta integra cálculos matemáticos con visualizaciones dinámicas mediante Plotly, operando sobre una interfaz de usuario optimizada con inyecciones profundas de HTML, CSS y componentes web.

## ⚙️ Módulos Técnicos

*   **Producción (IPR):** Calcula y grafica el Desempeño de Afluencia (Inflow Performance Relationship) de un pozo, modelando el comportamiento del fluido desde el reservorio utilizando el índice de productividad (J), la presión promedio y la presión de burbuja.
*   **Perforación (Balance Hidrostático):** Genera el perfil de presión hidrostática en función del peso del lodo (MW) y la profundidad vertical verdadera (TVD), validando gráficamente la profundidad actual del pozo.
*   **Reservorios (POES):** Estima el Petróleo Original en Sitio mediante análisis volumétrico y clasifica de forma interactiva la distribución entre el volumen de crudo recuperable y el remanente.

## 🏗️ Arquitectura del Proyecto

El código fuente obedece un estricto patrón de programación modular. Esta separación de responsabilidades aísla la lógica de enrutamiento, los cálculos de ingeniería, la estética visual y el renderizado de gráficos:

```text
├── .streamlit/
│   └── config.toml       # Variables de entorno y tema global (paleta oscura/lima)
├── app.py                # Enrutador principal y control de estado de sesión
├── home.py               # Vista de inicio con tarjetas interactivas animadas
├── ejercicios.py         # Lógica matemática e inputs para los módulos de cálculo
├── graficas.py           # Funciones aisladas para la generación de figuras en Plotly
├── estilos.py            # Inyecciones de CSS y constructores de componentes HTML personalizados
└── README.md             # Documentación técnica
