import streamlit as st
import random

# Funzione per calcolare la difficoltà della ricetta
def calcola_difficolta(tempo_totale):
    if tempo_totale < 15:
        return "Facile"
    elif 15 <= tempo_totale <= 30:
        return "Medio"
    else:
        return "Difficile"

# Funzione per generare la ricetta base con gli ingredienti forniti dall'utente
def genera_ricetta_base(ingredienti):
    titolo_ricetta = f"Ricetta Originale con {', '.join(ingredienti)}"
    
    tempo_preparazione = random.randint(5, 15)
    tempo_cottura = random.randint(10, 30)
    tempo_totale = tempo_preparazione + tempo_cottura
    difficolta = calcola_difficolta(tempo_totale)

    # Generazione delle quantità per ogni ingrediente
    quantita = {ingrediente: f"{random.randint(50, 300)}g" for ingrediente in ingredienti}

    istruzioni = [
        f"🔹 **Passaggio 1:** Prepara tutti gli ingredienti: {', '.join(ingredienti)}. Lavali e tagliali se necessario. *(Tempo: {tempo_preparazione} minuti)*",
        f"🔹 **Passaggio 2:** Scalda una padella con un cucchiaio di olio d'oliva. *(Tempo: 2 minuti)*",
        f"🔹 **Passaggio 3:** Se hai carne o pesce, condiscilo con sale, pepe e spezie e cuocilo per 5-7 minuti per lato.",
        f"🔹 **Passaggio 4:** Se hai riso o pasta, cuocili per {random.randint(8, 15)} minuti.",
        f"🔹 **Passaggio 5:** Aggiungi le verdure e falle saltare per 3-5 minuti.",
        f"🔹 **Passaggio 6:** Mescola bene tutti gli ingredienti, condisci a piacere e servi caldo. *(Tempo totale: {tempo_totale} minuti)*",
        "🔹 **Passaggio 7:** Buon appetito! 🍽️"
    ]

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

    return titolo_ricetta, difficolta, tempo_preparazione, tempo_cottura, tempo_totale, quantita, istruzioni, valori_nutrizionali

# Funzione per generare una versione migliorata della ricetta con ingredienti sostitutivi
def genera_ricetta_migliorata(ingredienti):
    sostituzioni = {
        "latte": "latte di mandorla o soia",
        "burro": "olio d'oliva o olio di cocco",
        "zucchero": "miele o sciroppo d'acero",
        "riso": "quinoa o couscous",
        "carne": "tofu o lenticchie",
        "pasta": "zucchine a spirale o pasta integrale"
    }
    
    ingredienti_migliorati = [sostituzioni.get(ingrediente, ingrediente) for ingrediente in ingredienti]

    return genera_ricetta_base(ingredienti_migliorati)

# Streamlit UI
st.title("🥗 Generatore di Ricette High-Protein per Atleti")
st.write("Inserisci gli ingredienti che hai a disposizione:")

ingredienti_input = st.text_input("🔍 Inserisci gli ingredienti (separati da virgola)")

if st.button("🔎 Genera Ricetta"):
    if ingredienti_input:
        lista_ingredienti = [i.strip().lower() for i in ingredienti_input.split(",")]

        # Genera Ricetta Base
        titolo_base, difficolta_base, tempo_preparazione_base, tempo_cottura_base, tempo_totale_base, quantita_base, istruzioni_base, valori_base = genera_ricetta_base(lista_ingredienti)

        # Genera Ricetta Migliorata
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

        # Mostra Ricetta Migliorata
        st.subheader(f"✨ **{titolo_migliorata} (Versione Migliorata)**")
        st.write(f"⏳ **Preparazione:** {tempo_preparazione_migliorata} min | 🔥 **Cottura:** {tempo_cottura_migliorata} min | ⭐ **Difficoltà:** {difficolta_migliorata}")
        st.subheader("📌 **Ingredienti:**")
        for ingrediente, quantita in quantita_migliorata.items():
            st.write(f"- {ingrediente.capitalize()}: {quantita}")
        st.subheader("📌 **Preparazione:**")
        for passo in istruzioni_migliorata:
            st.write(passo)
        st.subheader("🔥 **Valori Nutrizionali:**")
        for chiave, valore in valori_migliorata.items():
            st.write(f"- **{chiave}**: {valore}")

    else:
        st.warning("Inserisci gli ingredienti per generare una ricetta.")

