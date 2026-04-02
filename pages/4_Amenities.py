import streamlit as st
import pandas as pd
import plotly.express as px
from utils.components import neon_metric, load_css

load_css("assets/styles.css")   # ✅ FIX — Dark theme applies here

st.title("🧩 Amenities Analysis")

df = pd.read_csv("cleaned_df.csv", index_col=0)

city = st.selectbox("Select City", sorted(df.city.unique()))
df_city = df[df.city == city]

amen_cols = [c for c in df_city.columns if c.startswith("amenity__")]

# Most common amenities
amen_pct = (df_city[amen_cols].sum() / len(df_city) * 100).nlargest(20)
st.plotly_chart(px.bar(amen_pct, title="Top 20 Amenities (%)"), use_container_width=True)

# Amenities influencing price
amen_list = []
for col in amen_cols:
    avg = df_city[df_city[col] == 1]["price_original_$"].mean()
    if not pd.isna(avg):
        amen_list.append([col, avg])

amen_price = pd.DataFrame(amen_list, columns=["Amenity","Avg Price"]).nlargest(20,"Avg Price")
st.plotly_chart(px.scatter(amen_price, x="Amenity", y="Avg Price", size="Avg Price"), use_container_width=True)

# Correlation map
num_corr = df_city.select_dtypes(include="number").corr()
st.plotly_chart(px.imshow(num_corr, text_auto=True, color_continuous_scale="Electric"), use_container_width=True)
