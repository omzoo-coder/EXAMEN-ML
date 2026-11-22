import streamlit as st

st.set_page_config(page_title="Clustering : projets ML", page_icon="📊", layout="wide")

st.title("📊 Clustering : K-means et CAH")
st.markdown(
    """
Cette application regroupe plusieurs projets de **clustering** (K-means et Classification Ascendante Hiérarchique).
Choisissez un projet dans le **menu de gauche**.

| Page | Jeu de données | Modèle déployé |
|---|---|---|
| 1. Customer Segmentation | Clients d'un opérateur télécom | CAH |
| 2. Wheat Seeds | Graines de blé | *à venir* |
| 3. Dataset UCI n°1 | *à venir* | *à venir* |
| 4. Dataset UCI n°2 | *à venir* | *à venir* |
"""
)
