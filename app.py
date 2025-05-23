import streamlit as st
from pymongo import MongoClient
from bson.objectid import ObjectId

# Connexion à MongoDB local
client = MongoClient("mongodb://localhost:27017/")
db = client["Catalogue_de_produits"]
collection = db["produits"]

st.title("📦 Catalogue de Produits")

# ======================
# Section : Insertion de produit
# ======================
st.header("➕ Ajouter un produit")

with st.form("ajouter_produit"):
    nom = st.text_input("Nom du produit")
    prix = st.number_input("Prix (€)", min_value=0.0, step=0.01)
    stock = st.number_input("Stock disponible", min_value=0)
    categorie = st.text_input("Catégorie")
    submitted = st.form_submit_button("Ajouter")

    if submitted and nom:
        nouveau_produit = {
            "nom": nom,
            "prix": prix,
            "stock": stock,
            "categorie": categorie
        }
        collection.insert_one(nouveau_produit)
        st.success("✅ Produit ajouté avec succès !")
        st.experimental_rerun()

# ======================
# Section : Affichage et filtres
# ======================
st.header("📋 Liste des produits")

# Filtres simples
categorie_filtre = st.text_input("Filtrer par catégorie (optionnel)")
prix_max = st.slider("Prix maximum", 0, 2000, 1000)

# Requête MongoDB
filtre = {
    "prix": {"$lte": prix_max}
}
if categorie_filtre:
    filtre["categorie"] = categorie_filtre

produits = list(collection.find(filtre))

if produits:
    for prod in produits:
        st.markdown(f"""
        **🛒 {prod.get('nom')}**
        - 💶 Prix : {prod.get('prix')} €
        - 📦 Stock : {prod.get('stock')}
        - 🗂️ Catégorie : {prod.get('categorie')}
        """)

# ======================
# Section : Modifier / Supprimer
# ======================
st.header("🛠️ Modifier ou Supprimer un produit")

for prod in produits:
    with st.expander(f"📝 Modifier/Supprimer : {prod['nom']}"):
        col1, col2 = st.columns(2)

        with col1:
            nom_modif = st.text_input("Nom", value=prod["nom"], key=f"nom_{prod['_id']}")
            prix_modif = st.number_input("Prix", value=prod["prix"], key=f"prix_{prod['_id']}")
            stock_modif = st.number_input("Stock", value=prod["stock"], key=f"stock_{prod['_id']}")
            cat_modif = st.text_input("Catégorie", value=prod["categorie"], key=f"cat_{prod['_id']}")

            if st.button("💾 Enregistrer les modifications", key=f"save_{prod['_id']}"):
                collection.update_one(
                    {"_id": prod["_id"]},
                    {"$set": {
                        "nom": nom_modif,
                        "prix": prix_modif,
                        "stock": stock_modif,
                        "categorie": cat_modif
                    }}
                )
                st.success("✅ Produit modifié !")
                st.experimental_rerun()

        with col2:
            if st.button("🗑️ Supprimer ce produit", key=f"delete_{prod['_id']}"):
                collection.delete_one({"_id": prod["_id"]})
                st.warning("❌ Produit supprimé.")
                st.experimental_rerun()

st.header("📋 Liste des produits")

# Filtres simples
categorie_filtre = st.text_input("Filtrer par catégorie (optionnel)")
prix_max = st.slider("Prix maximum", 0, 2000, 1000)

# Requête MongoDB
filtre = {
    "prix": {"$lte": prix_max}
}
if categorie_filtre:
    filtre["categorie"] = categorie_filtre

produits = list(collection.find(filtre))

if produits:
    for prod in produits:
        st.markdown(f"""
        **🛒 {prod.get('nom')}**
        - 💶 Prix : {prod.get('prix')} €
        - 📦 Stock : {prod.get('stock')}
        - 🗂️ Catégorie : {prod.get('categorie')}
        """)

        # === Avis clients (affichés s’ils existent)
        if "avis" in prod and prod["avis"]:
            st.write("🗣️ Avis clients :")
            for a in prod["avis"]:
                st.markdown(f"- ⭐ {a['note']} : *{a['commentaire']}*")
        st.markdown("---")
else:
    st.warning("Aucun produit trouvé.")
