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

# Funzione per generare una ricetta dettagliata e coerente
def genera_ricetta(ingredienti):
    titolo_ricetta = f"Ricetta con {', '.join(ingredienti).capitalize()}"
    
    tempo_preparazione = random.randint(5, 15)
    tempo_cottura = random.randint(10, 30)
    tempo_totale = tempo_preparazione + tempo_cottura
    difficolta = calcola_difficolta(tempo_totale)

    # Generazione delle quantità per ogni ingrediente
    quantita = {ingrediente: f"{random.randint(50, 300)}g" for ingrediente in ingredienti}

    # Creazione della preparazione dettagliata
    preparazione = []

    preparazione.append(f"Per questa ricetta utilizzeremo {', '.join(ingredienti)}. Assicuriamoci di avere tutto pronto prima di iniziare.")

    if "avena" in ingredienti:
        preparazione.append("In un pentolino, portiamo a ebollizione 250ml di latte o acqua. Aggiungiamo l'avena e cuociamo a fuoco basso per circa 5 minuti, mescolando fino a ottenere una consistenza cremosa.")

    if "banana" in ingredienti:
        preparazione.append("Sbucciamo la banana e la schiacciamo con una forchetta fino a ottenere una purea liscia. Possiamo aggiungerla all'avena cotta per un sapore più dolce.")

    if "frutta secca" in ingredienti:
        preparazione.append("Tritiamo grossolanamente la frutta secca e la aggiungiamo sopra l'avena per un tocco croccante.")

    if "noci" in ingredienti:
        preparazione.append("Le noci possono essere tostate leggermente in padella per esaltarne il sapore. Le aggiungiamo sopra l'avena come topping.")

    preparazione.append(f"Impiattiamo il tutto con cura e serviamo caldo. *(Tempo totale: {tempo_totale} minuti)*")
    preparazione.append("Buon appetito! 🍽️")

    # Generazione dei valori nutrizionali più realistici
    valori_nutrizionali = {
        "Calorie": random.randint(300, 500),
        "Proteine": random.randint(8, 15),
        "Grassi": random.randint(10, 20),
        "Carboidrati": random.randint(50, 70),
        "Fibre": random.randint(5, 10),
        "Zuccheri": random.randint(10, 20),
        "Sale": round(random.uniform(0.1, 0.5), 1)
    }

    return titolo_ricetta, difficolta, tempo_preparazione, tempo_cottura, tempo_totale, quantita, preparazione, valori_nutrizionali

# Funzione per generare una variante migliorata
def genera_ricetta_migliorata(ingredienti):
    titolo, difficolta, tempo_preparazione, tempo_cottura, tempo_totale, quantita, preparazione, valori = genera_ricetta(ingredienti)

    # Variante con aggiunta di miele e cannella per un sapore più intenso
    preparazione.append("VARIANTE: Aggiungiamo un cucchiaino di miele per un tocco di dolcezza naturale.")
    preparazione.append("Per un ulteriore aroma, spolveriamo con un pizzico di cannella prima di servire.")

    return titolo, difficolta, tempo_preparazione, tempo_cottura, tempo_totale, quantita, preparazione, valori

# Streamlit UI
st.title("🥗 Generatore di Ricette High-Protein per Atleti")
st.write("Inserisci gli ingredienti che hai a disposizione:")

ingredienti_input = st.text_input("🔍 Inserisci gli ingredienti (separati da virgola)")

if st.button("🔎 Genera Ricetta"):
    if ingredienti_input:
        lista_ingredienti = [i.strip().lower() for i in ingredienti_input.split(",")]

        titolo_base, difficolta_base, tempo_preparazione_base, tempo_cottura_base, tempo_totale_base, quantita_base, istruzioni_base, valori_base = genera_ricetta(lista_ingredienti)
        titolo_variante, difficolta_variante, tempo_preparazione_variante, tempo_cottura_variante, tempo_totale_variante, quantita_variante, istruzioni_variante, valori_variante = genera_ricetta_migliorata(lista_ingredienti)

        st.subheader(f"🍽️ **{titolo_base}**")
        for passo in istruzioni_base:
            st.write(passo)
        st.subheader(f"✨ **{titolo_variante} (Variante con Tocco Magico)**")
        for passo in istruzioni_variante:
            st.write(passo)

    else:
        st.warning("Inserisci gli ingredienti per generare una ricetta.")
