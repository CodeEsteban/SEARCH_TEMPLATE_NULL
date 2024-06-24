import os
import json

# Ruta del directorio donde se buscarán los archivos .form
ruta_base = r'C:\Users\ING ESTEBAN\Pictures\MacareniaBPMN-develop.kevin'

# Lista de nombres a verificar
nombres_a_verificar = [
"ARBOLES_AISLADOS_Requiere",
"AUTO_INFORMACION_REUNIDA",
"AUTO_INICIO_perm",
"AUTO_INICIO_perm2",
"AUTO_INICIO_perm2 (1)",
"AUTO_INICIO_PFMN",
"auto-info-reu",
"auto-requerimiento-sub",
"concepto-tecnico",
"concepto-tecnico-cad",
"concepto-tecnico-cda",
"concepto-tecnico-determinantes-ambientales",
"concepto-tecnico-determinantes-PP",
"concepto-tecnico-dom",
"concepto-tecnico-DPA",
"concepto-tecnico-ief",
"concepto-tecnico-lh",
"concepto-tecnico-liboper",
"concepto-tecnico-manejo",
"concepto-tecnico-ocup",
"concepto-tecnico-pdc",
"concepto-tecnico-perm",
"concepto-tecnico-prosp",
"concepto-tecnico-rcd",
"concepto-tecnico-sub",
"concepto-tecnico-sup",
"concepto-tecnico-tritura",
"concepto-tecnico-vege",
"concepto-tecnico-verti",
"CT_CONTI_ALMACENAMIENTO",
"CT_FIJAS",
"CT_LICENCIA_AMBIENTAL",
"CT-Aislado",
"CT-Forestal-Unico",
"desesti-verti",
"desestimiento-manejo",
"desestimiento-prox",
"desestimiento-trituradora",
"desestimineto-liboper",
"desiste-ocupa",
"Desistimiento EXP 22",
"Desistimiento_DPP",
"Desistimiento_EXP_22_21_DA",
"Desistimiento_PFMN",
"Desistimiento_PP",
"desistimiento-ace",
"desistimiento-cda",
"desistimiento-lh",
"desistimiento-rcd",
"FORMATO RES DETERMINANTES AMBIENTALES",
"OFICIO DE REQUERIMIENTO_DPA",
"oficio-aviso-alcaldia",
"oficio-aviso-cormacarena",
"Oficio-domes",
"oficio-remisorio-aviso",
"oficio-req-sup",
"plantilla",
"Plantilla Oficio_DPP",
"req-liboper",
"req-manejo",
"req-ofi-ocup",
"req-prox",
"req-trituradora",
"req-verti",
"requerimiento_cda",
"REQUERIMIENTO_DPA_COORDINADOR",
"Requerimiento_DPP",
"REQUERIMIENTO_FIJAS",
"REQUERIMIENTO_PDC",
"requerimiento-ace",
"requerimiento-cad",
"requerimiento-cda",
"requerimiento-domest",
"requerimiento-lh",
"requerimiento-sub",
"requiere-vege",
"RES_APRUEBA_PCDH",
"RES_DESISTIMIENTO_FIJAS",
"RES_DESISTIMIENTO_PCDH",
"RES_DESISTIMIENTO_TACITO_Aprovechamiento Fortestal",
"RES_MODIFICA_FIJAS",
"RES_MODIFICA_PCDH",
"RES_NIEGA_FIJAS",
"RES_OTORGA_FIJAS",
"RES_RENUEVA_FIJAS",
"RES_REVOCATORIA_LIC_AMB_TEMP",
"resolucion",
"RESOLUCION_ARCHIVO_Y_CIERRE_DEF",
"RESOLUCION_CESION_DERECHOS",
"RESOLUCION_MODIFICA_LICENCIA",
"RESOLUCION_NIEGA_LICENCIA",
"RESOLUCION_OTORGA_LICENCIA",
"RESOLUCION_OTORGA_LICENCIA_PERMISO",
"Resolucion_PFMN",
"RESOLUCION_PRORROGA",
"RESOLUCION_RESUELVE_RECURSO",
"RESOLUCION_SUSPENSION",
"resolucion-cad",
"resolucion-cda",
"resolucion-desiste-sub",
"resolucion-lh",
"resolucion-liboper",
"resolucion-ocupa",
"resolucion-pdc",
"resolucion-perm",
"resolucion-prosp",
"resolucion-rcd",
"resolucion-sub",
"resolucion-sup",
"resolucion-sup-nieg",
"resolucion-sup-prorr",
"resolucion-vege",
"resolucion-vege2",
"resolucion-verti-desist",
"resolucion-verti-niega",
"resolucion-verti-otorg",
"reunida-info",
"SUBROGACION_DERECHOS",
"Unico_Res_Aprovechamiento_Unico",
"Unico_Res_Aprueba_Medida_Compensacion",
"Unico_Res_Cambio_Compensacion",
"Unico_Res_CUMPLIMIENTO_ARCHIVO",
"Unico_Res_Niega_Aprovechamiento_Forestal",
"Unico_Res_Prorroga_AF",
"Unico_Resolucion_Resuelve_Reposicion_AF"
]

# Conjunto para guardar los nombres encontrados en los archivos
nombres_encontrados = set()

# Función para buscar en los directorios de forma recursiva
def buscar_archivos_form(ruta):
    for raiz, dirs, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo.endswith('.form'):
                ruta_completa = os.path.join(raiz, archivo)
                try:
                    with open(ruta_completa, 'r', encoding='utf-8') as archivo_json:
                        datos = json.load(archivo_json)
                        # Suponiendo que la estructura incluye un array o es directamente accesible
                        if isinstance(datos, dict):
                            extraer_templateName(datos)
                        elif isinstance(datos, list):  # Si los datos son una lista de diccionarios
                            for item in datos:
                                extraer_templateName(item)
                except json.JSONDecodeError:
                    print(f"Error al decodificar JSON en el archivo: {ruta_completa}")
                except Exception as e:
                    print(f"Error procesando el archivo {ruta_completa}: {str(e)}")

def extraer_templateName(elemento):
    if 'properties' in elemento and 'templateName' in elemento['properties']:
        nombre_template = elemento['properties']['templateName']
        nombres_encontrados.add(nombre_template)
    for key, value in elemento.items():
        if isinstance(value, dict):
            extraer_templateName(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    extraer_templateName(item)

# Ejecutar la función
buscar_archivos_form(ruta_base)

# Determinar qué nombres no se encontraron en los archivos .form
nombres_no_encontrados = [nombre for nombre in nombres_a_verificar if nombre not in nombres_encontrados]

print("Nombres que no aparecen en los archivos '.form':")
for nombre in nombres_no_encontrados:
    print(nombre)
