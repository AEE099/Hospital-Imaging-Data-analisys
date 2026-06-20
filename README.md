# Hospital-Imaging-Data-analisys
Análisis de Demanda y Productividad del Departamento de Imagenología: Este proyecto utiliza análisis de datos y Machine Learning para identificar estacionalidad, optimizar el flujo de trabajo y predecir la demanda de estudios, incluyendo una automatización con pipeline y una aplicación interactiva con Streamlit.
# Análisis de Demanda y Productividad - Departamento de Imagenología (2024)

**Autor:** Alonzo Encarnacion

📌 **Descripción del Proyecto**

Este proyecto se enfoca en un análisis exhaustivo del volumen de estudios realizados en el Departamento de Imagenología durante el lapso de anos 2022-2024. El objetivo principal es identificar patrones de estacionalidad, comprender la participación de cada modalidad de imagenología y proponer optimizaciones en el flujo de atención al paciente. Además, se ha desarrollado un modelo de Machine Learning para la predicción de la demanda, una automatización del proceso mediante un pipeline y una aplicación interactiva con Streamlit para la visualización dinámica de los resultados.

---

📊 **Objetivos del Análisis**

*   **Limpieza y Preparación de Datos:** Transformar datos brutos de reportes (incluyendo eliminación de filas de control y desnormalización a formato largo).
*   **Análisis Descriptivo:** Cuantificar el volumen total y la participación porcentual de cada modalidad de estudio.
*   **Análisis Temporal y Estacional:** Evaluar las tendencias mensuales de la demanda para identificar picos y comportamientos estacionales.
*   **Segmentación Operacional:** Clasificar los estudios por complejidad (Alta Rotación, Alta Complejidad, Intervencionismo) para entender la carga de trabajo real.
*   **Visualización de Datos:** Crear gráficos claros y concisos para facilitar la toma de decisiones operativas.
*   **Modelado Predictivo (Machine Learning):** Desarrollar y optimizar modelos para pronosticar la demanda futura de estudios.
*   **Automatización de Procesos:** Implementar un pipeline end-to-end para procesar nuevos datos y generar reportes automáticamente.
*   **Despliegue Interactivo:** Desarrollar una aplicación en Streamlit para visualizar resultados y permitir la interacción con los datos y predicciones.

---

🧠 **Metodología**

1.  **Fase 1: Preparación de Datos**
    *   Lectura y carga de datos desde archivos `.xlsx`.
    *   Limpieza exhaustiva: eliminación de filas de subtotales, totales y cualquier otra información no operativa que pudiera introducir fuga de datos (`data leakage`).
    *   Transformación a formato largo (melt) para facilitar el análisis temporal y la segmentación.
2.  **Fase 2: Análisis Descriptivo**
    *   Cálculo del volumen total de estudios y la participación porcentual por modalidad.
3.  **Fase 3: Análisis de Tendencias y Estacionalidad**
    *   Agrupación de datos por mes para identificar patrones de demanda a lo largo del año.
    *   Creación de tablas pivote para una visión multivariable de las tendencias.
4.  **Fase 4: Segmentación por Complejidad Operativa**
    *   Clasificación de estudios en categorías: 'Alta Rotación / Baja Complejidad', 'Alta Complejidad / Mayor Tiempo', 'Procedimiento Intervencionismo', basada en criterios de recursos y tiempo.
    *   Cálculo de la participación de cada segmento en la carga operativa total.
5.  **Fase 5: Visualización de Datos**
    *   Uso de `Matplotlib` y `Seaborn` para generar gráficos que ilustran la distribución por complejidad, las modalidades más solicitadas y las tendencias mensuales.
6.  **Fase 6: Machine Learning para Predicción**
    *   **Preprocesamiento:** `OneHotEncoder` para variables categóricas (`ESTUDIO`, `MES`).
    *   **Modelos Evaluados:** Regresión Lineal, Ridge, Random Forest, Gradient Boosting, SVR.
    *   **Optimización de Hiperparámetros:** `GridSearchCV` utilizado para afinar `RandomForestRegressor` y `GradientBoostingRegressor`.
    *   **Auditoría de Sobreajuste y Fuga de Datos:** Implementación de una división cronológica estricta (entrenamiento en 2022-2023, prueba en 2024) para asegurar la capacidad predictiva del modelo en datos no vistos y mitigar la fuga de datos.
    *   **Selección del Mejor Modelo:** `GradientBoostingRegressor` resultó ser el modelo con mejor rendimiento tras la optimización.
    *   **Análisis de Importancia de Variables:** Identificación de los estudios más influyentes en la predicción de volumen.
7.  **Fase 7: Automatización End-to-End con Pipeline**
    *   Desarrollo de un script (`procesador_imagenes.py`) para encapsular la lógica de limpieza, transformación, clasificación y visualización, permitiendo la generación automática de reportes al ingresar nuevos archivos de datos.
8.  **Fase 8: Interfaz Interactiva con Streamlit**
    *   Creación de una aplicación `Streamlit` para presentar los análisis y permitir la interacción del usuario con las predicciones y gráficos generados.

---

📈 **Resultados Clave y Hallazgos Preliminares**

*   **Volumen Total:** Se analizaron un total de **272,059 estudios operativos** en el año 2024.
*   **Modalidades Dominantes:** Las **Sonografías** y los **Rayos X (RX)** representan la mayor proporción del volumen de estudios, confirmando su rol como modalidades de alta demanda.
*   **Carga Operativa:** La categoría de 'Alta Rotación / Baja Complejidad' es la que concentra el mayor volumen de estudios, indicando una operación eficiente para estos servicios.
*   **Estacionalidad:** Se observan patrones mensuales consistentes en la demanda de las principales modalidades, lo que sugiere oportunidades para la planificación de recursos.
*   **Rendimiento del Modelo ML:**
    *   El `GradientBoostingRegressor` fue seleccionado como el mejor modelo, alcanzando un **R2 Score de 0.9977** en el conjunto de prueba (2024) después de la mitigación de fuga de datos.
    *   El **MAE (Error Absoluto Medio) fue de 78.85** y el **RMSE (Raíz del Error Cuadrático Medio) de 144.66**, lo que indica una alta precisión en las predicciones.
    *   La auditoría cronológica mostró un `R2` en prueba de **0.9885** (en 2024) versus `R2` en entrenamiento de **0.9991** (en 2022-2023), sugiriendo un ajuste robusto sin sobreajuste significativo en la predicción de futuros datos.
*   **Variables más Importantes:** `ESTUDIO_SONOGRAFIAS` y `ESTUDIO_RX` son las variables con mayor importancia en el modelo predictivo, lo que subraya su impacto crítico en la demanda general.
*   **Proyecciones:** Se han generado proyecciones para 2025, mostrando una estimación del volumen de estudios para Sonografías, Tomografías y RX en los primeros meses.

---

🔜 **Trabajo Pendiente y Mejoras Futuras**

*   Integración de un mayor historial de datos (años anteriores) para entrenar modelos más robustos y capturar tendencias a largo plazo.
*   Análisis y modelado de la demanda a un nivel más granular (e.g., por clínica, por sala de estudio o por hora del día).
*   Mejoras en la interfaz de usuario de Streamlit para una experiencia más rica y funcionalidades personalizables por el usuario final.
*   Exploración de modelos de series temporales avanzados para mejorar la predicción de estacionalidad.
*   Implementación de un sistema de monitoreo de modelos para detectar el `model drift` y asegurar la validez de las predicciones a lo largo del tiempo.
*   Despliegue del modelo y la aplicación Streamlit en un entorno de producción para acceso continuo.

---

🛠️ **Tecnologías Utilizadas**

*   **Python:** Lenguaje principal de programación.
*   **Pandas:** Manipulación y análisis de datos.
*   **NumPy:** Operaciones numéricas y matemáticas.
*   **Matplotlib / Seaborn:** Visualización de datos y generación de gráficos estadísticos.
*   **Scikit-learn:** Desarrollo y evaluación de modelos de Machine Learning (Regresión Lineal, Ridge, Random Forest, Gradient Boosting, SVR, OneHotEncoder, ColumnTransformer, Pipeline, GridSearchCV).
*   **Jupyter Notebook / Google Colab:** Entorno de desarrollo interactivo.
*   **Streamlit:** Creación de aplicaciones web interactivas para la visualización de resultados.

---

⚙️ **Requisitos**

Para ejecutar este proyecto, instala las dependencias necesarias con pip:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl streamlit
```
