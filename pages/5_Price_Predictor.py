import streamlit as st
import pandas as pd
import numpy as np
import joblib
from utils.components import neon_metric, load_css
from my_module import CustomTransformer, my_preprocessing


load_css("assets/styles.css")   # ✅ FIX — Dark theme applies here

st.title("💰 Airbnb Price Predictor (ML Model)")

df = pd.read_csv("cleaned_df_for_ML.csv", index_col=0)
model = joblib.load("xgb_pipeline_final.pkl")

left, right = st.columns(2)

with left:
    property_type = st.selectbox("Property Type", df.property_type.unique())
    room_type = st.selectbox("Room Type", df.room_type.unique())
    bed_type = st.selectbox("Bed Type", df.bed_type.unique())
    city = st.selectbox("City", df.city.unique())
    cancellation_policy = st.selectbox("Cancellation Policy", df.cancellation_policy.unique())

with right:
    accommodates = st.slider("Accommodates", 1, 16)
    bathrooms = st.slider("Bathrooms", 1, 10)
    bedrooms = st.slider("Bedrooms", 0, 10)
    beds = st.slider("Beds", 1, 20)
    number_of_reviews = st.slider("Number of Reviews", 0, 500)
    review_scores_rating = st.slider("Review Scores Rating", 0.0, 100.0)
    amenities_count = st.slider("Amenities Count", 0, 50)
    host_experience_years = st.slider("Host Experience (Years)", 0.0, 20.0)

colA, colB, colC, colD = st.columns(4)
cleaning_fee = colA.selectbox("Cleaning Fee", [0,1])
host_has_profile_pic = colB.selectbox("Host Has Profile Pic", [0,1])
host_identity_verified = colC.selectbox("Identity Verified", [0,1])
instant_bookable = colD.selectbox("Instant Bookable", [0,1])

latitude = st.number_input("Latitude", value=float(df.latitude.mean()))
longitude = st.number_input("Longitude", value=float(df.longitude.mean()))
host_response_rate = st.slider("Host Response Rate", 0.0, 1.0, 0.80)

input_df = pd.DataFrame([locals()], columns=[
    "property_type", "room_type", "accommodates", "bathrooms", "bed_type",
    "cancellation_policy", "cleaning_fee", "city", "host_has_profile_pic",
    "host_identity_verified", "host_response_rate", "instant_bookable",
    "latitude", "longitude", "number_of_reviews", "review_scores_rating",
    "bedrooms", "beds", "amenities_count", "host_experience_years"
])

if st.button("🔮 Predict Price"):
    with st.spinner("Calculating price..."):
        log_price = model.predict(input_df)[0]
        price = round(np.exp(log_price), 2)
        st.success(f"✅ Estimated Price: **${price:,.2f}** per night")
