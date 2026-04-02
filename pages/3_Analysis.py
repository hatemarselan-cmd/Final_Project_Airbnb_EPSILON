import streamlit as st
import pandas as pd
import plotly.express as px
from utils.components import neon_metric, load_css

load_css("assets/styles.css")   # ✅ FIX — Dark theme applies here

st.title("📊 Categorical & Numerical Insights")

df = pd.read_csv("cleaned_df.csv", index_col=0)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Units per City",
    "Revenue by City",
    "Neighbourhood Pricing",
    "Room Types",
    "Cancellation Policy"
])

with tab1:
    st.plotly_chart(px.histogram(df, x="city", color="city", text_auto=True), use_container_width=True)

with tab2:
    top5 = df.groupby("city")["price_original_$"].sum().nlargest(5).reset_index()
    st.plotly_chart(px.bar(top5, x="city", y="price_original_$", text_auto=True), use_container_width=True)

with tab3:
    nei = df.groupby(["city","neighbourhood"])["price_original_$"].median()
    top20 = nei.sort_values(ascending=False).head(20).reset_index()
    st.plotly_chart(px.bar(top20, x="neighbourhood", y="price_original_$", color="city"), use_container_width=True)

with tab4:
    rt = df.groupby(["city","room_type"])["price_original_$"].mean().reset_index()
    st.plotly_chart(px.bar(rt, x="city", y="price_original_$", color="room_type", barmode="group"), use_container_width=True)

with tab5:
    cp = df.groupby(["city","cancellation_policy"])["price_original_$"].mean().reset_index()
    st.plotly_chart(px.bar(cp, x="city", y="price_original_$", color="cancellation_policy", barmode="group"), use_container_width=True)
