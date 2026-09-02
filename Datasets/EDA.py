import pandas as pd
import numpy as np

# ==================================================
# LOAD DATASETS
# ==================================================

india_env = pd.read_excel("india_cities_dataset_2021_2025.xlsx")
weather = pd.read_excel("india_2000_2024_daily_weather.xlsx")
disease = pd.read_excel("Disease_Incidence_Rate.xlsx")
uhi = pd.read_excel("urban_heat_island_dataset.xlsx")
micro = pd.read_excel("Microclimate_dataset.xlsx")

# ==================================================
# STANDARDIZE COLUMN NAMES
# ==================================================

for df in [india_env, weather, disease, uhi, micro]:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

# ==================================================
# REMOVE DUPLICATES
# ==================================================

india_env = india_env.drop_duplicates()
weather = weather.drop_duplicates()
disease = disease.drop_duplicates()
uhi = uhi.drop_duplicates()
micro = micro.drop_duplicates()

# ==================================================
# HANDLE MISSING VALUES
# ==================================================

def fill_missing(df):
    num_cols = df.select_dtypes(include=np.number).columns

    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())

    return df

india_env = fill_missing(india_env)
weather = fill_missing(weather)
disease = fill_missing(disease)
uhi = fill_missing(uhi)
micro = fill_missing(micro)

# ==================================================
# CHECK COMMON KEYS
# ==================================================

print("Environmental Columns")
print(india_env.columns)

print("Weather Columns")
print(weather.columns)

# ==================================================
# MERGE DATASETS
# ==================================================

# MODIFY THESE BASED ON ACTUAL COLUMN NAMES

final_df = india_env.copy()

# Merge weather
if {'city','year','month'}.issubset(weather.columns):
    final_df = final_df.merge(
        weather,
        on=['city','year','month'],
        how='left'
    )

# Merge disease
if {'city'}.issubset(disease.columns):
    final_df = final_df.merge(
        disease,
        on='city',
        how='left'
    )

# Merge UHI
if {'city'}.issubset(uhi.columns):
    final_df = final_df.merge(
        uhi,
        on='city',
        how='left'
    )

# Merge Microclimate
if {'city'}.issubset(micro.columns):
    final_df = final_df.merge(
        micro,
        on='city',
        how='left'
    )

# ==================================================
# FEATURE ENGINEERING
# ==================================================

# Vegetation vs Built-up ratio

if {'ndvi','ndbi'}.issubset(final_df.columns):
    final_df['green_urban_ratio'] = (
        final_df['ndvi'] /
        (final_df['ndbi'] + 0.001)
    )

# Heat Index

if {'temperature','humidity'}.issubset(final_df.columns):
    final_df['heat_index'] = (
        final_df['temperature']
        +
        0.1 * final_df['humidity']
    )

# Cooling Potential

if {'ndvi','wind_speed'}.issubset(final_df.columns):
    final_df['cooling_potential'] = (
        final_df['ndvi']
        *
        final_df['wind_speed']
    )

# ==================================================
# REMOVE EXTREME OUTLIERS
# ==================================================

numeric_cols = final_df.select_dtypes(
    include=np.number
).columns

for col in numeric_cols:

    q1 = final_df[col].quantile(0.25)
    q3 = final_df[col].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    final_df = final_df[
        (final_df[col] >= lower)
        &
        (final_df[col] <= upper)
    ]

# ==================================================
# FINAL CHECK
# ==================================================

print("\nShape:", final_df.shape)

print("\nMissing Values")
print(final_df.isnull().sum())

# ==================================================
# SAVE FINAL DATASET
# ==================================================

final_df.to_csv(
    "final_urban_heat_dataset.csv",
    index=False
)

print(
    "\nSaved Successfully: final_urban_heat_dataset.csv"
)