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

# Funzione per classificare la ricetta in base agli ingredienti
def classifica_ricetta(ingredienti):
    if "pasta" in ingredienti or "spaghetti" in ingredienti or "riso" in ingredienti:
        return "Primo Piatto"
    elif "carne" in ingredienti or "pesce" in ingredienti:
        return "Secondo Piatto"
    elif "radicchio" in ingredienti or "verdure" in ingredienti or "noci" in ingredienti:
        return "Insalata Proteica"
    else:
        return "Piatto Creativo"

# Funzione per creare una ricetta ben strutturata
def genera_ricetta(ingredienti):
    titolo_ricetta = f"Ricetta: {classifica_ricetta(ingredienti)} con {', '.join(ingredienti).capitalize()}"
    
    tempo_preparazione = random.randint(5, 15)
    tempo_cottura = random.randint(10, 30)
    tempo_totale = tempo_preparazione + tempo_cottura
    difficolta = calcola_difficolta(tempo_totale)

    # Generazione delle quantità per ogni ingrediente
    quantita = {ingrediente: f"{random.randint(50, 300)}g" for ingrediente in ingredienti}

    # Struttura della preparazione dettagliata
    preparazione = []
    
    preparazione.append(f"Per questa ricetta utilizzeremo {', '.join(ingredienti)}. Laviamo e prepariamo tutti gli ingredienti prima di iniziare la cottura.")

    if "spaghetti" in ingredienti or "pasta" in ingredienti:
        preparazione.append("Portiamo a ebollizione una pentola con abbondante acqua salata. Aggiungiamo la pasta e cuociamo per il tempo indicato sulla confezione, mescolando occasionalmente.")

    if "riso" in ingredienti:
        preparazione.append("In un pentolino, portiamo a ebollizione 500ml di acqua salata. Aggiungiamo il riso e cuociamo a fuoco medio per circa 12 minuti, mescolando di tanto in tanto.")

    if "ragù pomodoro" in ingredienti:
        preparazione.append("In una padella, scaldiamo un filo d'olio e aggiungiamo il ragù di pomodoro. Lasciamolo cuocere a fuoco basso per circa 10 minuti, mescolando per far amalgamare i sapori.")

    if "carne" in ingredienti:
        preparazione.append("Tagliamo la carne a cubetti e condiamola con sale, pepe e spezie a piacere. Scaldiamo una padella con un filo d’olio e cuociamo la carne per circa 7-10 minuti fino a doratura.")

    if "pesce" in ingredienti:
        preparazione.append("Condiamo il pesce con sale, pepe e limone. Lo cuociamo in padella con un filo d'olio per circa 4-5 minuti per lato o al forno a 180°C per 15 minuti.")

    if "radicchio" in ingredienti or "verdure" in ingredienti:
        preparazione.append("Tagliamo il radicchio e le verdure a strisce sottili. Le saltiamo in padella con un filo d'olio d'oliva per 5 minuti a fuoco medio, fino a quando saranno morbide ma ancora croccanti.")

    if "pecorino romano" in ingredienti and "spaghetti" in ingredienti:
        preparazione.append("Una volta scolata la pasta, la condiamo direttamente nella padella con il ragù, aggiungendo il pecorino romano grattugiato e mescolando bene per amalgamare il tutto.")

    if "noci" in ingredienti:
        preparazione.append("Le noci possono essere leggermente tostate in padella per 2-3 minuti, mescolandole continuamente per esaltare il loro aroma e renderle croccanti.")

    preparazione.append(f"Impiattiamo il tutto con cura e serviamo caldo. *(Tempo totale: {tempo_totale} minuti)*")
    preparazione.append("Buon appetito! 🍽️")

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

# Streamlit UI
st.title("🥗 Generatore di Ricette High-Protein per Atleti")
st.write("Inserisci gli ingredienti che hai a disposizione:")

ingredienti_input = st.text_input("🔍 Inserisci gli ingredienti (separati da virgola)")

if st.button("🔎 Genera Ricetta"):
    if ingredienti_input:
        lista_ingredienti = [i.strip().lower() for i in ingredienti_input.split(",")]

        # Genera Ricetta Base
        titolo_base, difficolta_base, tempo_preparazione_base, tempo_cottura_base, tempo_totale_base, quantita_base, istruzioni_base, valori_base = genera_ricetta(lista_ingredienti)

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

    else:
        st.warning("Inserisci gli ingredienti per generare una ricetta.")

