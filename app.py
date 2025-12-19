import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Account Manager Pro", layout="wide", page_icon="📈")

# --- STYLE PERSONNALISÉ ---
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
st.markdown("Identifiez vos comptes clés et préparez vos points hebdomadaires.")

# --- BARRE LATÉRALE ---
with st.sidebar:
    st.header("⚙️ Actions")
    if st.button("➕ Nouveau Compte / Reset"):
        st.rerun()
    st.divider()
    st.info("Le score est basé sur le Potentiel, l'Accessibilité et le Fit.")

# --- SECTION 1 : IDENTITÉ ET SCORING ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🏢 Identité du Compte")
    nom_compte = st.text_input("Nom de l'entreprise", placeholder="ex: L'Oréal")
    secteur = st.selectbox("Secteur", ["Banque/Assurance", "Industrie", "Luxe/Retail", "Public", "Énergie", "Autre"])
    champion = st.text_input("Interlocuteur Clé", placeholder="Prénom Nom - Poste")
    statut = st.select_slider("Avancement", options=["Prospection", "Approche", "RDV pris", "Discovery", "Proposition", "Closing"])

with col2:
    st.subheader("📊 Scoring Stratégique (1 à 5)")
    potentiel = st.slider("Potentiel Business", 1, 5, 3)
    accessibilite = st.slider("Accessibilité réseau", 1, 5, 2)
    fit_techno = st.slider("Fit avec notre Expertise", 1, 5, 4)
    
    # Calcul du score
    score_final = (potentiel + accessibilite + fit_techno) * 6.67
    
    if score_final >= 75:
        st.success(f"Score : {int(score_final)}/100 - Priorité : TIER 1 🔥")
    elif score_final >= 45:
        st.warning(f"Score : {int(score_final)}/100 - Priorité : TIER 2 ⚡")
    else:
        st.error(f"Score : {int(score_final)}/100 - Priorité : TIER 3 💤")

# --- SECTION 2 : PROSPECTION ET ACTIONS ---
st.divider()
col3, col4 = st.columns(2)

with col3:
    st.subheader("🎯 Stratégie & Accroche")
    hook = st.text_area("L'angle d'attaque", placeholder="Pourquoi les contacter maintenant ?")
    concurrence = st.text_input("Concurrents en place", placeholder="ex: Alten, Akkodis...")

with col4:
    st.subheader("📋 Suivi d'Activité")
    faits = st.text_area("✅ ACCOMPLI (Cette semaine)", placeholder="- Actions terminées")
    a_faire = st.text_area("⏳ À FAIRE (Semaine prochaine)", placeholder="- Prochaines étapes")

# --- SECTION 3 : GÉNÉRATION DU RAPPORT ---
st.divider()
if st.button("📄 GÉNÉRER LE MÉMO POUR MA MANAGER"):
    if not nom_compte:
        st.error("Veuillez entrer le nom d'un compte.")
    else:
        tier = "TIER 1 🔥" if score_final >= 75 else "TIER 2 ⚡" if score_final >= 45 else "TIER 3 💤"
        
        report = f"""📝 MÉMO HEBDO - {nom_compte.upper()}
--------------------------------------------------
⭐ PRIORITÉ : {tier} (Score: {int(score_final)}/100)
📍 STATUT : {statut}
👤 CHAMPION : {champion}

✅ ACTIONS RÉALISÉES :
{faits if faits else "N/A"}

🚀 PROCHAINES ÉTAPES :
{a_faire if a_faire else "N/A"}

💡 STRATÉGIE :
{hook}
--------------------------------------------------
🛠 CONCURRENCE : {concurrence}
"""
        st.subheader("Rapport à copier :")
        st.code(report, language="text")
        st.balloons()
