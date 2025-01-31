import streamlit as st
import random

# Funzione per calcolare la difficoltà in base al tempo totale
def calcola_difficolta(tempo_totale):
    if tempo_totale < 15:
        return "Facile"
    elif 15 <= tempo_totale <= 30:
        return "Medio"
    else:
        return "Difficile"

# Funzione per generare la ricetta in base agli ingredienti forniti dall'utente
def genera_ricetta(ingredienti):
    titolo_ricetta = f"Ricetta con {', '.join(ingredienti).capitalize()}"
    
    tempo_preparazione = random.randint(5, 15)
    tempo_cottura = random.randint(10, 30)
    tempo_totale = tempo_preparazione + tempo_cottura
    difficolta = calcola_difficolta(tempo_totale)

    # Generazione delle quantità per ogni ingrediente
    quantita = {ingrediente: f"{random.randint(50, 300)}g" for ingrediente in ingredienti}

    # Preparazione dettagliata basata sugli ingredienti forniti
    preparazione = [
        f"🔹 **Passaggio 1:** Prepara tutti gli ingredienti: {', '.join(ingredienti)}.",
        "🔹 **Passaggio 2:** Lava e taglia gli ingredienti se necessario.",
        "🔹 **Passaggio 3:** Scalda una padella con un filo d'olio a fuoco medio."
    ]
    
    if "carne" in ingredienti:
        preparazione.append("🔹 **Passaggio 4:** Cuoci la carne per 5-7 minuti per lato fino a doratura.")

    if "pesce" in ingredienti:
        preparazione.append("🔹 **Passaggio 5:** Condisci il pesce con sale, pepe e limone e cuocilo per 4-5 minuti per lato.")

    if "riso" in ingredienti:
        preparazione.append("🔹 **Passaggio 6:** Cuoci il riso in acqua bollente per circa 12 minuti e scolalo.")

    if "pasta" in ingredienti:
        preparazione.append("🔹 **Passaggio 7:** Cuoci la pasta in acqua salata per il tempo indicato.")

    if "verdure" in ingredienti:
        preparazione.append("🔹 **Passaggio 8:** Salta le verdure in padella per 5 minuti fino a renderle croccanti.")

    if "avocado" in ingredienti:
        preparazione.append("🔹 **Passaggio 9:** Schiaccia l’avocado con una forchetta, aggiungendo sale, limone e pepe.")

    preparazione.append(f"🔹 **Passaggio 10:** Impiatta e servi caldo. *(Tempo totale: {tempo_totale} minuti)*")
    preparazione.append("🔹 **Passaggio 11:** Buon appetito! 🍽️")

    # Generazione dei valori nutrizionali
    valori_nutrizionali = {
        "Calorie": random.randint(400, 800),
        "Proteine": random.randint(30, 60),
        "Grassi": random.randint(10, 30),
        "Carboidrati": random.randint(40, 100),
        "Fibre": random.randint(5, 15),
        "Zuccheri": random.randint(2, 10),
        "Sale": round(random.uniform(0.5, 2), 1)
    }

    return titolo_ricetta, difficolta, tempo_preparazione, tempo_cottura, tempo_totale, quantita, preparazione, valori_nutrizionali

# Funzione per generare la ricetta migliorata con ingredienti extra
def genera_ricetta_migliorata(ingredienti):
    varianti = {
        "pesce": "filetto di salmone",
        "carne": "petto di pollo",
        "pane": "pane integrale tostato"
    }

    ingredienti_migliorati = ingredienti.copy()

    for chiave, valore in varianti.items():
        if chiave not in ingredienti:
            ingredienti_migliorati.append(valore)

    return genera_ricetta(ingredienti_migliorati)

# Streamlit UI
st.title("🥗 Generatore di Ricette High-Protein per Atleti")
st.write("Inserisci gli ingredienti che hai a disposizione:")

ingredienti_input = st.text_input("🔍 Inserisci gli ingredienti (separati da virgola)")

if st.button("🔎 Genera Ricetta"):
    if ingredienti_input:
        lista_ingredienti = [i.strip().lower() for i in ingredienti_input.split(",")]

        # Genera Ricetta Base
        titolo_base, difficolta_base, tempo_preparazione_base, tempo_cottura_base, tempo_totale_base, quantita_base, istruzioni_base, valori_base = genera_ricetta(lista_ingredienti)

        # Genera Ricetta Migliorata con Varianti
        titolo_migliorata, difficolta_migliorata, tempo_preparazione_migliorata, tempo_cottura_migliorata, tempo_totale_migliorata, quantita_migliorata, istruzioni_migliorata, valori_migliorata = genera_ricetta_migliorata(lista_ingredienti)

        # Mostra Ricetta Base
        st.subheader(f"🍽️ **{titolo_base}**")
        st.write(f"⏳ **Preparazione:** {tempo_preparazione_base} min | 🔥 **Cottura:** {tempo_cottura_base} min | ⭐ **Difficoltà:** {difficolta_base}")
        st.subheader("📌 **Ingredienti:**")
        for ingrediente, quantita in quantita_base.items():
            st.write(f"- {ingrediente.capitalize()}: {quantita}")
        st.subheader("📌 **Preparazione:**")
        for passo in istruzioni_base:
            st.write(passo)
        st.subheader("🔥 **Valori Nutrizionali:**")
        for chiave, valore in valori_base.items():
            st.write(f"- **{chiave}**: {valore}")

        # Mostra Ricetta Migliorata con Varianti
        st.subheader(f"✨ **{titolo_migliorata} (Versione Migliorata con Varianti)**")
        for passo in istruzioni_migliorata:
            st.write(passo)

    else:
        st.warning("Inserisci gli ingredienti per generare una ricetta.")
