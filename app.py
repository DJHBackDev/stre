import streamlit as st
import pandas as pd
import os
from datetime import datetime

DATA_FILE = 'data.csv'

if not os.path.exists(DATA_FILE):
    df_init = pd.DataFrame(columns=['Fecha', 'Problema', 'Categoría', 'Descripción', 'Ubicación'])
    df_init.to_csv(DATA_FILE, index=False)

st.set_page_config(page_title="DataVeci - Reportes Comunitarios", layout="centered")

st.title("📍 DataVeci")
st.subheader("Registra problemas en tu comunidad y visualiza los reportes")

with st.form("form_reporte"):
    problema = st.text_input("Nombre del problema")
    categoria = st.selectbox("Categoría", ["Bache", "Basura", "Inseguridad", "Agua", "Luz", "Otro"])
    descripcion = st.text_area("Descripción")
    ubicacion = st.text_input("Ubicación (colonia, dirección, etc.)")
    submit = st.form_submit_button("Enviar reporte")

    if submit and problema and ubicacion:
        nueva_fila = {
            "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Problema": problema,
            "Categoría": categoria,
            "Descripción": descripcion,
            "Ubicación": ubicacion
        }
        df = pd.read_csv(DATA_FILE)
        df = pd.concat([df, pd.Series(nueva_fila).to_frame().T], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)
        st.success("✅ ¡Reporte enviado correctamente!")

st.markdown("## 📊 Reportes registrados")
df = pd.read_csv(DATA_FILE)
st.dataframe(df)

if not df.empty:
    st.markdown("### 📈 Reportes por categoría")
    st.bar_chart(df["Categoría"].value_counts())

