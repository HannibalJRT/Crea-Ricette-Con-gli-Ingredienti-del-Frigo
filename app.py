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

# Funzione per validare la combinazione degli ingredienti
def ingredienti_validi(ingredienti):
    ingredienti_di_base = {"pasta", "riso", "pane", "carne", "pesce", "uova", "latte", "farina", "zucchero", "verdure"}
    ingredienti_dolci = {"banana", "fichi", "yogurt", "miele", "cioccolato", "avena", "fragole"}
    ingredienti_non_adatti = {"radicchio"}

    matching_base = [i for i in ingredienti if i in ingredienti_di_base]
    matching_dolci = [i for i in ingredienti if i in ingredienti_dolci]
    matching_non_adatti = [i for i in ingredienti if i in ingredienti_non_adatti]

    if matching_non_adatti:
        return False, matching_non_adatti
    return (len(matching_base) > 0 or len(matching_dolci) > 0), None

# Funzione per generare la ricetta base
def genera_ricetta_base(ingredienti):
    titolo = f"Ricetta con {', '.join(ingredienti).capitalize()}"
    tempo_preparazione = random.randint(5, 15)
    tempo_cottura = random.randint(10, 30)
    tempo_totale = tempo_preparazione + tempo_cottura
    difficolta = calcola_difficolta(tempo_totale)
    quantita = {ingr: f"{random.randint(50,300)}g" for ingr in ingredienti}

    preparazione = [f"Per questa ricetta utilizzeremo {', '.join(ingredienti)}. Ecco il procedimento:"]

    for ingr in ingredienti:
        if ingr == "avocado":
            preparazione.append("Taglia l’avocado a metà, rimuovi il nocciolo, e affetta la polpa. Condisci con succo di limone e un pizzico di sale. Lascia da parte.")
        elif ingr == "uova":
            preparazione.append("Sbatti le uova con un pizzico di sale e pepe. Scalda una padella antiaderente e cuoci le uova strapazzate a fuoco medio per 3-5 minuti, mescolando frequentemente.")
        elif ingr == "belga":
            preparazione.append("Taglia il belga a strisce sottili. Scalda una padella con un filo d’olio d’oliva, aggiungi il belga e saltalo per 3-4 minuti, finché diventa tenero ma ancora croccante.")
        elif ingr == "noci":
            preparazione.append("Tosta le noci in padella per 2-3 minuti a fuoco medio, mescolando spesso. Questo intensifica il loro sapore e le rende croccanti.")
        elif ingr == "pomodorini":
            preparazione.append("Lava i pomodorini e tagliali a metà. Saltali in padella con un filo d’olio d’oliva per circa 5 minuti, fino a quando rilasciano il loro succo.")
        else:
            preparazione.append(f"Prepara {ingr} come preferisci e incorpora nel piatto.")

    preparazione.append("Quando tutti gli ingredienti sono pronti, assembla il piatto. Disponi l’avocado affettato come base, aggiungi le uova strapazzate, il belga saltato, le noci tostate e i pomodorini caldi sopra. Aggiungi un filo d’olio a crudo e, se preferisci, un pizzico di pepe nero macinato fresco.")
    preparazione.append(f"Tempo totale di preparazione: {tempo_totale} minuti.")

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
    preparazione_variante.append("VARIANTE: Aggiungi un pizzico di peperoncino e una manciata di parmigiano grattugiato per un sapore più intenso.")
    return f"{titolo} (Variante)", difficolta, tempo_preparazione, tempo_cottura, tempo_totale, quantita, preparazione_variante, valori

# Interfaccia Streamlit migliorata
st.title("🥗 Generatore di Ricette High-Protein")
st.write("Inserisci gli ingredienti che hai a disposizione per generare una ricetta adatta a uno stile di vita attivo e bilanciato.")

ingredienti_input = st.text_input("🔍 Inserisci gli ingredienti (separati da virgola)")
modalita = st.radio("Scegli la modalità:", ("Ricetta Base", "Variante con Tocco Magico"))

if st.button("🔎 Genera Ricetta"):
    if ingredienti_input:
        lista_ingredienti = [i.strip().lower() for i in ingredienti_input.split(",")]
        valido, non_adatti = ingredienti_validi(lista_ingredienti)
        if valido:
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
        elif non_adatti:
            st.warning(f"Attenzione! Questi ingredienti non sembrano combinarsi bene: {', '.join(non_adatti)}. Prova a sostituirli o rimuoverli.")
        else:
            st.warning("Sembra che questi ingredienti non si combinino facilmente in una ricetta. Ti consiglio di provare con un set di ingredienti più comuni.")
    else:
        st.warning("Inserisci gli ingredienti per generare una ricetta.")
