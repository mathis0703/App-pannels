import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Solar Decision Engine",
    page_icon="☀️",
    layout="wide"
)

# --------------------------------------------------
# STYLE GLOBAL
# --------------------------------------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #EAF4F4;
}

/* NAVIGATION */
div[role="radiogroup"] {
    background-color: white;
    padding: 10px;
    border-radius: 16px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.06);
    margin-bottom: 35px;
    display: flex;
    justify-content: center;
    gap: 20px;
}

div[role="radiogroup"] label {
    padding: 10px 20px;
    border-radius: 12px;
    font-weight: 600;
    cursor: pointer;
}

/* TEXT NAVIGATION */
div[role="radiogroup"] label div {
    color: #111827 !important;
}

/* ONGLET ACTIF (FIX) */
div[role="radiogroup"] input:checked + div {
    background-color: #D8E2DC;  /* <-- clair au lieu de noir */
    border-radius: 12px;
}

/* TEXTE ONGLET ACTIF (FIX) */
div[role="radiogroup"] input:checked + div div {
    color: #111827 !important;
}

/* HERO SECTION */
.hero {
    padding: 70px 50px;
    border-radius: 28px;
    background: linear-gradient(135deg, #CED4DA, #E9ECEF);
    text-align: center;
    margin-bottom: 40px;
}

.main-title {
    font-size: 52px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 22px;
}

.main-subtitle {
    font-size: 19px;
    color: #111827;
    max-width: 850px;
    margin: auto;
    line-height: 1.7;
}

/* INPUT PREVIEW BOX */
.input-preview {
    padding: 32px;
    border-radius: 22px;
    background-color: white;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.06);
    margin-top: 30px;
}

.input-preview h3 {
    color: #111827;
    margin-bottom: 10px;
}

.input-preview p {
    color: #111827;
    font-size: 16px;
}

/* HOME CARDS */
.card {
    padding: 28px;
    border-radius: 22px;
    background-color: white;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.07);
    margin-bottom: 25px;
}

.card h3 {
    color: #111827;
}

.card p {
    color: #374151;
    font-size: 16px;
}

/* TEXT GLOBAL */
h1, h2, h3, h4, h5, h6, p, span, label {
    color: #111827 !important;
}

/* FIX METRICS */
[data-testid="stMetricValue"] {
    color: #111827 !important;
}

[data-testid="stMetricLabel"] {
    color: #4b5563 !important;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# NAVIGATION 
# --------------------------------------------------
page = st.radio(
    label="Navigation",
    options=["Home", "Financial Results", "Graphs & Recommendation"],
    horizontal=True,
    label_visibility="collapsed"
)

# --------------------------------------------------
# PAGE 1: HOME
# --------------------------------------------------
if page == "Home":

    st.markdown("""
    <div class="hero">
        <div class="main-title">Should you invest in solar panels?</div>
        <div class="main-subtitle">
            This application helps users make informed decisions about installing solar panels.
            By entering their personal and housing characteristics, the app will later estimate
            solar energy production, evaluate financial profitability, and compare potential gains
            with or without battery storage.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>Solar Production</h3>
            <p>This section will later display estimated solar production.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>Profitability</h3>
            <p>This section will later show costs, savings and return on investment.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>Battery Analysis</h3>
            <p>This section will later compare results with and without battery.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-preview">
        <h3>User information</h3>
        <p>
            This section will contain the user inputs such as location, roof size, energy consumption,
            electricity price, available budget, and battery preferences.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# PAGE 2: FINANCIAL RESULTS
# --------------------------------------------------
elif page == "Financial Results":

    st.title("Financial Results")
    st.write("Here, financial results will be displayed.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total installation cost", "—")

    with col2:
        st.metric("Yearly savings", "—")

    with col3:
        st.metric("Payback period", "—")

# --------------------------------------------------
# PAGE 3: GRAPHS & RECOMMENDATION
# --------------------------------------------------
elif page == "Graphs & Recommendation":

    st.title("Graphs and Final Recommendation")
    st.write("Graphs and final recommendation will appear here.")

    st.metric("Annual production", "—")
    st.metric("Energy coverage", "—")
    st.metric("Self-consumption rate", "—")