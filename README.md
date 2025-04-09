
# 🌍 Where Should I Live in Scandinavia?

A **Streamlit app** that helps you find the best Scandinavian city to live in based on your personal and professional priorities — whether it's salary, access to nature, tech job opportunities, or mental well-being.

## 🚀 Features

- 🌆 Compares cities across **Sweden, Norway, Denmark, Finland, and Iceland**
- 🎯 Customize your preferences with **sliders** (salary, cost of living, work-life balance, etc.)
- 🔍 Calculates a **personalized score** for each city
- 🗺️ View cities on an **interactive map** with pop-up info
- 🎛️ Filter results by **minimum score threshold**
- 📊 See results in a dynamic table sorted by best match

## 📸 Screenshots

![App Screenshot](./images/app_screen.png)

## 🧠 How It Works

1. **Standardized** numeric metrics such as salary, nature score, tech job opportunities, and more.
2. Users assign **weights** to each factor based on their preferences.
3. A **composite score** is calculated for each city.
4. Results are displayed in a table and interactive map.

## 🛠️ Installation

Make sure you have Python 3.8+ installed.

```bash
# Clone the repo
git clone https://github.com/Nynor-code/scandi_recommender_app.git
cd scandi_recommender_app

# Install dependencies
pip install -r requirements.txt
```

## 📦 Run the App

```bash
streamlit run src/app.py
```

Then open your browser at `http://localhost:8501`.

## 🌐 Deployment

The app is deployed on **Streamlit Cloud**, and you can access it directly here:

[Streamlit Cloud Deployment](https://share.streamlit.io/Nynor-code/scandinavia-city-picker/main/)

## 📁 Project Structure

```
├── src/app.py     # Main application file
├── requirements.txt     # Python dependencies
├── README.md            # This file
```

## ✅ Dependencies

- `streamlit`
- `pandas`
- `folium`
- `streamlit-folium`
- `scikit-learn`

Install with:
```bash
pip install streamlit pandas folium streamlit-folium scikit-learn
```

## 🌱 Future Improvements

- Export recommendations (CSV, PDF)
- Add city profile cards with photos
- Support user accounts to save preferences
- Pull real-time data from APIs (cost, jobs, etc.)

## 📍 Inspiration

Created as part of a **Nordic-themed portfolio project** to support relocation decisions for tech professionals seeking better work-life balance and nature access.

## Data Sources

### Average Salary (EUR)
Sources:
* Numbeo (cost-of-living + salary comparisons)
* Statista and national statistics agencies (like SSB in Norway, SCB in Sweden)
* Job portals like Glassdoor, Levels.fyi, and local recruitment agencies
⚠ Note: salaries were normalized and scaled down by 10.

### Cost of Living Index
Sources:
* Numbeo
* Expatistan
* OECD living cost reports

### Nature Score (custom)
Subjective metric (1–10) based on Proximity to forests, lakes, mountains, national parks, and outdoor activity opportunities

Sources: 
* Google Maps
* Regional tourism data 
* Lifestyle rankings

### Mental Health Index (custom)
Estimated from:
* OECD Better Life Index
* WHO and Eurostat mental well-being reports
* Nordic health and happiness studies
* National mental health services access and societal factors

### Work-Life Balance
Based on:
* OECD Better Life Index
* Eurostat and Nordic Council reports
* Local labor laws (vacation, parental leave, work hours)

### Tech Job Score (custom)
Based on:
Local tech ecosystem maturity
Presence of startups, tech hubs, and accelerators
Remote work friendliness and demand for tech roles
Sources: 
* Dealroom
* Crunchbase
* EU tech job boards
* LinkedIn insights

### ⚠ Limitations
* Values are not official or real-time, but estimated and normalized to provide a consistent relative comparison across cities.
* The northern cities (e.g., Kiruna, Alta) are harder to get exact salary or tech scores for, so some were interpolated or scaled based on national/regional averages.

## 🧑‍💻 Author

Developed by [Nynor-code](https://github.com/Nynor-code).
