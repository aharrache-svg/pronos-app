import streamlit as st

# Configuration de l'affichage mobile
st.set_page_config(page_title="PronosAlgo", page_icon="⚽", layout="centered")

st.title("⚽ PronosAlgo")
st.caption("Pronostics du jour & Indice de confiance")

# Bouton de rafraîchissement
if st.button("🔄 Actualiser les matchs"):
    st.cache_data.clear()

# Données des matchs du jour
matchs = [
    {
        "championnat": "Ligue 1",
        "heure": "20:45",
        "equipes": "PSG vs Marseille",
        "prono": "Victoire PSG",
        "cote": 1.45,
        "confiance": 88
    },
    {
        "championnat": "La Liga",
        "heure": "21:00",
        "equipes": "Real Madrid vs Barcelone",
        "prono": "Plus de 2.5 Buts",
        "cote": 1.60,
        "confiance": 82
    },
    {
        "championnat": "Premier League",
        "heure": "18:30",
        "equipes": "Arsenal vs Chelsea",
        "prono": "Arsenal ou Nul",
        "cote": 1.35,
        "confiance": 91
    },
    {
        "championnat": "Serie A",
        "heure": "19:00",
        "equipes": "Inter Milan vs Juventus",
        "prono": "Les 2 équipes marquent",
        "cote": 1.75,
        "confiance": 68
    }
]

st.divider()

# Affichage sous forme de cartes simples
for match in matchs:
    # Couleur du voyant selon la confiance
    if match["confiance"] >= 80:
        badge = "🟢 Très élevé"
    elif match["confiance"] >= 65:
        badge = "🟡 Moyen"
    else:
        badge = "🔴 Risqué"

    with st.container():
        st.subheader(f"{match['equipes']}")
        st.caption(f"🏆 {match['championnat']} • 🕒 {match['heure']}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"💡 **Prono :**\n{match['prono']}")
        with col2:
            st.success(f"📊 **Cote :**\n{match['cote']}")
            
        st.write(f"**Indice de confiance :** {match['confiance']}% ({badge})")
        st.progress(match["confiance"] / 100)
        st.divider()
