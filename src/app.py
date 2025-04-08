import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
from sklearn.preprocessing import StandardScaler

# Sample data (normally load from CSV or external file)
data_base = {
    "City": ["Stockholm", "Oslo", "Copenhagen", "Helsinki", "Reykjavik", "Gothenburg", "Aarhus", "Tampere"],
    "Country": ["Sweden", "Norway", "Denmark", "Finland", "Iceland", "Sweden", "Denmark", "Finland"],
    "Latitude": [59.3293, 59.9139, 55.6761, 60.1699, 64.1466, 57.7089, 56.1629, 61.4978],
    "Longitude": [18.0686, 10.7522, 12.5683, 24.9384, -21.9426, 11.9746, 10.2039, 23.7610],
    "Avg_Salary_EUR": [3500, 3800, 3700, 3300, 4000, 3400, 3600, 3200],
    "Cost_of_Living_Index": [70, 75, 72, 68, 78, 65, 69, 60],
    "Nature_Score": [8.5, 9.0, 7.8, 8.2, 9.5, 8.7, 8.0, 8.4],
    "Mental_Health_Index": [7.8, 7.5, 7.9, 7.6, 8.0, 7.7, 7.8, 7.4],
    "Work_Life_Balance": [8.0, 8.2, 8.5, 8.3, 8.7, 8.1, 8.4, 8.0],
    "Tech_Job_Score": [8.2, 7.9, 8.4, 7.8, 6.5, 7.5, 7.6, 6.8]
}

data = {
    "City": ["Reykjavik", "Trondheim", "Oslo", "Bergen", "Copenhagen", "Aarhus", "Helsinki", "Stockholm", "Tampere", "Gothenburg", "Malmo", 
             "Rovaniemi", "Tromsø", "Luleå", "Umeå", "Kiruna", "Alta", "Narvik", "Oulu", "Bodø"],
    "Country": ["Iceland", "Norway", "Norway", "Norway", "Denmark", "Denmark", "Finland", "Sweden", "Finland", "Sweden", "Sweden", 
                "Finland", "Norway", "Sweden", "Sweden", "Sweden", "Norway", "Norway", "Finland", "Norway"],
    "Latitude": [64.1466, 63.4305, 59.9139, 60.39299, 55.6761, 56.1629, 60.1695, 59.3293, 61.4991, 57.7089, 55.6049, 66.5039, 
                 69.6496, 65.5848, 63.8258, 67.8558, 69.9656, 68.4384, 65.0125, 67.2804],
    "Longitude": [-21.9426, 10.3951, 10.7522, 5.32415, 12.5683, 10.2039, 24.9354, 18.0686, 23.7871, 11.9746, 13.0038, 25.7294, 
                  18.9560, 22.1567, 20.2630, 20.2253, 23.2712, 17.4423, 25.4682, 14.4048],
    "Avg_Salary_EUR": [3500, 4500, 5000, 4700, 5500, 4800, 4600, 4800, 4300, 4700, 4500, 3300, 3900, 3700, 3600, 3400, 3300, 3100, 3700, 3300],
    "Cost_of_Living_Index": [7.0, 6.5, 7.5, 6.8, 6.5, 6.3, 6.0, 6.4, 5.8, 6.2, 6.1, 5.5, 7.0, 6.5, 6.3, 7.2, 6.2, 6.3, 6.1, 6.5],
    "Nature_Score": [8.5, 9.0, 8.0, 8.8, 7.0, 7.5, 7.8, 8.0, 8.5, 8.2, 7.8, 9.5, 9.0, 9.0, 8.5, 9.5, 9.0, 9.2, 8.4, 9.2],
    "Mental_Health_Index": [8.0, 8.5, 9.0, 8.2, 8.8, 8.0, 8.5, 8.6, 8.0, 8.4, 8.2, 9.0, 8.5, 8.4, 8.2, 8.0, 8.5, 8.3, 8.1, 8.2],
    "Work_Life_Balance": [5.87, 6.5, 6.32, 6.2, 7.05, 6.8, 6.51, 6.48, 6.2, 6.07, 5.8, 7.0, 6.6, 6.5, 6.7, 6.8, 6.3, 6.6, 6.4, 6.5],
    "Tech_Job_Score": [7.5, 8.0, 8.5, 7.8, 9.0, 8.5, 8.8, 9.0, 8.0, 8.5, 8.0, 7.5, 8.0, 7.8, 8.2, 7.9, 7.8, 7.5, 8.1, 7.6]
}


# Convert to DataFrame
df = pd.DataFrame(data)

# Sidebar sliders for user preferences
st.sidebar.header("Set Your Preferences")
salary_weight = st.sidebar.slider("Salary Importance", 0, 5, 3)
cost_weight = st.sidebar.slider("Cost of Living Importance", 0, 5, 3)
nature_weight = st.sidebar.slider("Nature Access Importance", 0, 5, 4)
mental_weight = st.sidebar.slider("Mental Health Importance", 0, 5, 3)
wlb_weight = st.sidebar.slider("Work-Life Balance Importance", 0, 5, 4)
tech_weight = st.sidebar.slider("Tech Job Availability Importance", 0, 5, 3)

# Score filter
score_threshold = st.sidebar.slider("Minimum Score Filter", -10.0, 10.0, 0.0, step=0.1)

# Standardize features for scoring
features = [
    "Avg_Salary_EUR",
    "Cost_of_Living_Index",
    "Nature_Score",
    "Mental_Health_Index",
    "Work_Life_Balance",
    "Tech_Job_Score"
]
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df[features]), columns=features)

# Invert cost of living so lower cost is better
df_scaled["Cost_of_Living_Index"] *= -1

# Compute custom score
weights = [
    salary_weight,
    cost_weight,
    nature_weight,
    mental_weight,
    wlb_weight,
    tech_weight
]
df["Score"] = df_scaled.dot(weights)

# Filter based on score
df_filtered = df[df["Score"] >= score_threshold]

# Display results
st.title("🇸🇪 Where Should I Live in Scandinavia?")
st.write("This tool recommends cities based on your lifestyle and career preferences.")

st.dataframe(df_filtered.sort_values(by="Score", ascending=False).reset_index(drop=True))

# Interactive Map
st.subheader("📍 Explore Cities on the Map")

map_center = [63.0, 15.0]
m = folium.Map(location=map_center, zoom_start=4)
marker_cluster = MarkerCluster().add_to(m)

for _, row in df_filtered.iterrows():
    popup_text = (
        f"<b>{row['City']}, {row['Country']}</b><br>"
        f"Score: {row['Score']:.2f}<br>"
        f"Salary: €{row['Avg_Salary_EUR']}<br>"
        f"Cost Index: {row['Cost_of_Living_Index']}"
    )
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=popup_text,
        tooltip=row["City"]
    ).add_to(marker_cluster)

st_folium(m, width=700, height=500)
