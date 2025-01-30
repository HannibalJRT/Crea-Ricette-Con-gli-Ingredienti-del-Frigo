import streamlit as st
import random

# Funktion zur Berechnung der Schwierigkeitsstufe
def berechne_schwierigkeit(gesamtzeit):
    if gesamtzeit < 15:
        return "Einfach"
    elif 15 <= gesamtzeit <= 30:
        return "Mittel"
    else:
        return "Schwierig"

# Funktion zur Erstellung der ersten Rezeptvariante (nur mit Nutzereingaben)
def generiere_basis_rezept(zutaten):
    rezept_name = f"Original Rezept mit {', '.join(zutaten)}"
    
    vorbereitungszeit = random.randint(5, 15)
    kochzeit = random.randint(10, 30)
    gesamtzeit = vorbereitungszeit + kochzeit
    schwierigkeitsgrad = berechne_schwierigkeit(gesamtzeit)

    # Generierung der Mengen für jede Zutat
    mengen = {zutat: f"{random.randint(50, 300)}g" for zutat in zutaten}

    anweisungen = [
        f"🔹 **Schritt 1:** Bereite alle Zutaten vor: {', '.join(zutaten)}. Wasche und schneide sie nach Bedarf. *(Dauer: {vorbereitungszeit} Minuten)*",
        f"🔹 **Schritt 2:** Erhitze eine Pfanne mit einem Esslöffel Olivenöl. *(Dauer: 2 Minuten)*",
        f"🔹 **Schritt 3:** Falls du Fleisch oder Fisch hast, würze es mit Salz, Pfeffer und Gewürzen und brate es 5-7 Minuten pro Seite an.",
        f"🔹 **Schritt 4:** Falls du Reis oder Nudeln hast, koche sie für {random.randint(8, 15)} Minuten.",
        f"🔹 **Schritt 5:** Füge das Gemüse hinzu und brate es für weitere 3-5 Minuten.",
        f"🔹 **Schritt 6:** Vermische alle Zutaten gut, würze nach Geschmack und serviere es warm. *(Gesamtzeit: {gesamtzeit} Minuten)*",
        "🔹 **Schritt 7:** Guten Appetit! 🍽️"
    ]

    # Generierung der Nährwerte
    naehrwerte = {
        "Kalorien": random.randint(400, 800),
        "Eiweiß": random.randint(30, 60),
        "Fett": random.randint(10, 30),
        "Kohlenhydrate": random.randint(40, 100),
        "Ballaststoffe": random.randint(5, 15),
        "Zucker": random.randint(2, 10),
        "Salz": round(random.uniform(0.5, 2), 1)
    }

    return rezept_name, schwierigkeitsgrad, vorbereitungszeit, kochzeit, gesamtzeit, mengen, anweisungen, naehrwerte

# Funktion zur Generierung der verbesserten Rezeptvariante mit Alternativen und Tipps
def generiere_verbessertes_rezept(zutaten):
    ersatz = {
        "milch": "Mandelmilch oder Sojamilch",
        "butter": "Olivenöl oder Kokosöl",
        "zucker": "Honig oder Ahornsirup",
        "reis": "Quinoa oder Couscous",
        "fleisch": "Tofu oder Linsen",
        "nudeln": "Zucchini-Nudeln oder Vollkornnudeln"
    }
    
    verbesserte_zutaten = [ersatz.get(zutat, zutat) for zutat in zutaten]
    
    return generiere_basis_rezept(verbesserte_zutaten)

# Streamlit UI
st.title("🥗 High-Protein Rezept-Generator für Sportler")
st.write("Gib die Zutaten ein, die du im Kühlschrank hast:")

zutaten_input = st.text_input("🔍 Zutaten eingeben (durch Komma getrennt)")

if st.button("🔎 Rezept generieren"):
    if zutaten_input:
        zutaten_liste = [z.strip().lower() for z in zutaten_input.split(",")]

        # Generiere Original-Rezept
        rezept_titel, schwierigkeitsgrad, vorbereitungszeit, kochzeit, gesamtzeit, mengen, anweisungen, naehrwerte = generiere_basis_rezept(zutaten_liste)

        # Generiere Verbesserte Rezeptversion
        verbessertes_rezept_titel, verbessert_schwierigkeitsgrad, verbessert_vorbereitungszeit, verbessert_kochzeit, verbessert_gesamtzeit, verbesserte_mengen, verbesserte_anweisungen, verbesserte_naehrwerte = generiere_verbessertes_rezept(zutaten_liste)

        # Zeige Original-Rezept
        st.subheader(f"🍽️ **{rezept_titel}**")
        st.write(f"⏳ **Vorbereitungszeit:** {vorbereitungszeit} Minuten | 🔥 **Kochzeit:** {kochzeit} Minuten | ⭐ **Schwierigkeit:** {schwierigkeitsgrad}")
        st.subheader("📌 **Zutaten:**")
        for zutat, menge in mengen.items():
            st.write(f"- {zutat.capitalize()}: {menge}")
        st.subheader("📌 **Zubereitung:**")
        for schritt in anweisungen:
            st.write(schritt)
        st.subheader("🔥 **Nährwerte pro Portion:**")
        for key, value in naehrwerte.items():
            st.write(f"- **{key}**: {value}")

        # Zeige Verbesserte Version
        st.subheader(f"✨ **{verbessertes_rezept_titel} (Optimierte Version)**")
        st.write(f"⏳ **Vorbereitungszeit:** {verbessert_vorbereitungszeit} Minuten | 🔥 **Kochzeit:** {verbessert_kochzeit} Minuten | ⭐ **Schwierigkeit:** {verbessert_schwierigkeitsgrad}")
        st.subheader("📌 **Zutaten (mit Verbesserungen):**")
        for zutat, menge in verbesserte_mengen.items():
            st.write(f"- {zutat.capitalize()}: {menge}")
        st.subheader("📌 **Zubereitung:**")
        for schritt in verbesserte_anweisungen:
            st.write(schritt)
        st.subheader("🔥 **Nährwerte pro Portion:**")
        for key, value in verbesserte_naehrwerte.items():
            st.write(f"- **{key}**: {value}")

    else:
        st.warning("Bitte Zutaten eingeben, um ein Rezept zu generieren.")
