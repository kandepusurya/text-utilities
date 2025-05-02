# Florida-19 Election Modelling

This project focuses on modeling and predicting election outcomes for Florida's 19th Congressional District (FL-19) using historical and demographic data. It employs machine learning techniques to analyze voter behavior, predict voter turnout, and forecast election winners.

---

## Features
- Comprehensive exploratory data analysis (EDA) of election trends.
- Spatial analysis using geospatial data to understand geographic voting patterns.
- Machine learning models (classification and regression) to predict voter turnout and election outcomes.
- Detailed analysis of congressional and presidential election trends.

---

## Repository Structure
The repository is organized as follows:

```
.
├── FDE/                 # Processed data for elections
│   ├── Presidential/    # Presidential election data
│   ├── Primary/         # Primary election data
│   ├── General/         # General election data
├── Shapes/              # Geospatial data for boundaries
├── 1976-2020-president.csv  # Nationwide presidential election data
├── Voter Turnout.ods    # Spreadsheet for voter turnout
├── fl-19_district.csv   # District-level data for FL-19
├── osna.ipynb           # Jupyter Notebook for analysis and modeling
├── requirements.txt     # Python dependencies
└── README.md            # Project description and replication guide
```

---

## Data Sources
The following data sources were used:
- [Florida Division of Elections](https://dos.myflorida.com/elections/)
- [MIT Election Data and Science Lab](https://electionlab.mit.edu/)
- [Kaggle](https://www.kaggle.com/)
- [US Census Bureau](https://www.census.gov/)
- [Ballotpedia - FL-19 Congressional District](https://ballotpedia.org/Florida%27s_19th_Congressional_District)

---

## Installation and Setup
NOTE: this project uses conda fro pacake managing.
Follow these steps to replicate the work:

### 1. Clone the Repository
```bash
git clone https://github.com/Narsimha96/CS579-Project.git
cd CS579-Project
```

### 2. Install Dependencies
Ensure Python is installed on your machine. Install the required packages:
```bash
conda install -r requirements.txt
```

### 3. Download Necessary Data
The required datasets are already included in the repository. If additional data is needed, refer to the [Data Sources](#data-sources) section.

---

## How to Run
1. Open the `osna.ipynb` file in Jupyter Notebook or a similar environment.
   ```bash
   jupyter notebook osna.ipynb
   ```
2. Follow the steps in the notebook to:
   - Load and preprocess data.
   - Perform exploratory data analysis (EDA).
   - Train machine learning models for classification and regression.
   - Visualize results.

---

## Key Outputs
- **Visualizations**: Trends in voter turnout, party performance, and spatial patterns.
- **Model Predictions**: Forecasted voter turnout and winning parties for upcoming elections.
- **Insights**: Understanding the influence of demographic and socioeconomic factors on voting behavior.

---

## Future Work
- Integrating real-time election data.
- Advanced geospatial and temporal analysis.
- Exploring additional predictors like campaign financing and media influence.
