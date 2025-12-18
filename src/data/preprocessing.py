import pandas as pd

def clean_and_prepare_data(file_path):
    print("=== INICIANDO LIMPIEZA DE DATOS ===")
    print("Cargando archivo:", file_path)
    
    df = pd.read_csv(file_path)
    
    print("Columnas encontradas:", df.columns.tolist())
    print("Número de filas:", len(df))
    
    # Buscar columna de fecha
    date_col = None
    for col in df.columns:
        if 'date' in col.lower():
            date_col = col
            break
    
    if date_col:
        df['Date'] = pd.to_datetime(df[date_col])
        print(f"Fecha convertida desde columna '{date_col}'")
    else:
        print("No se encontró columna de fecha. Usando rango temporal por defecto.")
        df['Date'] = pd.date_range(start='2010-02-05', periods=len(df), freq='W-FRI')
    
    # Llenar NaN con 0 (simple y efectivo)
    df = df.fillna(0)
    
    # Crear columnas útiles
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Week'] = df['Date'].dt.isocalendar().week
    df['Is_Holiday_Week'] = 1 if 'IsHoliday' in df.columns and df['IsHoliday'].any() else 0
    
    # Guardar
    processed_path = '../../data/processed/walmart_sales_processed.csv'
    df.to_csv(processed_path, index=False)
    print(f"\n¡ÉXITO TOTAL! Datos procesados y guardados en:")
    print(processed_path)
    print(f"Filas finales: {len(df)} | Columnas finales: {len(df.columns)}")
    
    return df

print("FUNCIÓN clean_and_prepare_data CARGADA CORRECTAMENTE EN EL ARCHIVO")  # Esta línea es clave para verificar