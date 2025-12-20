# DynamicWal — Sistema de Optimización de Precios Dinámico para Retail

DynamicWal es un **sistema de inteligencia artificial diseñado para optimizar precios en el sector retail** de forma dinámica.  
El proyecto integra técnicas de **Machine Learning, Forecasting, análisis de elasticidad de precios y simulación**, con el objetivo de mejorar ingresos y apoyar la toma de decisiones estratégicas.

Este repositorio corresponde al **Proyecto Final de materia Inteligencia artificial de la Maestría en Inteligencia de Negocios y Ciencia de Datos**.

---

## 🧠 Descripción General

DynamicWal utiliza datos históricos de ventas para:

- Predecir la **demanda futura** por producto.
- Estimar la **elasticidad de precios**.
- Recomendar **precios óptimos** que mejoren métricas clave (revenue, margen).
- Simular escenarios de precios para medir impacto.
- Integrarse con sistemas de punto de venta (POS) mediante API.

---

## 👥 Integrantes — Grupo 4

- Arnaldo Andrés Rojas Jupiter  
- Andres Asisclo Florencia Toala  
- Denisse Angie Flores Arellano  
- Boris Ricardo Tigre Loja  

---

## 📁 Estructura del repositorio

proyecto-ia-dynamicwal-grupo4/  
├── README.md  
├── requirements.txt  
├── setup.py  
├── data/  
│   ├── raw/              # Datos crudos  
│   ├── processed/        # Datos limpios para modelado  
│   └── external/         # Datos externos (opcional)  
├── src/  
│   ├── data/             # Preprocesamiento  
│   ├── features/         # Ingeniería de características  
│   ├── models/           # Modelos de IA (forecasting, pricing)  
│   ├── visualization/    # Gráficos y análisis  
│   └── utils/            # Utilidades generales  
├── models/  
│   ├── trained_models/   # Modelos entrenados  
│   └── model_configs/    # Configuración de modelos  
├── notebooks/  
│   ├── exploratory/      # Análisis exploratorio  
│   └── modeling/         # Entrenamiento de modelos  

---

## 🚀 Tecnologías Utilizadas

- Python 3.10+
- Pandas, NumPy
- Prophet (forecasting de demanda)
- Scikit-learn / Statsmodels
- FastAPI (API REST)
- Streamlit (dashboard interactivo)
- Reinforcement Learning (Q-Learning)

---

## 📦 Instalación

Clonar el repositorio:

    git clone https://github.com/boristigre-uees/proyecto-ia-dynamicwal-grupo4.git
    cd proyecto-ia-dynamicwal-grupo4

Instalar dependencias:

    pip install -r requirements.txt

---

## ▶️ Ejecución del Proyecto

### Dashboard interactivo

    streamlit run dashboard/app.py

### API de optimización de precios

    uvicorn api.app:app --reload

Acceso a documentación:

    http://127.0.0.1:8000/docs

---

## 📓 Notebooks

Los notebooks incluyen:

- Análisis exploratorio de datos
- Forecasting de demanda
- Elasticidad de precios
- Simulación de escenarios
- Evaluación de impacto en revenue

Ubicación:

    notebooks/

---

## 📈 Resultados Esperados

- Mejora en ingresos por producto
- Soporte cuantitativo para decisiones de pricing
- Simulación de escenarios realistas
- Arquitectura escalable para integración futura

---

## 📄 Licencia

Proyecto desarrollado con fines **académicos**.  
No destinado a uso comercial.

---
