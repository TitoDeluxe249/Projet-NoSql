import streamlit as st
from db import collection

st.title("📊 Tableau de bord des Produits")
produits = list(collection.find())

for prod in produits:
    st.write(f"**{prod['nom']}** - {prod['prix']} € - Stock : {prod['stock']}")

    if "avis" in prod:
        st.write("Avis :")
        for avis in prod["avis"]:
            st.write(f"- ⭐ {avis['note']}: {avis['commentaire']}")