import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Account Manager Pro", layout="wide", page_icon="📈")

# --- STYLE PERSONNALISÉ (CORRIGÉ) ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { 
        width: 100%; 
        border-radius: 5px; 
        height: 3em; 
        background-color: #007bff; 
        color: white; 
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Strategic Account Scorer & Tracker")
st.markdown("Identifiez vos comptes clés et préparez vos points hebdomadaires avec précision.")

# --- BARRE LATÉRALE (SIDEBAR) ---
with st.sidebar:
    st.header("⚙️ Actions")
    if st.button("➕ Nouveau Compte / Reset"):
        st.rerun()
    st.divider()
    st.info("Le score est basé sur le Potentiel Business, l'Accessibilité et le Fit Technologique.")

# --- SECTION 1 : IDENTITÉ ET SCORING ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🏢 Identité du Compte")
    nom_compte = st.text_input("Nom de l'entreprise", placeholder="ex: L'Oréal")
    secteur = st.selectbox("Secteur", ["Banque/Assurance", "Industrie", "Luxe/Retail", "Public", "Énergie", "Autre"])
    champion = st.text_input("Interlocuteur Clé (Champion)", placeholder="Prénom Nom - Poste")
    statut = st.select_slider("Avancement", options=["Prospection", "Approche", "RDV pris", "Discovery", "Proposition", "Closing"])

with col2:
    st.subheader("📊 Scoring Stratégique (1 à 5)")
    potentiel = st.slider("Potentiel Business (Volume de besoins)", 1, 5, 3)
    accessibilite = st.slider("Accessibilité (Réseau / Facilité d'entrée)", 1, 5,
