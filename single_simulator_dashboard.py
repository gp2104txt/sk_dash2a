import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Single Simulator Dashboard", layout="wide")

st.title("✈️ Single Simulator Real-Time Overview")

# Simulator Health Summary
col1, col2, col3, col4 = st.columns(4)

col1.metric("Simulator Health Score", "92%", delta="-3%")
col2.metric("Operational State", "Running")
col3.metric("Current Scenario", "ILS Landing", delta="75% complete")
col4.metric("Active Users", "Instructor: John Doe\nStudent: Jane Smith")

st.divider()

# Real-Time Metrics Section
st.subheader("📊 Real-Time Simulation Data")

col1, col2 = st.columns(2)

# Ownship Position
with col1:
    st.write("**Ownship Position**")
    df_pos = pd.DataFrame({
        'lat': [37.7749],
        'lon': [-122.4194]
    })
    st.map(df_pos)

# Flight Attitude
with col2:
    st.write("**Ownship Attitude (°)**")
    attitude_df = pd.DataFrame({
        'Pitch': [np.random.uniform(-10,10)],
        'Roll': [np.random.uniform(-20,20)],
        'Yaw': [np.random.uniform(-180,180)]
    })
    st.bar_chart(attitude_df.T)

st.divider()

# Environmental and Hardware Status
st.subheader("🖥️ Hardware & Environment")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**CPU & RAM Usage (%)**")
    cpu_ram = pd.DataFrame({'CPU': [65], 'RAM': [78]})
    st.bar_chart(cpu_ram.T)

with col2:
    st.write("**Storage Status (GB)**")
    storage = pd.DataFrame({'Used': [250, 400], 'Free': [750, 600]}, index=['SSD1', 'SSD2'])
    st.bar_chart(storage)

with col3:
    st.write("**Environment**")
    st.json({'Air Temp (°C)': 21, 'Humidity (%)': 45, 'Air Quality (CO₂ ppm)': 400})

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
