import streamlit as st
import pandas as pd
import plotly.express as px
from utils.components import neon_metric, load_css

# ✅ Load CSS theme
load_css("assets/styles.css")

st.title("🌍 Airbnb Listings Map")

df = pd.read_csv("cleaned_df.csv", index_col=0)

# ✅ City Filter
cities = sorted(df["city"].unique())
selected_city = st.selectbox("Select City", cities)

df_city = df[df["city"] == selected_city]

# ✅ Neighbourhood Filter
neighbourhoods = sorted(df_city["neighbourhood"].unique())
selected_neighbourhoods = st.multiselect(
    "Select Neighbourhood(s)",
    neighbourhoods,
    default=neighbourhoods
)

df_city_nei = df_city[df_city["neighbourhood"].isin(selected_neighbourhoods)]

# ✅ MAP
if len(df_city_nei) == 0:
    st.warning("No listings found for this selection.")
else:
    fig = px.scatter_mapbox(
        df_city_nei,
        lat="latitude",
        lon="longitude",
        color="price_original_$",
        size="price_original_$",
        zoom=10,
        mapbox_style="open-street-map",
        height=650,
        title=f"Airbnb Listings in {selected_city}",
        color_continuous_scale="Electric"
    )
    st.plotly_chart(fig, use_container_width=True)

# ✅ KPIs
total_accommodations = len(df_city_nei)
total_revenue = df_city_nei["price_original_$"].sum()
avg_price = df_city_nei["price_original_$"].mean()

col1, col2, col3 = st.columns(3)
neon_metric("🏘 Total Units", f"{total_accommodations:,}")
neon_metric("💰 Total Revenue", f"${total_revenue:,.2f}")
neon_metric("📊 Avg Price per Unit", f"${avg_price:,.2f}")

# ✅ UNDER / OVER PRICED ANALYSIS
p20 = df_city_nei["price_original_$"].quantile(0.20)
p80 = df_city_nei["price_original_$"].quantile(0.80)

under_df = df_city_nei[df_city_nei["price_original_$"] < p20]
over_df = df_city_nei[df_city_nei["price_original_$"] > p80]

if st.checkbox("Price Over / Under Priced Analysis"):
    st.subheader("📊 Price Over / Under Priced Units")

    col4, col5, col6, col7 = st.columns(4)

    neon_metric("⬇ Under‑Priced Units", f"{len(under_df):,}")
    neon_metric("💵 Avg Under Price", f"${under_df['price_original_$'].mean():,.2f}")

    neon_metric("⬆ Over‑Priced Units", f"{len(over_df):,}")
    neon_metric("💰 Avg Over Price", f"${over_df['price_original_$'].mean():,.2f}")
