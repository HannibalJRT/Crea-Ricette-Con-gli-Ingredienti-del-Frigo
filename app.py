import streamlit as st
import random

# Funzione per generare una ricetta base
def genera_ricetta(ingredienti):
    # Controlliamo se gli ingredienti sono accettabili (nel tuo caso, implementa qui logiche più complesse)
    if "radicchio" in ingredienti:
        return None, "Non è stato possibile creare una ricetta sensata con gli ingredienti forniti. Rimuovi il radicchio e prova di nuovo."
    
    # Generiamo una ricetta casuale e i valori nutrizionali
    titolo = f"Ricetta con {', '.join(ingredienti).capitalize()}"
    tempo_preparazione = random.randint(5, 15)
    tempo_cottura = random.randint(10, 30)
    difficolta = "Medio" if tempo_cottura < 20 else "Difficile"

    valori_nutrizionali = {
        "Calorie": random.randint(300, 700),
        "Proteine": random.randint(20, 50),
        "Grassi": random.randint(10, 30),
        "Carboidrati": random.randint(40, 100),
        "Fibre": random.randint(5, 15),
        "Zuccheri": random.randint(2, 8),
        "Sale": round(random.uniform(0.2, 1.5), 2),
    }

    # Procedimento della ricetta
    procedimento = [
        "Preparare gli ingredienti sul piano di lavoro.",
        "Tagliare a cubetti la carne e marinarla per 10 minuti.",
        "Scaldare l’olio in una padella e cuocere la carne a fuoco medio per 7 minuti.",
        "Saltare le verdure in padella con poco olio per 5 minuti.",
        "Aggiungere un pizzico di sale e pepe.",
        "Impiattare e servire caldo."
    ]

    return {
        "titolo": titolo,
        "tempo_preparazione": tempo_preparazione,
        "tempo_cottura": tempo_cottura,
        "difficolta": difficolta,
        "ingredienti": ingredienti,
        "valori_nutrizionali": valori_nutrizionali,
        "procedimento": procedimento
    }, None

# Funzione per generare una variante della ricetta
def genera_variante_ricetta(ricetta_base):
    variante = ricetta_base.copy()
    variante["titolo"] += " (Variante con Tocco Magico)"
    variante["procedimento"].append("Aggiungere una spolverata di formaggio grattugiato.")
    variante["valori_nutrizionali"]["Calorie"] += 50
    return variante

# Interfaccia utente con Streamlit
st.title("🍽️ Generatore di Ricette Personalizzate")

# Input: ingredienti
ingredienti_input = st.text_input("Inserisci gli ingredienti disponibili (separati da virgola):")
if not ingredienti_input:
    st.warning("Inserisci almeno un ingrediente.")
else:
    ingredienti = [ingr.strip().lower() for ingr in ingredienti_input.split(",")]

    # Scelta della modalità
    modalita = st.radio("Scegli il tipo di ricetta:", ("Ricetta Base", "Ricetta con Variante"))

    # Pulsante per generare la ricetta
    if st.button("Genera Ricetta"):
        ricetta, errore = genera_ricetta(ingredienti)
        if errore:
            st.error(errore)
        else:
            # Se è selezionata la variante, generiamo una variante
            if modalita == "Ricetta con Variante":
                ricetta = genera_variante_ricetta(ricetta)
            
            # Mostriamo la ricetta
            st.subheader(ricetta["titolo"])
            st.write(f"**Tempo di preparazione:** {ricetta['tempo_preparazione']} minuti")
            st.write(f"**Tempo di cottura:** {ricetta['tempo_cottura']} minuti")
            st.write(f"**Difficoltà:** {ricetta['difficolta']}")
            st.write("**Ingredienti:**")
            for ingr in ricetta["ingredienti"]:
                st.write(f"- {ingr.capitalize()}")
            st.write("**Procedimento:**")
            for passo in ricetta["procedimento"]:
                st.write(f"- {passo}")
            st.write("**Valori Nutrizionali:**")
            for chiave, valore in ricetta["valori_nutrizionali"].items():
                st.write(f"- {chiave}: {valore}")
