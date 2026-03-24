import gdown
import os

# 1️⃣ cleaned_df_for_ML.csv
if not os.path.exists("cleaned_df_for_ML.csv"):
    url_ml = "https://drive.google.com/uc?id=12eC3ySmp2G-Sce47wVTZH4ZoNLy3XstU"
    print("Downloading cleaned_df_for_ML.csv...")
    gdown.download(url_ml, "cleaned_df_for_ML.csv", quiet=False)

print("✅ All files are ready!")
