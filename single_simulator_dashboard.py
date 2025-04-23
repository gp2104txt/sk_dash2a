import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Single Simulator Dashboard", layout="wide")

st.title("✈️ Single Simulator Real-Time Overview")

# Simulator Health Summary
col1, col2, col3, col4 = st.columns(4)

col1.metric("Simulator Health Score", "92%", delta="-3%")
col2.metric("Operational State", "Running", delta=None)
col3.metric("Current Scenario", "ILS Landing", delta="75% complete")
col4.metric("Active Users", "Instructor: John Doe\nStudent: Jane Smith")

st.divider()

# Real-Time Metrics Section
st.subheader("📊 Real-Time Simulation Data")

col1, col2 = st.columns(2)

# 3D Aircraft Position (Simplified as Map)
with col1:
    st.write("**Ownship Position**")
    df_pos = pd.DataFrame({
        'lat': [37.7749],
        'lon': [-122.4194]
    })
    st.map(df_pos)

# Flight Attitude (Random Data Example)
with col2:
    st.write("**Ownship Attitude (°)**")
    attitude_df = pd.DataFrame({
        'Attitude': ['Pitch', 'Roll', 'Yaw'],
        'Value': [np.random.uniform(-10,10), np.random.uniform(-20,20), np.random.uniform(-180,180)]
    })
    st.bar_chart(attitude_df.set_index('Attitude'))

st.divider()

# Environmental and Hardware Status
st.subheader("🖥️ Hardware & Environment")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**CPU & RAM Usage (%)**")
    cpu_ram = pd.DataFrame({
        'Resource': ['CPU', 'RAM'],
        'Usage': [65, 78]
    })
    st.bar_chart(cpu_ram.set_index('Resource'))

with col2:
    st.write("**Storage Status (GB)**")
    storage = pd.DataFrame({
        'Disk': ['SSD1', 'SSD2'],
        'Used': [250, 400],
        'Free': [750, 600]
    })
    st.bar_chart(storage.set_index('Disk'))

with col3:
    st.write("**Environment (°C / %) **")
    env_data = {
        'Air Temp (°C)': 21,
        'Humidity (%)': 45,
        'Air Quality (CO₂ ppm)': 400
    }
    st.json(env_data)

st.divider()

# Detailed Diagnostics & Logs
st.subheader("🛠️ Process Status & Logs")

process_data = pd.DataFrame({
    'Process': ['Visual System', 'Flight Model', 'Instructor Station', 'Data Recorder'],
    'Status': ['Running', 'Running', 'Running', 'Idle'],
    'Alerts': ['None', 'None', 'Latency Warning', 'None']
})
st.dataframe(process_data, use_container_width=True)

st.button("🔧 Open Support Ticket")
