import streamlit as st
import random

# Funzione per calcolare la difficoltà
def calcola_difficolta(tempo_totale):
    if tempo_totale < 20:
        return "Facile"
    elif 20 <= tempo_totale <= 40:
        return "Medio"
    else:
        return "Difficile"

# Funzione per generare una ricetta dettagliata
def genera_ricetta(ingredienti):
    # Se non ci sono ingredienti, restituiamo un messaggio di errore
    if not ingredienti:
        return None, "Non ci sono abbastanza ingredienti per creare una ricetta. Aggiungi qualcosa e riprova."

    # Generazione casuale dei tempi e delle quantità
    titolo = f"Piatto a base di {', '.join(ingredienti).capitalize()}"
    tempo_preparazione = random.randint(10, 20)
    tempo_cottura = random.randint(15, 30)
    tempo_totale = tempo_preparazione + tempo_cottura
    difficolta = calcola_difficolta(tempo_totale)
    quantita_ingredienti = {ing: f"{random.randint(50, 200)}g" for ing in ingredienti}

    # Preparazione del piatto
    preparazione = f"Unite {', '.join(ingredienti)} in una ciotola capiente. " \
                   "Scaldate una padella antiaderente con un filo d'olio extra vergine di oliva. " \
                   "Aggiungete gli ingredienti e lasciateli rosolare dolcemente a fuoco medio. " \
                   "Dopo qualche minuto, abbassate la fiamma e mescolate delicatamente per amalgamare i sapori. " \
                   "Continuate la cottura finché gli ingredienti non raggiungono una consistenza morbida ma compatta. " \
                   "Aggiungete sale e pepe a piacere."

    # Consigli per l'impiattamento
    impiattamento = "Servite in un piatto fondo o una ciotola rustica. Disponete gli ingredienti uniformemente, " \
                    "aggiungendo un filo d'olio a crudo e, se lo gradite, una spolverata di prezzemolo fresco."

    # Valori nutrizionali
    valori_nutrizionali = {
        "Calorie": random.randint(400, 800),
        "Proteine": random.randint(20, 40),
        "Grassi": random.randint(10, 30),
        "Carboidrati": random.randint(40, 90),
        "Fibre": random.randint(5, 15),
        "Zuccheri": random.randint(2, 8),
        "Sale": round(random.uniform(0.5, 1.5), 1)
    }

    # Ricetta completa
    ricetta = {
        "titolo": titolo,
        "tempo_preparazione": tempo_preparazione,
        "tempo_cottura": tempo_cottura,
        "tempo_totale": tempo_totale,
        "difficolta": difficolta,
        "quantita_ingredienti": quantita_ingredienti,
        "preparazione": preparazione,
        "impiattamento": impiattamento,
        "valori_nutrizionali": valori_nutrizionali
    }

    return ricetta, None

# Funzione per generare una variante
def genera_variante(ricetta_base):
    variante = ricetta_base.copy()
    variante["titolo"] += " (Variante con Tocco Magico)"
    variante["preparazione"] += " Aggiungere una spolverata di pecorino romano grattugiato e qualche goccia di limone prima di servire."
    variante["valori_nutrizionali"]["Calorie"] += 50
    return variante

# Interfaccia Streamlit
st.title("🍽️ Generatore di Ricette Personalizzate")
st.write("Inserisci gli ingredienti che hai a disposizione e lasciati ispirare da nuove ricette!")

# Inserimento degli ingredienti
ingredienti_input = st.text_input("Ingredienti disponibili (separati da virgola):")
ingredienti = [ing.strip().lower() for ing in ingredienti_input.split(",") if ing.strip()]

# Pulsante per generare la ricetta
if st.button("Genera Ricetta"):
    ricetta, errore = genera_ricetta(ingredienti)
    if errore:
        st.error(errore)
    elif ricetta:
        st.subheader(f"🍽️ {ricetta['titolo']}")
        st.write(f"**Tempo di preparazione:** {ricetta['tempo_preparazione']} minuti")
        st.write(f"**Tempo di cottura:** {ricetta['tempo_cottura']} minuti")
        st.write(f"**Difficoltà:** {ricetta['difficolta']}")

        st.write("**Ingredienti:**")
        for ingr, qty in ricetta["quantita_ingredienti"].items():
            st.write(f"- {ingr.capitalize()}: {qty}")

        st.subheader("Preparazione:")
        st.write(ricetta["preparazione"])

        st.subheader("Impiattamento:")
        st.write(ricetta["impiattamento"])

        st.subheader("Valori Nutrizionali:")
        for k, v in ricetta["valori_nutrizionali"].items():
            st.write(f"- {k}: {v}")

        st.subheader("Valore Proteico:")
        st.write(f"- Proteine: {ricetta['valori_nutrizionali']['Proteine']}g")

        # Variante con tocco magico
        variante = genera_variante(ricetta)
        st.subheader(f"🍽️ {variante['titolo']}")
        st.write("**Preparazione Variante:**")
        st.write(variante["preparazione"])
    else:
        st.error("Non è stato possibile generare una ricetta.")
