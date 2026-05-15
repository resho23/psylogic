# app.py
import streamlit as st
from ai_functions import erstelle_gutachten, analysiere_gutachten

st.set_page_config(page_title="Psychotherapeutisches Gutachten Tool", page_icon="📝")
st.title("Psychotherapeutisches Gutachten Tool")
st.write("Gib dein Roh-Diktat ein, das Tool erstellt ein strukturiertes Gutachten und analysiert es.")

roht_text = st.text_area("Roh-Diktat eingeben:", height=250)

if st.button("Gutachten erstellen"):
    if not roht_text.strip():
        st.warning("Bitte zuerst den Rohtext eingeben!")
    else:
        gutachten = erstelle_gutachten(roht_text)
        st.subheader("Strukturiertes Gutachten")
        st.text_area("Gutachten", value=gutachten, height=400)

        analyse = analysiere_gutachten(gutachten)
        st.subheader("Analyse & Hinweise")
        st.write("Konkrete Schwächen:")
        for s in analyse["schwaechen"]:
            st.write(f"- {s}")
        st.write("Verbesserungsvorschläge:")
        for v in analyse["verbesserungsvorschlaege"]:
            st.write(f"- {v}")
