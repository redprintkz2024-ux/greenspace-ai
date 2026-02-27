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

    year1 = st.number_input("First Year", value=2020)
    year2 = st.number_input("Second Year", value=2026)

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
    zoom_start=12,
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri"
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
    with tab5:
    st.header("🧠 CNN Forest Segmentation Demo")

    st.write("""
    This module simulates a Convolutional Neural Network (CNN)
    performing forest segmentation on satellite imagery.
    """)

    # === Симуляция спутникового NDVI изображения ===
    ndvi_image = np.random.uniform(0.2, 0.9, (200, 200))

    # === "Сегментация" леса (как будто CNN выделяет лес) ===
    forest_mask = ndvi_image > 0.6  # лес если NDVI > 0.6

    forest_area_percent = np.sum(forest_mask) / forest_mask.size * 100

    st.subheader("NDVI Map")
    fig1, ax1 = plt.subplots()
    ax1.imshow(ndvi_image)
    ax1.set_title("Simulated NDVI")
    ax1.axis("off")
    st.pyplot(fig1)

    st.subheader("Forest Segmentation (CNN Output)")
    fig2, ax2 = plt.subplots()
    ax2.imshow(forest_mask)
    ax2.set_title("Forest Mask")
    ax2.axis("off")
    st.pyplot(fig2)

    st.subheader("Model Output")
    st.write(f"Estimated Forest Area: {forest_area_percent:.2f}%")

    if forest_area_percent < 40:
        st.error("⚠ Low forest coverage detected")
    elif forest_area_percent > 70:
        st.success("🌿 Dense healthy forest detected")
    else:
        st.info("🌳 Moderate forest coverage")

    st.progress(int(forest_area_percent) / 100)
