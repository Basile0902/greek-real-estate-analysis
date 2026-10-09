import kagglehub
import os
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("logiover/xe-gr-properties-data")

print("Path to dataset files:", path)

# --- LOAD DATA ---

# Locatiing the JSON File in the downloaded folder
files=os.listdir(path)
json_files=[f for f in files if f.endswith(".json")]

if json_files:

    json_file_path=os.path.join(path,json_files[0])
    df=pd.read_json(json_file_path)

    print("----First 5 records----")
    print(df.head())

    print("Information about the columns")
    print(df.info())

else:
    print("Didn't find json file in the folder")

# --- DATA CLEANING ---

df_clean=df.query("pricePerSqm > 100 and pricePerSqm < 15000 and sqMeters > 10").copy()

# --- ANALYSIS ---

# 1.Cheapest cities
MostCheapCities=(
    df_clean.groupby("city")["pricePerSqm"].mean().sort_values()
)

print("Most cheap cities:")
print(MostCheapCities)

# 2.Old vs New

OldBuildPrice=df_clean.query("yearBuilt < 2006")["pricePerSqm"].mean()

NewBuildPrice=df_clean.query("yearBuilt >= 2006")["pricePerSqm"].mean()

print(f"Average price of old buildings: {OldBuildPrice:.2f}€/m²")
print(f"Average price of new buildings: {NewBuildPrice:.2f}€/m²")

# 3.Opportunities and Overpriced finders

df_clean["cityMeanPrice"]=df_clean.groupby("city")["pricePerSqm"].transform("mean")

df_clean["cityStdPrice"]=df_clean.groupby("city")["pricePerSqm"].transform("std")

df_clean["zScore"]=(df_clean["pricePerSqm"] - df_clean["cityMeanPrice"]) / df_clean["cityStdPrice"]

opportunities=(
    df_clean.query("zScore < -2.0")
[["title","city","price","sqMeters","pricePerSqm","zScore"]].sort_values("zScore")
)

overpriced=(
        df_clean.query("zScore > 1.5")
        [["title","city","price","sqMeters","pricePerSqm","zScore"]].sort_values("zScore",ascending=False)
)

print("---Potential Opportunities---")
print(opportunities.head(5))

print("---Overpriced Properties---")
print(overpriced.head(5))







