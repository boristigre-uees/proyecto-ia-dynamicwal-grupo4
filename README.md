# DynamicWal - Sistema de Optimización de Precios Dinámico para Retail

Proyecto final de Maestría en Inteligencia de Negocios y Ciencia de Datos.

## Descripción del Proyecto
DynamicWal es un sistema de inteligencia artificial diseñado para optimizar precios en el sector retail de manera dinámica. Utiliza técnicas avanzadas de machine learning y reinforcement learning para predecir demanda, modelar elasticidad de precios y sugerir precios óptimos que maximicen ingresos.

### Entregables Completos
- **Motor de optimización de precios**: Reinforcement Learning con Q-Learning
- **Dashboard de control de precios**: Aplicación interactiva con Streamlit
- **Simulador de escenarios**: Slider para probar diferentes precios y ver impacto en revenue
- **API para integración con POS**: API REST con FastAPI
- **Reportes de impacto financiero**: Métricas de uplift estimado y reducción de stockouts

## Dashboard Interactivo en Vivo (Streamlit Cloud)
**Link público del dashboard (accesible desde cualquier dispositivo):**
https://proyecto-ia-dynamicwal-grupo-9uuhi6novydeuw3erbvfma.streamlit.app/

## Estructura del Repositorio
proyecto-ia-dynamicwal-grupo4/
├── README.md
├── requirements.txt
├── setup.py
├── data/
│   ├── raw/               # Datos crudos (ej. walmart_sales.csv)
│   ├── processed/         # Datos limpios generados
│   └── external/          # Datos externos (opcional)
├── src/
│   ├── init.py
│   ├── data/              # Preprocesamiento
│   ├── models/            # Modelos (Q-Learning)
│   ├── features/          # Feature engineering
│   ├── visualization/    # Funciones de gráficos
│   └── utils/             # Utilidades
├── models/
│   ├── trained_models/    # Modelos entrenados (vacío por ahora)
│   └── model_configs/     # Configuraciones
├── notebooks/
│   ├── exploratory/       # Análisis exploratorio
│   ├── modeling/          # Modelado y forecasting
│   └── evaluation/        # Evaluación
├── api/
│   ├── app.py             # API principal con FastAPI
│   ├── routes/            # Endpoints (pricing.py)
│   └── schemas/           # Modelos de datos Pydantic
├── dashboard/             # Dashboard interactivo
│   └── app.py
├── tests/                 # Pruebas unitarias (estructura)
├── docs/                  # Documentación
│   └── propuesta.md       # Propuesta original del proyecto
└── docker/                # Configuración Docker (estructura)
text## Cómo Ejecutar el Proyecto

### 1. Clonar el repositorio
```bash
*git clone https://github.com/boristigre-uees/proyecto-ia-dynamicwal-grupo4.git
*cd proyecto-ia-dynamicwal-grupo4
*2. Instalar dependencias
*Bashpip install -r requirements.txt
*3. Ejecutar el Dashboard Interactivo
*Bashstreamlit run dashboard/app.py

*Se abrirá en el navegador
*Incluye: predicción de ingresos, elasticidad, precio óptimo sugerido, simulador de escenarios y reportes de impacto

*4. Ejecutar la API para integración con POS
*Bashuvicorn api.app:app --reload

*Se abrirá en http://127.0.0.1:8000
*Documentación interactiva: http://127.0.0.1:8000/docs
*Endpoint principal: POST /optimize-price (devuelve precio óptimo y uplift)

*5. Ejecutar notebooks de análisis

*Abre los notebooks en notebooks/modeling/ con Jupyter o VS Code
*Incluyen forecasting con Prophet, análisis de elasticidad y experimentos

*Tecnologías Utilizadas

*Python 3.11+
*Pandas, NumPy, Matplotlib
*Prophet (forecasting)
*Statsmodels (elasticidad)
*FastAPI + Uvicorn (API)
*Streamlit (dashboard)
*Reinforcement Learning (Q-Learning personalizado)

*Autor
*Boris Tigre
*Maestría en Inteligencia de Negocios y Ciencia de Datos
*¡Proyecto completo y funcional! Quedo a disposición para cualquier consulta o demostración.