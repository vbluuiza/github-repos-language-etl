## 📊 GitHub Repos Language ETL

**An ETL pipeline to collect, process, and analyze programming languages used in public repositories from major tech companies on GitHub.**

---

### 🚀 What this project does

This project automates the extraction and processing of GitHub repositories for companies such as **Amazon**, **Netflix**, and **Spotify**, generating a clean dataset of repository names and their primary programming languages.

---

### 🧱 Project Structure

```

.
├── data/
│   ├── raw/                  # Raw API data (JSON)
│   └── processed/            # Final CSV files
├── notebooks/                
├── src/
│   ├── scripts/
│   │   └── repos_data.py     # Core class for data extraction
│   ├── extract.py            # Executes data extraction for each company
│   ├── load.py               # Combines and saves final dataset
    ├── transform_&_load.ipynb # Notebook for cleaning, merging and exporting language data
│   └── __init__.py
├── .env                      # API token (not tracked)
├── .gitignore
├── requirements.txt
└── README.md

```

---

### ⚙️ Features

- 🔐 Loads GitHub API token from `.env`
- 🌐 Extracts public repositories for multiple organizations
- 🧼 Cleans and structures repository name & language
- 📁 Saves per-company CSVs and a combined dataset
- 📦 Modular code with `extract`, `transform`, `load` steps

---

### 📦 Technologies Used

- `Python 3.10+`
- `Pandas`
- `Requests`
- `dotenv`

---

### 📁 Example Output

**`data/processed/all_companies_languages.csv`**

| repository_name | language | source |
| --- | --- | --- |
| firetv-app | Java | amazon |
| api-gateway | Go | netflix |
| wrapped-2022 | TypeScript | spotify |

---

> 💡 This project was developed and tested using WSL2 (Ubuntu 22.04) on Windows.

---

### 🔧 Setup Instructions

```bash

# Clone the repository
git clone https://github.com/your-username/github-repos-language-etl
cd github-repos-language-etl

# Create a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file with your GitHub API token
echo "ACCESS_TOKEN=your_github_token_here" > .env

# Run extraction and loading
python -m src.extract
python -m src.load
```

---

### 📈 Next Steps

- Add more companies (Meta, Google, Microsoft…)
- Visualize the language distribution
- Export to a database or dashboard

---

### 👩‍💻 Developed by

Luiza Vieira – Systems Analysis and Development student - Cesar School

  - 💼 [LinkedIn](https://www.linkedin.com/in/vbluuiza)
  - 💻 [GitHub](https://github.com/vbluuiza)
