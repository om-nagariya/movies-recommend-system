# 🎬 Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

A **content-based movie recommendation system** built with **Python** and **Streamlit**.  
It recommends the **top 5 similar movies** based on a selected movie’s tags (genres, overview, cast, etc.) and fetches posters using the **TMDB API**.

---

## 🚀 Features

- **Interactive Web Interface** – User-friendly Streamlit UI  
- **Content-Based Filtering** – Uses *Cosine Similarity* for recommendations  
- **Real-time Posters** – Fetches movie posters dynamically using TMDB API  
- **Robust Error Handling** – Handles API failures and missing images  

---

## 🛠️ Tech Stack

- **Python** – Core logic  
- **Pandas** – Data manipulation  
- **Scikit-learn** – Similarity calculation  
- **Streamlit** – Web frontend  
- **TMDB API** – Poster fetching  

---

## 📂 Project Structure
```yaml
├── app.py # Main Streamlit application
├── tmdb_5000_credits.csv # Raw dataset (Credits)
├── tmdb_5000_movies.csv # Raw dataset (Movies)
├── preprocess.ipynb # Jupyter Notebook for preprocessing
├── movies_data.pkl # Pre-processed dataframe (Pickle file)
├── similarity.pkl # Similarity matrix (Pickle file)
├── requirements.txt # List of dependencies
└── README.md # Project documentation
```
---

# 🔧 How to Run Locally

## 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
```

## 2️⃣ Install dependencies
```bash 
streamlit run app.py
```

---

# 🔑 TMDB API Setup (Important)

To fetch posters, you **must add your TMDB API key.**

### Add the API key in your code `(app.py)`:
```python
api_key = "YOUR_TMDB_API_KEY"
```
### 📌 Get your free API key here:
<https://www.themoviedb.org/settings/api>

---

# 🛠️ Full Preprocessing Guide 
### ***(If Pickle Files Are Missing)***

> #### If `movies_data.pkl` and `similarity.pkl` are not present, follow this guide.

### Step 1 — Launch Jupyter Notebook
```bash
jupyter notebook
```

### Step 2 — Open and run `preprocess.ipynb`

**The notebook performs:**

- **Loading TMDB dataset**

- **Cleaning genres, keywords, cast, crew**

- **Creating a unified tags column**

- **Vectorizing tags using CountVectorizer**

- **Computing Cosine Similarity**

- **Saving:**

        - movies_data.pkl
        - similarity.pkl

**After running the notebook, ensure both files appear in your project directory.**

---

# 📊 Dataset

This system uses the **TMDB 5000 Movie Dataset**, containing:

- **tmdb_5000_movies.csv** – Movie metadata (genres, overview, keywords)

- **tmdb_5000_credits.csv** – Cast and crew details

---

# 🚧 Future Improvements

#### Here are some features planned / recommended for future versions:

- **🔍 Search bar with autocomplete**

- **⭐ User ratings-based filtering**

- **🧠 Hybrid model (Content + Collaborative Filtering)**

- **🌐 Deploy on Streamlit Cloud / Render**

- **🎥 Add trailer links from TMDB or YouTube**

---

# 🤝 Contributing

## Contributions are welcome!

**1. Fork the repository**

**2. Create a new branch**

**3. Make your changes**

**4. Submit a pull request**

---

# 🔑 API Key & Credits

This project uses the **TMDB API** for poster fetching.

> This project uses the **TMDB API but is not endorsed or certified by TMDB.**

Make sure your system has an **active internet connection** for poster downloads.

---

# ✔️ License

This project is released under the **MIT License.**

---

# ⭐ Final Notes

**If you find this project useful, please consider starring the repository on GitHub!**

**It helps support development and visibility.**


