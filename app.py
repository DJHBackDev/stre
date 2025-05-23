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
st.subheader("Record issues in your community and view reports")

with st.form("form_reporte"):
    problema = st.text_input("Name of the problem")
    categoria = st.selectbox("Category", ["Pothole", "Trash", "Insecurity", "Water", "Light", "Other"])
    descripcion = st.text_area("Description")
    ubicacion = st.text_input("Location (neighborhood, address, etc.)")
    submit = st.form_submit_button("send reprt")

    if submit and problema and ubicacion:
        nueva_fila = {
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Problem": problema,
            "Category": categoria,
            "Description": descripcion,
            "Location": ubicacion
        }
        df = pd.read_csv(DATA_FILE)
        df = pd.concat([df, pd.Series(nueva_fila).to_frame().T], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)
        st.success("✅ ¡Reporte enviado correctamente!")

st.markdown("## 📊 Registered reports")
df = pd.read_csv(DATA_FILE)
st.dataframe(df)

if not df.empty:
    st.markdown("### 📈 Reports by category")
    st.bar_chart(df["Categoría"].value_counts())

