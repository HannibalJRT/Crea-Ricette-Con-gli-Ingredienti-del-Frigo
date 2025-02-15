import streamlit as st
import random

# Funzione per generare una ricetta base
def genera_ricetta(ingredienti):
    if not ingredienti:
        return "Nessun ingrediente fornito. Aggiungi degli ingredienti per iniziare!"

    # Creazione di una ricetta semplice
    titolo = f"Ricetta con {', '.join(ingredienti)}"
    tempo_preparazione = random.randint(5, 10)
    tempo_cottura = random.randint(10, 20)
    difficolta = "Facile" if tempo_preparazione + tempo_cottura < 30 else "Medio"
    
    procedura = (
        f"1. Unisci {', '.join(ingredienti)} in una ciotola. "
        "2. Scalda una padella con un filo d'olio. "
        "3. Aggiungi gli ingredienti e cuoci per 10-15 minuti, mescolando di tanto in tanto."
    )
    
    valori_nutrizionali = {
        "Calorie": random.randint(200, 500),
        "Proteine": random.randint(10, 30),
        "Grassi": random.randint(5, 20),
        "Carboidrati": random.randint(20, 50)
    }

    # Restituisci la ricetta formattata
    return {
        "titolo": titolo,
        "tempo_preparazione": tempo_preparazione,
        "tempo_cottura": tempo_cottura,
        "difficolta": difficolta,
        "procedura": procedura,
        "valori_nutrizionali": valori_nutrizionali
    }

# Interfaccia Streamlit
st.title("🍴 Generatore di Ricette")
st.write("Inserisci gli ingredienti separati da una virgola e premi il pulsante per generare una ricetta.")

# Campo di input per gli ingredienti
ingredienti_input = st.text_input("Ingredienti disponibili:")
if st.button("Genera Ricetta"):
    ingredienti = [ing.strip() for ing in ingredienti_input.split(",") if ing.strip()]
    ricetta = genera_ricetta(ingredienti)
    if isinstance(ricetta, str):
        st.error(ricetta)
    else:
        st.subheader(ricetta["titolo"])
        st.write(f"**Tempo di preparazione:** {ricetta['tempo_preparazione']} minuti")
        st.write(f"**Tempo di cottura:** {ricetta['tempo_cottura']} minuti")
        st.write(f"**Difficoltà:** {ricetta['difficolta']}")
        st.subheader("Procedura")
        st.write(ricetta["procedura"])
        st.subheader("Valori nutrizionali")
        for k, v in ricetta["valori_nutrizionali"].items():
            st.write(f"- {k}: {v}")
