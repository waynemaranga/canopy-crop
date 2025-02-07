# Classification Challenge

## Objective

Develop a machine learning model to classify land cover pixels into **Forest Tree Cover, Cocoa Crops, or Palm Plantations** using **multi-year Sentinel-2 satellite imagery**. Minimize confusion between natural forests and agricultural plantations

## Dataset & Features

- **Sentinel-2 Imagery**: 13 spectral bands per pixel. Each band captures different aspects of vegetation and surface properties. Additional derived indices (NDVI, NDMI, NDWI, CI). **NDVI Calculation** helps differentiate vegetation types.
- **Temporal Data**: 3 years of imagery to capture land cover changes over time; observations every 5 days; this temporal depth is crucial as it captures the full growth cycles of these vegetation types.
- **Distinct AOIs for Training & Testing**: Ensures model generalization. i.e Spatial Component. Data is organized by Areas of Interest (AOIs). AOIs are kept separate between training and testing sets to prevent spatial leakage; Each pixel has a unique identifier and timestamp

## Challenges

- **Spectral Confusion**: Forest vs. plantation crops may look similar.
- **Temporal Patterns Matter**: Crops grow at different rates, requiring time-series analysis.
- **Imbalanced Data**: Some land cover types may dominate, affecting accuracy.

## TODOs

### Preprocessing
- [ ] Handle missing data: interpolation/forward-backward fill <!-- TODO: swap between both/all methods, see which works best>
- [ ] Filter anomalous reflectance values and atmospheric noise
- [ ] Create time series features per pixel:
  - [ ] Rolling means (30-day windows) <!-- TODO: try different window sizes>
  - [ ] Seasonal statistics for each band (e.g., min, max, mean) <!-- TODO: try different stats>
  - [ ] Growth curve parameters (e.g., slope, intercept) <!-- TODO: try different curve types/parameters/fitting methods>
- [ ] Engineer additional spectral indices:
  - [ ] Enhanced Vegetation Index (EVI)
  - [ ] Soil Adjusted Vegetation Index (SAVI)
  - [ ] Canopy chlorophyll content index
- [ ]  Generate temporal metrics:
  - [ ]  Peak growing season values
  - [ ]  Standard deviation of seasonal patterns
  - [ ]  Phenological transition timing
- [ ]  Create aggregated features across years:
  - [ ]  Annual min/max/mean for each band
  - [ ]  Year-to-year variation metrics
  - [ ]  Seasonal amplitude calculations
  - [ ]  Scale features appropriately:
  - [ ]  Normalize spectral bands
  - [ ]  Scale derived indices consistently
  - [ ]  Handle outliers in temporal aggregates
  - [ ]  Structure data for model input:
  - [ ]  Organize features by AOI
  - [ ]  Create consistent temporal windows
  - [ ]  Format data for various model architectures (tabular vs sequential)


- [ ] Process multi-temporal satellite data
- [ ] Develop robust classification features
- [ ] Create a model that generalizes well across different AOIs

✅ **Extract Features**

- Compute NDVI for each year.
- Flatten spatial data into a structured dataset.

✅ **Prepare Labels**

- Convert land cover types into categorical labels (e.g., `0 = Forest, 1 = Cocoa, 2 = Palm`).

✅ **Split Data**

- Separate into **training and testing sets** (AOI-based).

---

### **2️⃣ Build & Train Models**

✅ **Baseline Model (Traditional ML)**

- **Random Forest (RF) or XGBoost**
- Input: Tabular format (bands + NDVI over 3 years).
- Output: Classification (Forest, Cocoa, Palm).

✅ **Deep Learning Model (CNNs)**

- **1D CNN**: Uses spectral data over time for each pixel.
- **2D CNN**: Uses spatial information from neighboring pixels.
- **3D CNN**: Uses both spatial and temporal data.

---

### **3️⃣ Model Evaluation & Comparison**

✅ Compare **accuracy, precision, recall, F1-score** across models.  
✅ Use a **confusion matrix** to analyze misclassifications.

---

## **🎯 Expected Outcome**

🚀 **Goal**: Achieve high classification accuracy while minimizing confusion between classes.  
📈 **Deliverables**:

- Trained models (RF + CNNs).
- Evaluation results (accuracy, confusion matrix).
- Insights on feature importance (e.g., which bands matter most).

---

## **🔜 Next Steps**

🔹 Format dataset for **Random Forest baseline test**.  
🔹 Train **1D CNN** as a first deep learning approach.  
🔹 Expand to **2D/3D CNNs** if needed.
