import streamlit as st

st.set_page_config(
    page_title="Ask Reflex",
    page_icon="🔎",
    layout="wide"
)

st.title("Ask Reflex")
st.write("Finden Sie schnell die richtigen Informationen für Ihr Projekt.")

frage = st.text_area(
    "Was möchten Sie erreichen?",
    placeholder="Ich plane ein Bürogebäude und benötige eine Lösung für die Druckhaltung."
)

if st.button("Projekt analysieren"):

    text = frage.lower()

    rolle = "Unbekannt"
    gebaeude = "Nicht erkannt"
    anwendung = "Allgemeine Anfrage"
    projektphase = "Nicht erkannt"

    if "plane" in text or "planer" in text or "planung" in text:
        rolle = "TGA-Planer"

    if "büro" in text or "office" in text:
        gebaeude = "Bürogebäude"
    elif "hotel" in text:
        gebaeude = "Hotel"
    elif "industrie" in text:
        gebaeude = "Industriegebäude"

    if "druckhaltung" in text:
        anwendung = "Druckhaltung"
    elif "bim" in text:
        anwendung = "BIM / Planungsdaten"
    elif "installation" in text:
        anwendung = "Installation"

    if "planung" in text or "plane" in text:
        projektphase = "Planung"
    elif "installation" in text:
        projektphase = "Ausführung"

    st.subheader("Erkannter Projektkontext")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Rolle", rolle)

    with col2:
        st.metric("Gebäude", gebaeude)

    with col3:
        st.metric("Anwendung", anwendung)

    with col4:
        st.metric("Projektphase", projektphase)

    st.subheader("Empfohlene Reflex-Inhalte")

    if anwendung == "Druckhaltung":
        st.success("Passende Reflex-Lösung für Druckhaltung")
        st.write("📄 Technisches Datenblatt")
        st.write("🏗️ BIM-Modell")
        st.write("📝 Ausschreibungstext")
        st.write("🧮 Berechnung starten")

    elif anwendung == "BIM / Planungsdaten":
        st.success("BIM@Reflex")
        st.write("🏗️ BIM-Modell")
        st.write("📐 CAD-Daten")
        st.write("📄 Technische Produktdaten")

    elif anwendung == "Installation":
        st.success("Installations- und Serviceinformationen")
        st.write("🔧 Montageanleitung")
        st.write("📄 Inbetriebnahmehinweise")
        st.write("🛠️ Troubleshooting")

    else:
        st.info("Bitte beschreiben Sie Ihr Projekt noch etwas genauer.")

    st.divider()

    st.subheader("Digital Project Profile")

    profil_col1, profil_col2 = st.columns(2)

    with profil_col1:
        st.write(f"**Nutzerrolle:** {rolle}")
        st.write(f"**Gebäudetyp:** {gebaeude}")

    with profil_col2:
        st.write(f"**Anwendung:** {anwendung}")
        st.write(f"**Projektphase:** {projektphase}")

    st.caption(
        "Das Projektprofil entsteht automatisch aus den digitalen Interaktionen des Nutzers."
    )
    st.divider()

    st.subheader("Lead Score")

    score = 0

    if rolle != "Unbekannt":
        score += 15

    if gebaeude != "Nicht erkannt":
        score += 15

    if anwendung != "Allgemeine Anfrage":
        score += 25

    if projektphase != "Nicht erkannt":
        score += 20

    if "bim" in text:
        score += 10

    if "datenblatt" in text or "ausschreibung" in text:
        score += 10

    if "kontakt" in text or "beratung" in text:
        score += 20

    if score > 100:
        score = 100

    if score >= 70:
        status = "SQL"
    elif score >= 40:
        status = "MQL"
    else:
        status = "Marketing Contact"

    score_col1, score_col2 = st.columns(2)

    with score_col1:
        st.metric("Lead Score", f"{score}/100")

    with score_col2:
        st.metric("Status", status)

    st.progress(score / 100)

    st.caption(
        "Der Lead Score bewertet den Projektkontext und die digitale Kaufabsicht."
    )
