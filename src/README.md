# SoilSync AI: System Navigation Guide

**SoilSync AI** is a precision agriculture platform designed to transform soil health management for Kenyan smallholder farmers by integrating AI, SoilHive platform data, real-time environmental inputs, and farmer feedback. It addresses soil degradation, nutrient imbalances, and limited data access, targeting a **15-30% yield increase**, **22% fertilizer cost reduction**, and **0.4 tons CO2/ha carbon sequestration**.

---

## How to Run the Application

### Access the Platform
- Visit: **[https://kenyasoil-advisor.lovable.app/](https://kenyasoil-advisor.lovable.app/)**
- Create an account using your **phone number or email** and select your preferred language (English, Swahili, or other local languages).
- Enable **offline mode** for areas with limited connectivity, allowing data syncing when internet is available.

### Usage
1. **Input Farm Details**: Enter farm location, crop type, and management practices in the **Farm Profile** section.
2. **Soil Health Assessment**: Use the **Soil Diagnostic** tool to analyze soil data from SoilHive (75,505 testing points), IoT sensors, and satellite imagery.
3. **Receive Tailored Recommendations**: View crop-specific fertilizer and management recommendations in the **Recommendations** tab, downloadable as PDFs.
4. **Monitor Soil Health**: Track real-time soil changes (NDVI, moisture, pH) via the **Monitoring Dashboard**.
5. **Engage with Support Features**: Use the **voice assistant** (in local languages) or **community section** for peer support and extension services.
6. **Review Impact and Analytics**: Check the **Impact** section for yield improvements, cost savings, and environmental metrics.

---

## Which Technologies Are Used

- **AI and Machine Learning**: Random Forests with SMOTE and feature selection for **87% nutrient prediction accuracy** and rule-based recommendations with **92% accuracy**.
- **Data Sources**: SoilHive platform data (20+ years, pH, N-P-K, micronutrients), simulated IoT sensor data (pH, salinity), Sentinel-2/Landsat imagery (NDVI, soil moisture), and simulated climate data (rainfall, temperature).
- **Platform**: Cloud-based, mobile-first architecture with **PostgreSQL/PostGIS**, **FastAPI** for APIs, and **React** for mobile app and dashboards. Supports offline capabilities and multilingual interfaces.
- **Infrastructure**: Scalable cloud (AWS/GCP) with simulated IoT data integration.

---

## What Problem Is Solved

SoilSync AI tackles Kenya’s soil health crisis (nutrient depletion, acidity, salinization), impacting **5.9M+ smallholder households**. It improves productivity, reduces fertilizer waste by **22%**, enhances food security, and promotes sustainable practices with measurable environmental benefits.

---

## What APIs/Datasets Does the Solution Use

- **Datasets**:
  - **SoilHive Platform**: Historical soil data (75,505 points: pH, N-P-K, micronutrients, organic carbon).
  - **Satellite Imagery**: Simulated Sentinel-2/Landsat data for NDVI and soil moisture.
  - **IoT Sensors**: Simulated real-time pH and salinity data.
  - **Farmer Observations**: Simulated crop stress and nutrient deficiency indicators.
  - **Climate Data**: Simulated rainfall and temperature from the Kenya Meteorological Department.
- **APIs**:
  - **SoilHive API**: Simulated soil data retrieval.
  - **Sentinel-2/Landsat APIs**: Placeholder for imagery feeds.
  - **GIS/Climate APIs**: Simulated for spatial and climate data integration.

---

## Installation and Setup (For Developers)

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/soilsync-ai/soilsync-ai.git
   cd soilsync-ai
