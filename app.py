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

# Funzione per creare una ricetta dettagliata e fluida
def genera_ricetta(ingredienti):
    titolo_ricetta = f"Ricetta con {', '.join(ingredienti).capitalize()}"
    
    tempo_preparazione = random.randint(5, 15)
    tempo_cottura = random.randint(10, 30)
    tempo_totale = tempo_preparazione + tempo_cottura
    difficolta = calcola_difficolta(tempo_totale)

    # Generazione delle quantità per ogni ingrediente
    quantita = {ingrediente: f"{random.randint(50, 300)}g" for ingrediente in ingredienti}

    # Struttura della preparazione fluida e ben descritta
    preparazione = []
    
    preparazione.append(f"Per iniziare, raccogli tutti gli ingredienti necessari: {', '.join(ingredienti)}. Se necessario, lavali accuratamente e procedi al taglio per facilitarne la cottura.")
    
    if "carne" in ingredienti:
        preparazione.append("Se hai scelto la carne, tagliala a cubetti e condiscila con sale, pepe e spezie a piacere. Scalda una padella con un filo d'olio e cuocila a fuoco medio per circa 7-10 minuti, mescolando di tanto in tanto per una doratura uniforme.")

    if "pesce" in ingredienti:
        preparazione.append("Se hai optato per il pesce, insaporiscilo con un pizzico di sale, pepe e qualche goccia di limone. Cuocilo in una padella antiaderente con un filo d'olio per circa 4-5 minuti per lato, fino a quando la carne risulterà tenera e leggermente croccante all'esterno.")

    if "riso" in ingredienti:
        preparazione.append("Per la preparazione del riso, porta a ebollizione 500ml di acqua salata e aggiungi il riso. Lascia cuocere a fuoco medio per circa 12 minuti, mescolando di tanto in tanto. Una volta pronto, scolalo e lascialo riposare per un paio di minuti prima di servirlo.")

    if "pasta" in ingredienti:
        preparazione.append("Se hai deciso di usare la pasta, riempi una pentola con abbondante acqua salata e portala a ebollizione. Aggiungi la pasta e cuocila secondo il tempo indicato sulla confezione, mescolando occasionalmente per evitare che si attacchi. Una volta cotta, scolala e tienila da parte.")

    if "radicchio" in ingredienti or "zucchine" in ingredienti or "verdure" in ingredienti:
        preparazione.append("Le verdure possono essere tagliate a fettine sottili e saltate in padella con un filo d'olio d'oliva. Cuocile per circa 5 minuti a fuoco medio, fino a quando diventano tenere ma ancora croccanti. Se preferisci, puoi grigliarle per un sapore più intenso.")

    if "avocado" in ingredienti:
        preparazione.append("Se hai un avocado, taglialo a metà e rimuovi il nocciolo. Schiaccia la polpa con una forchetta e aggiungi un pizzico di sale, qualche goccia di limone e una spolverata di pepe. Questa crema di avocado è perfetta per accompagnare il piatto.")

    if "noci" in ingredienti:
        preparazione.append("Le noci possono essere leggermente tostate in padella per 2-3 minuti, mescolandole continuamente per evitare che si brucino. Questo passaggio aiuta a esaltare il loro sapore e a renderle ancora più croccanti.")

    preparazione.append(f"Una volta che tutti gli ingredienti sono pronti, impiatta il tutto con cura e servi il piatto caldo. *(Tempo totale: {tempo_totale} minuti)*")
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

# Funzione per creare la variante con ingredienti extra
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
