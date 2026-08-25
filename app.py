import streamlit as st
import pandas as pd
from pathlib import Path

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Ask Reflex",
    page_icon="🔎",
    layout="wide"
)

# -------------------------------------------------
# DESIGN / REFLEX-INSPIRED LOOK
# -------------------------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background-color: #ffffff;
        color: #242424;
    }

    .block-container {
        padding-top: 2.3rem;
        padding-bottom: 4rem;
        max-width: 1180px;
    }

    h1 {
        font-size: 3.2rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.035em;
        color: #222222 !important;
        margin-bottom: 0.2rem !important;
    }

    h2 {
        color: #222222 !important;
        font-weight: 650 !important;
        margin-top: 1rem !important;
    }

    h3 {
        color: #222222 !important;
        font-weight: 600 !important;
    }

    p {
        color: #4b4b4b;
    }

    div.stButton > button {
        background-color: #86c440;
        color: #1f1f1f;
        border: none;
        border-radius: 3px;
        padding: 0.75rem 1.5rem;
        font-weight: 650;
    }

    div.stButton > button:hover {
        background-color: #76b337;
        color: #111111;
        border: none;
    }

    div[data-testid="stMetric"] {
        background-color: #f5f5f3;
        border: 1px solid #e5e5e2;
        padding: 1rem;
        border-radius: 3px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid #e2e2df !important;
        border-radius: 3px !important;
        background-color: #fafafa;
    }

    div[data-testid="stAlert"] {
        border-radius: 3px;
    }

    textarea {
        border-radius: 3px !important;
    }

    .stProgress > div > div > div > div {
        background-color: #86c440;
    }

    .hero-kicker {
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 700;
        color: #86c440;
        margin-bottom: 0.25rem;
    }

    .hero-copy {
        font-size: 1.15rem;
        color: #5a5a5a;
        max-width: 760px;
        margin-bottom: 1.8rem;
    }

    .demo-note {
        background: #f5f5f3;
        border-left: 4px solid #86c440;
        padding: 0.8rem 1rem;
        margin-top: 2rem;
        font-size: 0.9rem;
        color: #555555;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# DATA LOAD
# -------------------------------------------------

BASE_DIR = Path(__file__).parent
PRODUCT_FILE = BASE_DIR / "product.csv"

try:
    produkte = pd.read_csv(PRODUCT_FILE)
except Exception:
    st.error(
        "Die Produktdaten konnten nicht geladen werden. "
        "Bitte prüfen Sie die Datei product.csv."
    )
    st.stop()

# -------------------------------------------------
# HERO
# -------------------------------------------------

st.markdown(
    '<div class="hero-kicker">Reflex Thinking Solutions</div>',
    unsafe_allow_html=True
)

st.title("Ask Reflex")

st.markdown(
    """
    <div class="hero-copy">
    Die intelligente Informationsdrehscheibe für Planung, Produkte und Services.
    Beschreiben Sie Ihr Projekt oder Ihre Aufgabe – Ask Reflex priorisiert
    die relevanten Informationen und nächsten Schritte.
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# INPUT
# -------------------------------------------------

frage = st.text_area(
    "Was möchten Sie für Ihr Projekt erreichen?",
    placeholder=(
        "Beispiel: Ich plane ein Bürogebäude und brauche "
        "eine Lösung für die Druckhaltung sowie BIM-Daten."
    ),
    height=120
)

analyse_starten = st.button(
    "Projekt analysieren",
    use_container_width=True
)

# -------------------------------------------------
# ANALYSIS
# -------------------------------------------------

if analyse_starten:

    if not frage.strip():
        st.warning("Bitte beschreiben Sie zuerst Ihr Projekt oder Ihre Aufgabe.")
        st.stop()

    text = frage.lower()

    rolle = "Unbekannt"
    gebaeude = "Nicht erkannt"
    anwendung = "Allgemeine Anfrage"
    projektphase = "Nicht erkannt"

    # ---------------------------------------------
    # PERSONA
    # ---------------------------------------------

    if (
        "plane" in text
        or "planung" in text
        or "planer" in text
        or "tga" in text
        or "ingenieur" in text
    ):
        rolle = "TGA-Planer"

    elif (
        "installateur" in text
        or "installation" in text
        or "montage" in text
        or "inbetriebnahme" in text
    ):
        rolle = "Installateur / Fachhandwerker"

    elif (
        "betreiber" in text
        or "facility" in text
        or "wartung" in text
        or "service" in text
    ):
        rolle = "Betreiber / Facility Manager"

    # ---------------------------------------------
    # BUILDING TYPE
    # ---------------------------------------------

    if "büro" in text or "office" in text:
        gebaeude = "Bürogebäude"

    elif "hotel" in text:
        gebaeude = "Hotel"

    elif "industrie" in text:
        gebaeude = "Industriegebäude"

    elif "krankenhaus" in text or "klinik" in text:
        gebaeude = "Krankenhaus"

    elif "wohn" in text:
        gebaeude = "Wohngebäude"

    # ---------------------------------------------
    # APPLICATION / INTENT
    # ---------------------------------------------

    if "druckhaltung" in text or "druck halten" in text:
        anwendung = "Druckhaltung"

    elif "bim" in text or "cad" in text:
        anwendung = "BIM / Planungsdaten"

    elif (
        "installation" in text
        or "montage" in text
        or "inbetriebnahme" in text
    ):
        anwendung = "Installation"

    elif (
        "wartung" in text
        or "service" in text
        or "störung" in text
        or "fehler" in text
    ):
        anwendung = "Service / Betrieb"

    # ---------------------------------------------
    # PROJECT PHASE
    # ---------------------------------------------

    if (
        "planung" in text
        or "plane" in text
        or "entwurf" in text
        or "ausschreibung" in text
    ):
        projektphase = "Planung"

    elif (
        "installation" in text
        or "montage" in text
        or "inbetriebnahme" in text
    ):
        projektphase = "Ausführung"

    elif (
        "wartung" in text
        or "betrieb" in text
        or "service" in text
    ):
        projektphase = "Betrieb"

    # ---------------------------------------------
    # LEAD SCORE
    # ---------------------------------------------

    score = 0

    if rolle != "Unbekannt":
        score += 15

    if gebaeude != "Nicht erkannt":
        score += 15

    if anwendung != "Allgemeine Anfrage":
        score += 25

    if projektphase != "Nicht erkannt":
        score += 20

    if "bim" in text or "cad" in text:
        score += 10

    if "datenblatt" in text or "ausschreibung" in text:
        score += 10

    if (
        "beratung" in text
        or "kontakt" in text
        or "angebot" in text
    ):
        score += 20

    score = min(score, 100)

    if score >= 70:
        status = "SQL"
    elif score >= 40:
        status = "MQL"
    else:
        status = "Marketing Contact"

    # ---------------------------------------------
    # TABS
    # ---------------------------------------------

    kunden_tab, sales_tab = st.tabs(
        ["Kundensicht", "Sales-Sicht"]
    )

    # =============================================
    # CUSTOMER VIEW
    # =============================================

    with kunden_tab:

        st.markdown("### KI-Interpretation")

        interpretation = (
            f"Die Anfrage wird als **{anwendung}** "
            f"für **{gebaeude}** in der Projektphase "
            f"**{projektphase}** interpretiert."
        )

        st.info(interpretation)

        st.subheader("Erkannter Projektkontext")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("Rolle", rolle)

        with c2:
            st.metric("Gebäude", gebaeude)

        with c3:
            st.metric("Anwendung", anwendung)

        with c4:
            st.metric("Projektphase", projektphase)

        st.subheader("Empfohlene Reflex-Inhalte")

        if anwendung == "Druckhaltung":

            st.success(
                "Priorität: passende Druckhaltungslösung "
                "mit Planungs- und Produktinformationen"
            )

            st.markdown("#### Warum empfohlen?")

            st.write(
                "Die Anfrage enthält einen konkreten Planungsfall "
                "mit Bedarf im Bereich Druckhaltung. Deshalb werden "
                "zuerst geeignete Druckhaltungslösungen sowie technische "
                "und planerische Informationen priorisiert."
            )

            st.write("📄 Technische Produktdaten")
            st.write("🏗️ BIM- / CAD-Informationen")
            st.write("📝 Ausschreibungsinformationen")
            st.write("🧮 Auslegung / Berechnung")

        elif anwendung == "BIM / Planungsdaten":

            st.success("Priorität: BIM- und Planungsinformationen")

            st.write("🏗️ BIM-Daten")
            st.write("📐 CAD-Daten")
            st.write("📄 Technische Produktdaten")
            st.write("📝 Ausschreibungsinformationen")

        elif anwendung == "Installation":

            st.success(
                "Priorität: Installations- und Inbetriebnahmeinformationen"
            )

            st.write("🔧 Montageinformationen")
            st.write("📄 Inbetriebnahmehinweise")
            st.write("🛠️ Troubleshooting")
            st.write("📚 Weiterführende Dokumentation")

        elif anwendung == "Service / Betrieb":

            st.success(
                "Priorität: Service- und Betriebsinformationen"
            )

            st.write("🔧 Wartungsinformationen")
            st.write("🛠️ Troubleshooting")
            st.write("📄 Betriebsunterlagen")
            st.write("♻️ Lifecycle-Informationen")

        else:

            st.info(
                "Bitte beschreiben Sie Ihr Projekt noch etwas genauer, "
                "damit Ask Reflex die passenden Informationen priorisieren kann."
            )

        # -----------------------------------------
        # PRODUCT DATA
        # -----------------------------------------

        st.divider()

        st.subheader("Passende Produktinformationen")

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

                        pc1, pc2 = st.columns(2)

                        with pc1:

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

                        with pc2:

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

            else:

                st.warning(
                    "Für diese Anwendung sind im Demonstrator "
                    "noch keine Produktdaten hinterlegt."
                )

        else:

            st.info(
                "Für diese Demo ist aktuell der Produktbereich "
                "Druckhaltung vollständig hinterlegt."
            )

    # =============================================
    # SALES VIEW
    # =============================================

    with sales_tab:

        st.subheader("Opportunity Summary")

        st.write(
            "Aus der Nutzerinteraktion wurde automatisch "
            "ein strukturiertes Projektprofil erzeugt."
        )

        s1, s2, s3, s4 = st.columns(4)

        with s1:
            st.metric("Persona", rolle)

        with s2:
            st.metric("Projekt", gebaeude)

        with s3:
            st.metric("Interesse", anwendung)

        with s4:
            st.metric("Phase", projektphase)

        st.divider()

        st.subheader("Lead Qualification")

        lc1, lc2 = st.columns(2)

        with lc1:
            st.metric(
                "Lead Score",
                f"{score}/100"
            )

        with lc2:
            st.metric(
                "Lead Status",
                status
            )

        st.progress(score / 100)

        if status == "SQL":

            st.success(
                "Hohe kommerzielle Relevanz erkannt."
            )

            st.markdown("#### Empfohlene Sales-Aktion")

            st.write(
                "Technischen Vertrieb priorisiert informieren und "
                "Projektkontext für die Kontaktaufnahme bereitstellen."
            )

        elif status == "MQL":

            st.info(
                "Konkretes Interesse erkannt, aber noch nicht "
                "ausreichend für eine direkte Vertriebspriorisierung."
            )

            st.markdown("#### Empfohlene nächste Aktion")

            st.write(
                "Passende technische Inhalte und Tools anbieten und "
                "weitere Interaktionen zur Qualifizierung nutzen."
            )

        else:

            st.markdown("#### Empfohlene nächste Aktion")

            st.write(
                "Nutzer zunächst mit relevantem Content unterstützen "
                "und weitere Projektsignale sammeln."
            )

        st.divider()

        st.subheader("Digital Project Profile")

        profil = {
            "Nutzerrolle": rolle,
            "Gebäudetyp": gebaeude,
            "Anwendung": anwendung,
            "Projektphase": projektphase,
            "Lead Score": score,
            "Lead Status": status
        }

        for key, value in profil.items():
            st.write(f"**{key}:** {value}")

        st.caption(
            "Im Pilotprojekt könnten diese Informationen strukturiert "
            "an CRM, Marketing Automation oder Service-Systeme übergeben werden."
        )

# -------------------------------------------------
# DISCLAIMER
# -------------------------------------------------

st.markdown(
    """
    <div class="demo-note">
    <strong>Demonstrator:</strong>
    Produktdaten, Intent-Erkennung und Lead-Scoring dienen der
    Illustration eines möglichen Pilotprojekts. Die produktive Lösung
    würde offizielle Reflex-Datenquellen und definierte Schnittstellen nutzen.
    </div>
    """,
    unsafe_allow_html=True
)
