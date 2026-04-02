import streamlit as st
from utils.components import load_css

st.set_page_config(
    page_title="Airbnb USA Dashboard",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS theme
load_css("assets/styles.css")

# Sidebar Branding
st.sidebar.markdown("""
<div class="sidebar-title">
    <span class="glow-text">🏡 Airbnb Analytics</span>
    <hr class="sidebar-divider">
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### 🔍 Navigation<br>Use the sidebar to switch between pages.", unsafe_allow_html=True)

st.markdown("""
<h1 class="main-title">Airbnb USA Analytics Dashboard</h1>
<p class="subtitle">A futuristic neon dashboard for exploring Airbnb prices and analytics</p>
""", unsafe_allow_html=True)
