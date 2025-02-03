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

# Funzione per generare una ricetta base, utilizzando esclusivamente gli ingredienti forniti dall'utente
def genera_ricetta_base(ingredienti):
    titolo = f"Ricetta con {', '.join(ingredienti).capitalize()}"
    tempo_preparazione = random.randint(5, 15)
    tempo_cottura = random.randint(10, 30)
    tempo_totale = tempo_preparazione + tempo_cottura
    difficolta = calcola_difficolta(tempo_totale)
    quantita = {ingr: f"{random.randint(50,300)}g" for ingr in ingredienti}

    preparazione = []
    preparazione.append(f"Per questa ricetta utilizzeremo {', '.join(ingredienti)}. Assicuriamoci di avere tutto pronto prima di iniziare.")
    
    if "pasta" in ingredienti or "spaghetti" in ingredienti:
        preparazione.append("Portiamo a ebollizione una pentola con abbondante acqua salata, aggiungiamo la pasta e cuociamo per il tempo indicato sulla confezione, mescolando occasionalmente.")
    if "riso" in ingredienti:
        preparazione.append("In un pentolino, portiamo a ebollizione 500 ml di acqua salata, aggiungiamo il riso e lo cuociamo a fuoco medio per circa 12 minuti, quindi lo scoliamo.")
    if "ragù pomodoro" in ingredienti:
        preparazione.append("In una padella, scaldiamo un filo d'olio e aggiungiamo il ragù di pomodoro, lasciandolo cuocere a fuoco basso per circa 10 minuti per far amalgamare i sapori.")
    if "guanciale" in ingredienti:
        preparazione.append("Tagliamo il guanciale a striscioline sottili, lo facciamo rosolare in padella a fuoco medio senza aggiungere olio, fino a renderlo croccante, e poi lo mettiamo da parte.")
    if "carne" in ingredienti:
        preparazione.append("Tagliamo la carne a cubetti, condiscendola con sale, pepe e spezie, e la cuociamo in padella con un filo d’olio per circa 7-10 minuti fino a doratura.")
    if "pesce" in ingredienti:
        preparazione.append("Condiamo il pesce con sale, pepe e limone, e lo cuociamo in padella con un filo d'olio per circa 4-5 minuti per lato, oppure al forno a 180°C per 15 minuti.")
    if "radicchio" in ingredienti or "verdure" in ingredienti or "zucchine" in ingredienti:
        preparazione.append("Tagliamo il radicchio o le verdure a strisce sottili e le saltiamo in padella con un filo d'olio d'oliva per circa 5 minuti, fino a renderle tenere ma croccanti.")
    if "avocado" in ingredienti:
        preparazione.append("Sbucciamo l'avocado, lo schiacciamo con una forchetta e lo condiamo con sale, succo di limone e pepe per ottenere una crema morbida.")
    if "noci" in ingredienti:
        preparazione.append("Le noci vengono tostate in padella per 2-3 minuti, mescolandole continuamente per esaltarne il sapore e renderle croccanti.")

    preparazione.append(f"Impiattiamo il tutto con cura e serviamo caldo. (Tempo totale: {tempo_totale} minuti)")
    preparazione.append("Buon appetito! 🍽️")
    
    valori = {
        "Calorie": random.randint(400, 800),
        "Proteine": random.randint(30, 60),
        "Grassi": random.randint(10, 30),
        "Carboidrati": random.randint(40, 100),
        "Fibre": random.randint(5, 15),
        "Zuccheri": random.randint(2, 10),
        "Sale": round(random.uniform(0.5, 2), 1)
    }
    
    return titolo, difficolta, tempo_preparazione, tempo_cottura, tempo_totale, quantita, preparazione, valori

def genera_ricetta_variante(ingredienti):
    # Genera la ricetta base
    titolo, difficolta, tempo_preparazione, tempo_cottura, tempo_totale, quantita, preparazione_base, valori = genera_ricetta_base(ingredienti)
    # Crea una variante aggiungendo passaggi extra, senza rimuovere quelli base
    preparazione_variante = preparazione_base.copy()
    preparazione_variante.append("Come variante, dopo aver scolato la pasta, la facciamo saltare in padella per 2 minuti con un filo d'olio e un pizzico di pepe nero per insaporirla ulteriormente.")
    preparazione_variante.append("Infine, aggiungiamo un cucchiaino di miele per un tocco di dolcezza naturale e spolveriamo con cannella per un aroma unico.")
    titolo_variante = f"{titolo} (Variante con Tocco Magico)"
    
    return titolo_variante, difficolta, tempo_preparazione, tempo_cottura, tempo_totale, quantita, preparazione_variante, valori

# Interfaccia Streamlit
st.title("🥗 Generatore di Ricette High-Protein per Atleti")
st.write("Inserisci gli ingredienti che hai a disposizione:")

ingredienti_input = st.text_input("🔍 Inserisci gli ingredienti (separati da virgola)")

modalita = st.radio("Scegli la modalità:", ("Ricetta Base", "Variante con Tocco Magico"))

if st.button("🔎 Genera Ricetta"):
    if ingredienti_input:
        lista_ingredienti = [i.strip().lower() for i in ingredienti_input.split(",")]
        if modalita == "Ricetta Base":
            titolo, difficolta, tp, tc, tt, quantita, preparazione, valori = genera_ricetta_base(lista_ingredienti)
        else:
            titolo, difficolta, tp, tc, tt, quantita, preparazione, valori = genera_ricetta_variante(lista_ingredienti)
        
        st.subheader(f"🍽️ **{titolo}**")
        st.write(f"⏳ Preparazione: {tp} min | 🔥 Cottura: {tc} min | ⭐ Difficoltà: {difficolta}")
        st.subheader("📌 Ingredienti:")
        for ingr, q in quantita.items():
            st.write(f"- {ingr.capitalize()}: {q}")
        st.subheader("📌 Preparazione:")
        for passo in preparazione:
            st.write(passo)
        st.subheader("🔥 Valori Nutrizionali:")
        for chiave, valore in valori.items():
            st.write(f"- {chiave}: {valore}")
    else:
        st.warning("Inserisci gli ingredienti per generare una ricetta.")
