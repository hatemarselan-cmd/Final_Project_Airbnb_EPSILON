import streamlit as st

# ✅ Load global CSS (for dark neon theme)
def load_css(path: str):
    with open(path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ Neon blue metric card
def neon_metric(label, value):
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)

# ✅ Neon blue info card
def neon_card(title, content):
    st.markdown(f"""
    <div class="neon-card">
        <h3 style='color:#00E6FF;'>{title}</h3>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)

