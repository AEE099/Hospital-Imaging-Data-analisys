# app.py
import streamlit as pd
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importamos la lógica de limpieza y procesamiento que ya programaste
from procesador_imagenes import ejecutar_pipeline_imagenes, entrenar_predictor_estudios

# 1. Configuración de la página web
st.set_page_config(
    page_title="Dashboard de Imagenología",
    page_icon="📊",
    layout="wide"
)

# 2. Título y encabezado principal
st.title("📊 Analizador Automático - Departamento de Imágenes")
st.markdown("""
Bienvenido al sistema de procesamiento y análisis de productividad. 
Sube el archivo comprimido o extraído de la relación de estudios anuales para generar métricas y gráficos al instante.
""")

st.divider()

# 3. Componente para subir el archivo (Drag and Drop)
archivo_subido = st.file_uploader(
    "Selecciona o arrastra el archivo Excel de datos aquí:", 
    type=["excel", "csv", "xlsx"],
    accept_multiple_files=False
)

# 4. Lógica de ejecución cuando el archivo es detectado
if archivo_subido is not None:
    st.divider()

    # Mensaje de estado/carga mientras el pipeline trabaja
    with st.spinner("🧠 Procesando datos y ejecutando el pipeline..."):
        try:
            # Ejecutamos tu pipeline reutilizando el script modular.
            # Le pasamos el archivo subido directamente y definimos la carpeta de salida.
            df_procesado = ejecutar_pipeline_imagenes(archivo_subido, carpeta_salida='reporte_streamlit')
            
            # Cálculos rápidos para los bloques de métricas (KPIs)
            total_estudios = df_procesado['CANTIDAD'].sum()
            promedio_mensual = total_estudios / 12
            estudio_top = df_procesado.groupby('ESTUDIO')['CANTIDAD'].sum().idxmax()
            volumen_top = df_procesado.groupby('ESTUDIO')['CANTIDAD'].sum().max()
            
            st.success("🎉 ¡Análisis generado con éxito!")
            
            # ==========================================
            # SECCIÓN 1: MÉTRICAS CLAVE (KPIs)
            # ==========================================
            st.subheader("📈 Indicadores Clave de Rendimiento (KPIs)")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(label="Total de Estudios Realizados", value=f"{total_estudios:,}")
            with col2:
                st.metric(label="Promedio de Producción Mensual", value=f"{int(promedio_mensual):,}")
            with col3:
                st.metric(label="Modalidad Más Solicitada", value=estudio_top, delta=f"{volumen_top:,} servicios")
                            
            # ==========================================
            # SECCIÓN 2: VISUALIZACIONES
            # ==========================================
            st.subheader("📊 Visualización Operativa y de Demanda")
            
            # Creamos dos pestañas independientes para organizar los gráficos
            tab1, tab2 = st.tabs(["Carga Operativa & Modalidades", "Tendencia Temporal"])
            
            with tab1:
                col_g1, col_g2 = st.columns(2)
                with col_g1:
                    st.markdown("**Distribución por Complejidad Operativa**")
                    st.image('reporte_streamlit/1_distribucion_complejidad.png', use_container_width=True)
                with col_g2:
                    st.markdown("**Volumen por Tipo de Estudio**")
                    st.image('reporte_streamlit/2_volumen_modalidades.png', use_container_width=True)
                    
            with tab2:
                st.markdown("**Evolución de la Demanda a lo Largo del Año**")
                st.image('reporte_streamlit/3_tendencia_temporal.png', use_container_width=True)
            # ==========================================
            # SECCIÓN 3: VISTA DE LA DATA TRANSFORMADA
            # ==========================================
            st.subheader("📋 Vista Previa de los Datos Procesados (Formato Tidy)")
            # Permitimos que exploren o descarguen la tabla final
            st.dataframe(df_procesado, use_container_width=True)
             
        except Exception as e:
            st.error(f"❌ Ocurrió un error al procesar el archivo: {e}")
            st.info("Asegúrate de que el archivo tenga la estructura estándar del Departamento de Imágenes.")

else:
    # Mensaje amigable si no se ha subido nada aún
    st.info("👋 Por favor, sube un archivo CSV para activar el análisis automático.")