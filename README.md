# 🏢 Greek Real Estate Data Analysis

A Python data analysis project analyzing property listings in Greece using data from Kaggle. The script cleans raw property data, compares pricing metrics across cities and property ages, and detects market anomalies (deals & overpriced listings) using **Z-Scores**.

## 🚀 Features
- **Automated Data Retrieval**: Downloads dataset via `kagglehub`.
- **Data Cleaning**: Filters out erroneous entries and extreme outliers.
- **Exploratory Data Analysis**:
  - Identifies the cheapest cities based on average price per m².
  - Compares average m² prices between old (<2006) and new (>=2006) properties.
- **Deal & Overpriced Detection**: Uses **Z-Score grouping by city** to highlight properties selling significantly below or above regional market averages.

## 🛠️ Tech Stack
- **Python 3.x**
- **Pandas**
- **Kagglehub**

## 🏃 How to Run
1. Clone the repository:
   ```bash
   git clone <YOUR-GITHUB-REPO-LINK>
   cd Real-Estate-Project