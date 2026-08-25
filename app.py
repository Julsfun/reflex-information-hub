import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Ask Reflex",
    page_icon="🔎",
    layout="wide"
)

st.markdown(
    """
    <style>

    .stApp {
        background-color: #ffffff;
        color: #1f1f1f;
    }

    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    h1 {
        font-size: 3rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.03em;
        color: #202020 !important;
        margin-bottom: 0.4rem !important;
    }

    h2, h3 {
        color: #202020 !important;
        font-weight: 600 !important;
    }

    p {
        color: #4a4a4a;
    }

    div.stButton > button {
        background-color: #202020;
        color: white;
        border: none;
        border-radius: 2px;
        padding: 0.7rem 1.4rem;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #3b3b3b;
        color: white;
        border: none;
    }

    div[data-testid="stMetric"] {
        background-color: #f6f6f4;
        border: 1px solid #e8e8e5;
        padding: 1rem;
        border-radius: 2px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid #e7e7e3 !important;
        border-radius: 2px !important;
        background-color: #fafafa;
    }

    .stProgress > div > div > div > div {
        background-color: #222222;
    }

    div[data-testid="stAlert"] {
        border-radius: 2px;
    }

    textarea {
        border-radius: 2px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

BASE_DIR = Path(__file__).parent
produkte = pd.read_csv(BASE_DIR / "product.csv")

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

    text = frage.lower()

    rolle = "Unbekannt"
    gebaeude = "Nicht erkannt"
    anwendung = "Allgemeine Anfrage"
    projektphase = "Nicht erkannt"

    if (
        "plane" in text
        or "planer" in text
        or "planung" in text
    ):
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

    if (
        "datenblatt" in text
        or "ausschreibung" in text
    ):
        score += 10

    if (
        "kontakt" in text
        or "beratung" in text
    ):
        score += 20

    score = min(score, 100)

    if score >= 70:
        status = "SQL"
    elif score >= 40:
        status = "MQL"
    else:
        status = "Marketing Contact"

    kunden_tab, sales_tab = st.tabs(
        ["Kundensicht", "Sales-Sicht"]
    )

    # -----------------------------
    # KUNDENSICHT
    # -----------------------------

    with kunden_tab:

        st.markdown("### KI-Interpretation")

        interpretation = (
            f"Die Anfrage wird als **{anwendung}** "
            f"für den Gebäudetyp **{gebaeude}** "
            f"in der Projektphase **{projektphase}** interpretiert."
        )

        st.info(interpretation)
        
        st.subheader("Ihr Projektkontext")

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

            st.success(
                "Passende Reflex-Lösung für Druckhaltung"
            )

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

            st.success(
                "Installations- und Serviceinformationen"
            )

            st.write("🔧 Montageanleitung")
            st.write("📄 Inbetriebnahmehinweise")
            st.write("🛠️ Troubleshooting")

        else:

            st.info(
                "Bitte beschreiben Sie Ihr Projekt "
                "noch etwas genauer."
            )

        st.divider()

        st.subheader("Gefundene Produktdaten")

        if anwendung == "Druckhaltung":

            treffer = produkte[
                produkte["category"].str.contains(
                    "Druckhaltung",
                    case=False,
                    na=False
                )
            ]

            if not treffer.empty:

                for _, produkt in treffer.iterrows():

                    with st.container(border=True):

                        st.markdown(
                            f"### {produkt['product_name']}"
                        )

                        st.write(
                            produkt["description"]
                        )

                        produkt_col1, produkt_col2 = st.columns(2)

                        with produkt_col1:

                            st.write(
                                f"**Kategorie:** "
                                f"{produkt['category']}"
                            )

                            st.write(
                                f"**Anwendung:** "
                                f"{produkt['application']}"
                            )

                            st.write(
                                f"**Systemtyp:** "
                                f"{produkt['system_type']}"
                            )

                        with produkt_col2:

                            st.write(
                                f"**Max. Betriebsdruck:** "
                                f"{produkt['max_operating_pressure']}"
                            )

                            st.write(
                                f"**Steuerung:** "
                                f"{produkt['control']}"
                            )

                            st.write(
                                f"**Artikelnummer:** "
                                f"{produkt['article_number']}"
                            )

                        st.link_button(
                            "Produktdetails bei Reflex öffnen",
                            produkt["source_url"],
                            use_container_width=True
                        )

            else:

                st.warning(
                    "Für diese Anwendung wurden noch "
                    "keine Produktdaten gefunden."
                )

        else:

            st.info(
                "Für diese Anfrage werden im nächsten "
                "Schritt weitere Produktkategorien angebunden."
            )

    # -----------------------------
    # SALES-SICHT
    # -----------------------------

    with sales_tab:

        st.subheader("Digital Project Profile")

        profil_col1, profil_col2 = st.columns(2)

        with profil_col1:

            st.write(
                f"**Nutzerrolle:** {rolle}"
            )

            st.write(
                f"**Gebäudetyp:** {gebaeude}"
            )

        with profil_col2:

            st.write(
                f"**Anwendung:** {anwendung}"
            )

            st.write(
                f"**Projektphase:** {projektphase}"
            )

        st.caption(
            "Das Projektprofil entsteht automatisch "
            "aus den digitalen Interaktionen des Nutzers."
        )

        st.divider()

        st.subheader("Lead Qualification")

        score_col1, score_col2 = st.columns(2)

        with score_col1:

            st.metric(
                "Lead Score",
                f"{score}/100"
            )

        with score_col2:

            st.metric(
                "Status",
                status
            )

        st.progress(score / 100)

        st.caption(
            "Der Lead Score bewertet den Projektkontext "
            "und die digitale Kaufabsicht."
        )

        st.divider()

        st.subheader("Empfohlene Sales-Aktion")

        if status == "SQL":

            st.success(
                "Hohe Kaufabsicht erkannt – "
                "persönliche Kontaktaufnahme priorisieren."
            )

            st.write(
                "**Nächster Schritt:** "
                "Technischen Vertrieb informieren"
            )

        elif status == "MQL":

            st.info(
                "Relevantes Projektinteresse erkannt – "
                "weitere digitale Interaktionen beobachten."
            )

            st.write(
                "**Nächster Schritt:** "
                "Passende Inhalte und Tools anbieten"
            )

        else:

            st.write(
                "Noch kein unmittelbarer Vertriebsbedarf."
            )

            st.write(
                "**Nächster Schritt:** "
                "Nutzer weiter mit relevantem Content unterstützen"
            )
