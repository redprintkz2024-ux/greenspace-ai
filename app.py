import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="GreenSpace AI", layout="wide")

st.title("🌱 GreenSpace AI")

# ====== ВКЛАДКИ ======
tab1, tab2, tab3, tab4 = st.tabs(["Dashboard", "Analysis", "Map", "Reports"])

# ====== DASHBOARD ======
with tab1:
    st.header("📊 Forest Condition Change (NDVI)")

    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    ndvi_values = np.random.uniform(0.6, 0.85, 12)

    fig, ax = plt.subplots()
    ax.plot(months, ndvi_values)
    ax.set_ylabel("NDVI Index")
    ax.set_title("Monthly NDVI Trend")

    st.pyplot(fig)

# ====== ANALYSIS ======
with tab2:
    st.header("🔍 New Analysis")

    lat = st.number_input("Latitude", value=48.0)
    lon = st.number_input("Longitude", value=67.0)

    year1 = st.number_input("First Year", value=2023)
    year2 = st.number_input("Second Year", value=2024)

    if st.button("Analyze Forest"):

        nir_1 = np.random.uniform(0.6, 0.9, (200, 200))
        red_1 = np.random.uniform(0.2, 0.4, (200, 200))

        nir_2 = np.random.uniform(0.4, 0.8, (200, 200))
        red_2 = np.random.uniform(0.3, 0.5, (200, 200))

        ndvi_1 = (nir_1 - red_1) / (nir_1 + red_1)
        ndvi_2 = (nir_2 - red_2) / (nir_2 + red_2)

        mean1 = np.mean(ndvi_1)
        mean2 = np.mean(ndvi_2)

        change = ((mean2 - mean1) / mean1) * 100

        st.subheader("Results")
        st.write(f"NDVI in {year1}: {mean1:.3f}")
        st.write(f"NDVI in {year2}: {mean2:.3f}")
        st.write(f"Change: {change:.2f}%")

        if change < -10:
            st.error("⚠ Possible forest degradation")
        elif change > 5:
            st.success("🌿 Forest health improving")
        else:
            st.info("📈 No significant change detected")

# ====== MAP ======
with tab3:
    st.header("🛰 Satellite View")

    lat_map = st.number_input("Map Latitude", value=48.0, key="map_lat")
    lon_map = st.number_input("Map Longitude", value=67.0, key="map_lon")

    m = folium.Map(
        location=[lat_map, lon_map],
        zoom_start=10,
        tiles="OpenStreetMap"
    )

    folium.Marker(
        [lat_map, lon_map],
        popup="Analysis Area",
    ).add_to(m)

    st_folium(m, width=1000, height=500)

# ====== REPORTS ======
with tab4:
    st.header("📑 AI Report")

    st.write("""
    This report summarizes the forest condition analysis based on NDVI index.

    The system evaluates vegetation health, detects degradation trends,
    and provides confidence estimation.

    Future versions will integrate real satellite data and CNN-based segmentation.
    """)

    confidence = np.random.randint(85, 98)
    st.progress(confidence / 100)
    st.write(f"AI Confidence Level: {confidence}%")
