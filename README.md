# **VIPR — Villages Pickleball Ratings (Prototype)**
_An experimental Python project for analyzing pickleball games, player ratings, and match results._

## 🎯 **Overview**

**VIPR** (Villages Pickleball Ratings) is a Python-based analytics project designed to load, merge, and summarize pickleball game data.  
It demonstrates:

- Reading multiple CSV and JSON files  
- Merging game data with player rating information  
- Producing basic summaries of loaded datasets  
- Providing a clean, extensible structure for future analytics

This repo is a starting point for more advanced work — eventually supporting skill modeling, match prediction, DUPR comparison, and PCVG-style rating exploration.

## 📁 **Project Structure**

```
VIPR/
│
├── src/
│   └── main.py            # Main Python entry point
│
├── data/
│   ├── games_with_ratings.csv
│   ├── pickleball_games.csv
│   ├── player_ratings.csv
│   ├── games_with_ratings.json
│   ├── pickleball_games.json
│   └── player_ratings.json
│
├── requirements.txt       # Python dependencies
└── README.md
```

## ⚙️ **Features**

✔ Loads CSV and JSON game/rating files  
✔ Prints dataset shapes and basic summaries  
✔ Demonstrates merging game results with ratings  
✔ Prepares foundation for deeper analysis (e.g., skill modeling)  
✔ Clean, modular project layout  
✔ Uses a virtual environment for isolated development  

## 🚀 **Getting Started**

### **1. Clone the repo**
```bash
git clone https://github.com/jrdoran/VIPR.git
cd VIPR
```

### **2. Create & activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate   # macOS
```

### **3. Install dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the project**
```bash
python src/main.py
```

## 📊 **Data Description**

The `data/` folder contains sample pickleball datasets used for development:

- `games_with_ratings.*` — Games paired with known player ratings  
- `pickleball_games.*` — Basic match results (players + scores)  
- `player_ratings.*` — Individual player skill ratings between 3.9 and 5.0  

Files are provided in both **CSV** and **JSON** formats to demonstrate multiple data loaders.



This project is intentionally minimal, but serves as a foundation for:

- 📈 Rating algorithm experiments  
- 🤝 Player-partner chemistry analysis  
- 🧮 Predictive modeling (who would win?)  
- 🎭 DUPR vs. new rating models  
- 🏆 League analytics + match summaries  
- 🔗 Integration with 

## 👤 **Author**



## 📄 **License**

This project is for **personal and experimental use**.  
Formal licensing will be added if/when the project expands.
