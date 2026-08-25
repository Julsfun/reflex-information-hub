import streamlit as st

st.set_page_config(
    page_title="Ask Reflex",
    page_icon="🔎",
    layout="wide"
)

st.title("Ask Reflex")

st.write(
    "Finden Sie schnell die richtigen Informationen für Ihr Projekt."
)

frage = st.text_area(
    "Was möchten Sie erreichen?",
    placeholder=(
        "Ich plane ein Bürogebäude und benötige "
        "eine Lösung für die Druckhaltung."
    )
)

if st.button("Projekt analysieren"):

    st.subheader("Erkannter Projektkontext")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rolle", "TGA-Planer")

    with col2:
        st.metric("Gebäude", "Büro")

    with col3:
        st.metric("Anwendung", "Druckhaltung")

    st.subheader("Empfohlene Reflex-Inhalte")

    st.success("Reflex Druckhaltungslösung")

    st.write("📄 Technisches Datenblatt")
    st.write("🏗️ BIM-Modell")
    st.write("📝 Ausschreibungstext")
    st.write("🧮 Berechnung starten")
