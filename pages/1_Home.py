import streamlit as st
import pandas as pd
from utils.components import neon_card
from utils.components import neon_metric, load_css

load_css("assets/styles.css")   # ✅ FIX — Dark theme applies here

st.title("🏠 Home — Dataset Overview")

df = pd.read_csv("cleaned_df.csv", index_col=0)

st.markdown("### ✅ Dataset Preview")
st.dataframe(df.head(12), use_container_width=True)

with st.expander("📘 Column Descriptions"):
    col_desc = {
        "id": "Unique listing identifier.",
        "log_price": "Log-transformed nightly price.",
        "property_type": "Type of property.",
        "room_type": "Type of room.",
        "amenities": "List of amenities.",
        "accommodates": "Max number of guests.",
        "bathrooms": "Number of bathrooms.",
        "bed_type": "Type of provided bed.",
        "cancellation_policy": "Booking cancellation policy.",
        "cleaning_fee": "Cleaning fee yes/no.",
        "city": "City of listing.",
        "latitude": "Longitude & latitude.",
        "longitude": "Coordinates.",
        "number_of_reviews": "Total reviews.",
        "review_scores_rating": "Rating by guests.",
        "bedrooms": "Bedrooms count.",
        "beds": "Number of beds."
    }
    st.table(pd.DataFrame(list(col_desc.items()), columns=["Column","Description"]))

neon_card("Welcome!", 
"""
This neon dashboard lets you explore Airbnb USA listings with  
interactive maps, analytics, and ML-driven price prediction.
""")
