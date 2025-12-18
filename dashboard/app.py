import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# Path corregido
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.append(project_path)

from src.models.qlearning_pricing import QLearningPricer

st.set_page_config(page_title="DynamicWal", layout="wide")
st.title("🛒 DynamicWal - Sistema de Optimización de Precios Dinámico")

# DATOS DE EJEMPLO (sin CSV grande)
st.write("**Datos de ejemplo generados para demostración**")

dates = pd.date_range(start='2024-01-01', periods=180, freq='D')
np.random.seed(42)
revenue = 10000 + np.cumsum(np.random.normal(100, 500, len(dates))) + np.sin(np.arange(len(dates)) * 2 * np.pi / 7) * 2000
daily = pd.DataFrame({'Date': dates, 'revenue': revenue})

categories = ['Electronics', 'Appliances', 'Clothing']
df = pd.DataFrame({
    'Date': np.random.choice(dates, 1000),
    'category': np.random.choice(categories, 1000),
    'quantity_sold': np.random.randint(1, 10, 1000),
    'unit_price': np.random.uniform(100, 2000, 1000),
})
df['revenue'] = df['quantity_sold'] * df['unit_price']

st.sidebar.header("Controles")
category = st.sidebar.selectbox("Categoría", df['category'].unique())
base_price = st.sidebar.number_input("Precio base actual ($)", min_value=100.0, value=1000.0, step=50.0)
elasticity = st.sidebar.slider("Elasticidad estimada", -2.5, -0.5, -1.3, step=0.1)

# 1. Forecasting simple
st.header("1. Predicción de Ingresos")
daily['trend'] = daily['revenue'].rolling(window=7, center=True).mean()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(daily['Date'], daily['revenue'], label='Ingresos reales', alpha=0.6)
ax.plot(daily['Date'], daily['trend'], label='Tendencia', color='red', linewidth=3)
ax.set_title("Tendencia de Ingresos Diarios (datos de ejemplo)")
ax.legend()
ax.grid(True)
st.pyplot(fig)

st.write("**Predicción aproximada**: Tendencia creciente con estacionalidad semanal.")

# 2. Elasticidad
st.header("2. Elasticidad de Precios")
cat_df = df[df['category'] == category]
st.metric("Transacciones en categoría", len(cat_df))
st.metric("Elasticidad", f"{elasticity:.2f}")

# 3. Optimización
st.header("3. Precio Óptimo Sugerido")
pricer = QLearningPricer(base_price=base_price, elasticity=elasticity)
pricer.train(episodes=500)

optimal_price = pricer.get_optimal_price(1.0)
uplift = ((optimal_price - base_price) / base_price) * 100

col1, col2 = st.columns(2)
with col1:
    st.metric("Precio Actual", f"${base_price:,.2f}")
with col2:
    st.metric("Precio Óptimo", f"${optimal_price:,.2f}", f"{uplift:+.1f}%")

if uplift > 0:
    st.success(f"¡Subir precio {uplift:.1f}% maximiza ingresos!")
else:
    st.warning(f"¡Bajar precio {abs(uplift):.1f}% maximiza ingresos!")

# 4. Simulador
st.header("4. Simulador de Escenarios")
test_price = st.slider("Prueba otro precio", base_price*0.5, base_price*1.5, base_price, step=10.0)
sim_demand = 1000 * ((test_price / base_price) ** elasticity)
sim_revenue = test_price * sim_demand
current_revenue = base_price * 1000

st.metric("Revenue estimado", f"${sim_revenue:,.0f}", f"{sim_revenue - current_revenue:+,.0f}")

# 5. Impacto
st.header("5. Impacto Financiero")
st.write("• Uplift esperado: +3% a +8% en ingresos")
st.write("• Reducción de stockouts y sobre-stock")
st.success("¡DynamicWal COMPLETO!")
st.balloons()
