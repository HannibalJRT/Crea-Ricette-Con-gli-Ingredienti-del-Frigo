import streamlit as st
import random

# Funzione per calcolare la difficoltà
def calcola_difficolta(tempo_totale):
    if tempo_totale < 15:
        return "Facile"
    elif 15 <= tempo_totale <= 30:
        return "Medio"
    else:
        return "Difficile"

# Funzione per valutare la plausibilità della combinazione di ingredienti
def ingredienti_validi(ingredienti):
    # Regola più ampia: consideriamo validi sia gli ingredienti di base che le combinazioni dolci
    ingredienti_di_base = {"pasta", "riso", "pane", "carne", "pesce", "uova", "latte", "farina", "zucchero", "verdure"}
    ingredienti_dolci = {"banana", "fichi", "yogurt", "miele", "cioccolato", "avena", "fragole"}
    ingredienti_non_adatti = {"radicchio", "aglio", "cipolla"}

    matching_base = [i for i in ingredienti if i in ingredienti_di_base]
    matching_dolci = [i for i in ingredienti if i in ingredienti_dolci]
    matching_non_adatti = [i for i in ingredienti if i in ingredienti_non_adatti]

    # Se ci sono ingredienti non adatti, avvisiamo
    if matching_non_adatti:
        return False, matching_non_adatti
    # È valido se c'è almeno un ingrediente di base o almeno una combinazione dolce riconosciuta
    return (len(matching_base) > 0 or len(matching_dolci) > 0), None

# Funzione per generare la ricetta base
def genera_ricetta_base(ingredienti):
    titolo = f"Ricetta con {', '.join(ingredienti).capitalize()}"
    tempo_preparazione = random.randint(5, 15)
    tempo_cottura = random.randint(10, 30)
    tempo_totale = tempo_preparazione + tempo_cottura
    difficolta = calcola_difficolta(tempo_totale)
    quantita = {ingr: f"{random.randint(50,300)}g" for ingr in ingredienti}

    # Iniziamo a preparare i passaggi
    preparazione = [f"Per questa ricetta utilizzeremo {', '.join(ingredienti)}. Assicuriamoci di avere tutto pronto prima di iniziare."]

    for ingr in ingredienti:
        if "avena" in ingr:
            preparazione.append("Cuoci l’avena con 250ml di latte o acqua a fuoco basso fino a ottenere una consistenza cremosa.")
        elif "banana" in ingr:
            preparazione.append("Sbuccia la banana e schiacciala con una forchetta fino a ottenere una purea liscia. Incorporala nel composto.")
        elif "fichi" in ingr:
            preparazione.append("Taglia i fichi in pezzi e falli caramellare in padella con un cucchiaino di miele per un tocco dolce.")
        elif "yogurt" in ingr:
            preparazione.append("Mescola lo yogurt con un pizzico di zucchero e un po’ di succo di limone per una crema fresca.")
        elif "frutta secca" in ingr:
            preparazione.append("Trita grossolanamente la frutta secca e tostala in padella per 2-3 minuti per esaltarne il sapore.")
        elif "noci" in ingr:
            preparazione.append("Tosta le noci leggermente in padella per intensificarne l’aroma.")
        elif "pane" in ingr:
            preparazione.append("Tosta il pane in forno a 180°C per 5 minuti, oppure doralo in padella con un filo d’olio.")
        elif "ricotta" in ingr:
            preparazione.append("Mescola la ricotta con un pizzico di sale e pepe per una crema morbida e gustosa.")
        elif "belga" in ingr:
            preparazione.append("Taglia il belga a strisce e saltalo in padella con un filo d’olio d’oliva per 3-4 minuti.")
        elif "grana" in ingr:
            preparazione.append("Grattugia finemente il grana e spargilo sul piatto finito.")
        else:
            preparazione.append(f"Prepara {ingr} a tuo piacere, quindi incorporalo nel piatto finale.")

    # Passaggio finale
    preparazione.append("Impiattiamo il tutto con cura e serviamo caldo.")
    preparazione.append(f"Tempo totale: {tempo_totale} minuti.")

    # Generazione valori nutrizionali
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

# Funzione per generare la variante
def genera_ricetta_variante(ingredienti):
    titolo, difficolta, tempo_preparazione, tempo_cottura, tempo_totale, quantita, preparazione_base, valori = genera_ricetta_base(ingredienti)
    preparazione_variante = preparazione_base.copy()
    # Aggiungere un tocco magico nella variante
    preparazione_variante.append("VARIANTE: Spolvera con cannella e aggiungi un cucchiaino di miele per una dolcezza naturale.")
    preparazione_variante.append("Oppure aggiungi una manciata di cioccolato fondente tritato per un tocco goloso.")
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
        
        valido, non_adatti = ingredienti_validi(lista_ingredienti)
        if valido:
            # Generare la ricetta in base alla modalità
            if modalita == "Ricetta Base":
                titolo, difficolta, tp, tc, tt, quantita, preparazione, valori = genera_ricetta_base(lista_ingredienti)
            else:
                titolo, difficolta, tp, tc, tt, quantita, preparazione, valori = genera_ricetta_variante(lista_ingredienti)
            
            # Mostrare la ricetta
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
        elif non_adatti:
            # Ingredienti non adatti trovati
            st.warning(f"Attenzione! Questi ingredienti non sembrano combinarsi bene: {', '.join(non_adatti)}. Prova a sostituirli o rimuoverli.")
        else:
            # Nessuna ricetta sensata trovata
            st.warning("Sembra che questi ingredienti non si combinino facilmente in una ricetta. Ti consiglio di provare con un set di ingredienti più comuni oppure aggiungere un ingrediente di base come riso, pasta o un’altra fonte di proteine.")
    else:
        st.warning("Inserisci gli ingredienti per generare una ricetta.")

