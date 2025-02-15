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

# Funzione per generare una ricetta
def genera_ricetta(ingredienti, restrizioni):
    if not ingredienti:
        return None, "Non è possibile creare una ricetta senza ingredienti."
    
    # Verifica delle restrizioni
    if restrizioni:
        if "senza glutine" in restrizioni and "farina" in ingredienti:
            return None, "La farina contiene glutine. Rimuovila o seleziona un sostituto senza glutine."

    # Generazione casuale di una ricetta di esempio
    titolo = f"Ricetta con {', '.join(ingredienti).capitalize()}"
    tempo_preparazione = random.randint(5, 15)
    tempo_cottura = random.randint(10, 30)
    difficolta = calcola_difficolta(tempo_preparazione + tempo_cottura)
    
    procedimento = f"""
    Per preparare questo piatto, iniziate mettendo sul piano di lavoro tutti gli ingredienti: {', '.join(ingredienti)}. 
    Lavate e tagliate gli ingredienti freschi come necessario. Scaldare una padella antiaderente con un filo d’olio d’oliva.
    Aggiungete le verdure e saltatele per alcuni minuti, finché iniziano a diventare morbide. Se state utilizzando carne o pesce, 
    cuoceteli separatamente fino a completa cottura. Nel frattempo, preparate una semplice salsa mescolando olio, limone, e 
    spezie a piacere. Quando tutto è pronto, mescolate gli ingredienti e servite in un piatto fondo. 
    Completate il piatto con un filo di olio extra vergine e una spolverata di pepe nero.
    """
    
    valori_nutrizionali = {
        "Calorie": random.randint(300, 700),
        "Proteine": random.randint(20, 50),
        "Grassi": random.randint(10, 30),
        "Carboidrati": random.randint(40, 100),
        "Fibre": random.randint(5, 15),
        "Zuccheri": random.randint(2, 10),
        "Sale": round(random.uniform(0.5, 2), 2),
    }

    return {
        "titolo": titolo,
        "tempo_preparazione": tempo_preparazione,
        "tempo_cottura": tempo_cottura,
        "difficolta": difficolta,
        "procedimento": procedimento,
        "valori_nutrizionali": valori_nutrizionali,
    }, None

# Funzione per generare una variante della ricetta
def genera_variante(ricetta_base):
    ricetta_variante = ricetta_base.copy()
    ricetta_variante["titolo"] += " (Variante con Tocco Magico)"
    ricetta_variante["procedimento"] += " Per aggiungere un tocco speciale, spolverate con parmigiano grattugiato e aggiungete qualche foglia di basilico fresco."
    ricetta_variante["valori_nutrizionali"]["Calorie"] += 50
    return ricetta_variante

# Interfaccia utente
st.title("🍽️ Generatore di Ricette Personalizzate")
st.write("Inserisci gli ingredienti che hai a disposizione e seleziona eventuali restrizioni dietetiche.")

# Inserimento ingredienti
ingredienti_input = st.text_input("Ingredienti disponibili (separati da virgola):")
ingredienti = [ing.strip().lower() for ing in ingredienti_input.split(",") if ing.strip()]

# Selezione restrizioni dietetiche
restrizioni = st.multiselect("Seleziona eventuali restrizioni dietetiche:", ["senza glutine", "ad alto contenuto proteico"])

# Scelta della versione della ricetta
modalita = st.radio("Scegli il tipo di ricetta:", ("Base", "Variante"))

# Pulsante per generare la ricetta
if st.button("Genera Ricetta"):
    ricetta, errore = genera_ricetta(ingredienti, restrizioni)
    if errore:
        st.error(errore)
    elif ricetta:
        if modalita == "Variante":
            ricetta = genera_variante(ricetta)
        
        # Mostra la ricetta
        st.subheader(ricetta["titolo"])
        st.write(f"**Tempo di preparazione:** {ricetta['tempo_preparazione']} minuti")
        st.write(f"**Tempo di cottura:** {ricetta['tempo_cottura']} minuti")
        st.write(f"**Difficoltà:** {ricetta['difficolta']}")
        st.subheader("Procedimento:")
        st.write(ricetta["procedimento"])
        st.subheader("Valori Nutrizionali:")
        for k, v in ricetta["valori_nutrizionali"].items():
            st.write(f"- {k}: {v}")
    else:
        st.error("Si è verificato un errore imprevisto.")
