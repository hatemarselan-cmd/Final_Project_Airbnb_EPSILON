import gdown
import os

# 1️⃣ cleaned_df_for_ML.csv
if not os.path.exists("cleaned_df_for_ML.csv"):
    url_ml = "https://drive.google.com/uc?id=12eC3ySmp2G-Sce47wVTZH4ZoNLy3XstU"
    print("Downloading cleaned_df_for_ML.csv...")
    gdown.download(url_ml, "cleaned_df_for_ML.csv", quiet=False)

# 2️⃣ cleaned_df.csv
if not os.path.exists("cleaned_df.csv"):
    url_cleaned = "https://drive.google.com/uc?id=1_vNuJFk75sp1tBx7I4a4fZu_t8dJJWK3"
    print("Downloading cleaned_df.csv...")
    gdown.download(url_cleaned, "cleaned_df.csv", quiet=False)

print("✅ All files are ready!")
