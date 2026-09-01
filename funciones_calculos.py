# =============================================================================
# ARCHIVO: funciones_calculos.py
# DESCRIPCIÓN: Módulo de cálculo matemático para la aplicación Oil & Gas.
# =============================================================================

#REVISADO CORRECTO

def calcular_produccion_ipr(presion_reservorio_psi, presion_burbuja_psi, indice_productividad_stbd_psi, presion_fondo_fluyente_psi):
    """
    Calcula el desempeño de afluencia (IPR) combinando el modelo lineal y el modelo de Vogel.
    """
    # 1. Cálculo del caudal a la presión de burbuja
    caudal_burbuja_stbd = indice_productividad_stbd_psi * (presion_reservorio_psi - presion_burbuja_psi)
    
    # 2. Cálculo del caudal máximo teórico
    termino_vogel = (indice_productividad_stbd_psi * presion_burbuja_psi) / 1.8
    caudal_maximo_stbd = caudal_burbuja_stbd + termino_vogel
    
    # 3. Determinación del caudal operativo según el régimen de presión
    if presion_fondo_fluyente_psi >= presion_burbuja_psi:
        # Régimen lineal (por encima de la presión de burbuja)
        caudal_operativo_stbd = indice_productividad_stbd_psi * (presion_reservorio_psi - presion_fondo_fluyente_psi)
        estado_regimen = "Sobre punto de burbuja (Flujo Lineal)"
    else:
        # Régimen no lineal de Vogel (por debajo de la presión de burbuja)
        relacion_presiones = presion_fondo_fluyente_psi / presion_burbuja_psi
        caudal_operativo_stbd = caudal_burbuja_stbd + termino_vogel * (1 - 0.2 * relacion_presiones - 0.8 * (relacion_presiones ** 2))
        estado_regimen = "Bajo punto de burbuja (Flujo de Vogel)"
        
    return {
        "caudal_operativo_stbd": round(caudal_operativo_stbd, 2),
        "caudal_burbuja_stbd": round(caudal_burbuja_stbd, 2),
        "caudal_maximo_stbd": round(caudal_maximo_stbd, 2),
        "estado_regimen": estado_regimen
    }
    
    #REVISADO CORRECTO

def calcular_presion_hidrostatica(peso_lodo_ppg, profundidad_medida_ft, profundidad_vertical_verdadera_ft, presion_formacion_psi):
    """
    Calcula el gradiente hidrostático, la presión ejercida por el lodo y el balance del pozo.

    """
    # 1. Validaciones lógicas y físicas de los parámetros de entrada
    if peso_lodo_ppg < 0:
        raise ValueError("El peso del lodo (MW) debe ser estrictamente positivo.")
    
    if profundidad_medida_ft <= 0 or profundidad_vertical_verdadera_ft <= 0:
        raise ValueError("Las profundidades MD y TVD deben ser mayores que cero.")
        
    if profundidad_vertical_verdadera_ft > profundidad_medida_ft:
        raise ValueError("Error geométrico: La profundidad vertical (TVD) no puede ser mayor que la profundidad medida (MD).")
        
    if presion_formacion_psi < 0:
        raise ValueError("La presión de formación (Pform) no puede ser un valor negativo.")

    # 2. Cálculo del gradiente y presión (Depende exclusivamente de TVD)
    gradiente_hidrostatico_psi_ft = 0.052 * peso_lodo_ppg
    
    presion_hidrostatica_psi = gradiente_hidrostatico_psi_ft * profundidad_vertical_verdadera_ft
    
    # 3. Cálculo del diferencial de presión
    diferencial_presion_psi = presion_hidrostatica_psi - presion_formacion_psi
    
    # 4. Determinación del estado de balance
    if diferencial_presion_psi > 50: 
        estado_balance = "Sobrebalance"
    elif diferencial_presion_psi < -50:
        estado_balance = "Bajo balance"
    else:
        estado_balance = "Balance aproximado"
        
    return {
        "gradiente_hidrostatico_psi_ft": round(gradiente_hidrostatico_psi_ft, 4),
        "presion_hidrostatica_psi": round(presion_hidrostatica_psi, 2),
        "diferencial_presion_psi": round(diferencial_presion_psi, 2),
        "estado_balance": estado_balance
    }

#POR REVISAR

def calcular_volumetria_poes(area_reservorio_acres, espesor_bruto_ft, relacion_net_to_gross, 
                             porosidad_efectiva_frac, saturacion_agua_inicial_frac, 
                             factor_volumetrico_inicial_rb_stb, factor_recobro_frac):
    """
    Estima el Petróleo Original en Sitio (POES) y el volumen recuperable.
    """
    # Validación para evitar división por cero
    if factor_volumetrico_inicial_rb_stb <= 0:
        raise ValueError("El factor volumétrico inicial (Boi) debe ser mayor a cero.")

    # 1. Cálculo del espesor neto
    espesor_neto_ft = espesor_bruto_ft * relacion_net_to_gross
    
    # 2. Cálculo del POES (constante 7758 para conversión a barriles)
    espacio_poroso_util = porosidad_efectiva_frac * (1 - saturacion_agua_inicial_frac)
    poes_stb = (7758 * area_reservorio_acres * espesor_neto_ft * espacio_poroso_util) / factor_volumetrico_inicial_rb_stb
    poes_mmstb = poes_stb / 1000000
    
    # 3. Cálculo del volumen recuperable
    volumen_recuperable_stb = poes_stb * factor_recobro_frac
    volumen_recuperable_mmstb = volumen_recuperable_stb / 1000000
    
    return {
        "espesor_neto_ft": round(espesor_neto_ft, 2),
        "poes_stb": round(poes_stb, 2),
        "poes_mmstb": round(poes_mmstb, 3),
        "volumen_recuperable_stb": round(volumen_recuperable_stb, 2),
        "volumen_recuperable_mmstb": round(volumen_recuperable_mmstb, 3)
    }