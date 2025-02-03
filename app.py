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
def genera_ricetta(ingredienti):
    # Titolo: si basa esclusivamente sugli ingredienti inseriti
    titolo_ricetta = f"Ricetta con {', '.join(ingredienti).capitalize()}"
    
    # Tempi: generati casualmente per preparazione e cottura
    tempo_preparazione = random.randint(5, 15)
    tempo_cottura = random.randint(10, 30)
    tempo_totale = tempo_preparazione + tempo_cottura
    difficolta = calcola_difficolta(tempo_totale)
    
    # Generazione delle quantità per ogni ingrediente
    quantita = {ingrediente: f"{random.randint(50, 300)}g" for ingrediente in ingredienti}

    # Creazione di un procedimento coerente e dettagliato
    preparazione = []
    preparazione.append(f"Per questa ricetta utilizzeremo {', '.join(ingredienti)}. Assicuriamoci di avere tutto pronto prima di iniziare.")
    
    # Esempi di passaggi per ingredienti specifici:
    if "spaghetti" in ingredienti or "pasta" in ingredienti:
        preparazione.append("Portiamo a ebollizione una pentola con abbondante acqua salata. Aggiungiamo la pasta e cuociamo per il tempo indicato sulla confezione, mescolando occasionalmente.")
    if "riso" in ingredienti:
        preparazione.append("In un pentolino, portiamo a ebollizione 500 ml di acqua salata. Aggiungiamo il riso e lo cuociamo a fuoco medio per circa 12 minuti, mescolando di tanto in tanto.")
    if "ragù pomodoro" in ingredienti:
        preparazione.append("In una padella, scaldiamo un filo d'olio e aggiungiamo il ragù di pomodoro. Lasciamo cuocere a fuoco basso per circa 10 minuti, mescolando per far amalgamare i sapori.")
    if "guanciale" in ingredienti:
        preparazione.append("Tagliamo il guanciale a striscioline sottili e lo facciamo rosolare in una padella a fuoco medio, senza aggiungere altro olio, finché non diventa croccante. Lo mettiamo da parte.")
    if "carne" in ingredienti:
        preparazione.append("Tagliamo la carne a cubetti, condiscendola con sale, pepe e spezie, e la cuociamo in padella con un filo d'olio per circa 7-10 minuti fino a doratura.")
    if "pesce" in ingredienti:
        preparazione.append("Condiamo il pesce con sale, pepe e limone, quindi lo cuociamo in padella con un filo d'olio per 4-5 minuti per lato o al forno a 180°C per 15 minuti.")
    if "radicchio" in ingredienti or "verdure" in ingredienti or "zucchine" in ingredienti:
        preparazione.append("Tagliamo il radicchio (o le verdure) a strisce sottili e le saltiamo in padella con un filo d'olio d'oliva per 5 minuti, fino a quando saranno tenere ma ancora croccanti.")
    if "avocado" in ingredienti:
        preparazione.append("Sbucciamo l'avocado, lo schiacciamo con una forchetta e lo condiamo con un pizzico di sale, succo di limone e pepe, ottenendo una crema morbida.")
    if "noci" in ingredienti:
        preparazione.append("Tostiamo leggermente le noci in padella per 2-3 minuti, mescolandole continuamente per esaltarne il sapore e renderle croccanti.")
    if "pane" in ingredienti:
        preparazione.append("Tostiamo il pane in forno o in padella fino a renderlo dorato, per un effetto croccante.")
    if "pesto" in ingredienti:
        preparazione.append("Se presente, aggiungiamo un cucchiaio di pesto sopra il piatto finito per un tocco aromatico.")

    # Concludiamo il procedimento
    preparazione.append(f"Impiattiamo il tutto con cura e serviamo caldo. (Tempo totale: {tempo_totale} minuti)")
    preparazione.append("Buon appetito! 🍽️")
    
    # Generazione dei valori nutrizionali (valori realistici per una ricetta high-protein)
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

# Funzione per generare la variante della ricetta con un tocco magico
def genera_ricetta_migliorata(ingredienti):
    # Genera la ricetta base e poi crea una variante modificata
    titolo, difficolta, tempo_preparazione, tempo_cottura, tempo_totale, quantita, preparazione, valori = genera_ricetta(ingredienti)
    
    # Creiamo un titolo di variante
    titolo_variante = f"{titolo} (Variante con Tocco Magico)"
    
    # Creiamo un nuovo procedimento variante, modificando i passaggi per dare un tocco diverso
    preparazione_variante = []
    preparazione_variante.append(f"Iniziamo preparando {', '.join(ingredienti)}. Disponi gli ingredienti sul piano di lavoro, pronti per essere trasformati in un piatto unico.")
    
    # Se la ricetta contiene carne, la variante la marina e la cuoce in forno
    if "carne" in ingredienti:
        preparazione_variante.append("Marina la carne con rosmarino, limone e pepe per 15 minuti. Quindi, disponila in una teglia e cuocila in forno a 180°C per circa 20 minuti, fino a ottenere una doratura perfetta.")
    
    # Se contiene pesce, usa un metodo diverso
    if "pesce" in ingredienti:
        preparazione_variante.append("Condisci il pesce con limone, sale e pepe. Cuoci il pesce in forno a 180°C per 15 minuti, in modo da mantenere la sua delicatezza.")
    
    # Per avocado, crea una crema diversa
    if "avocado" in ingredienti:
        preparazione_variante.append("Prepara una crema di avocado frullandolo con succo di lime, un pizzico di peperoncino e un filo d'olio extra vergine.")
    
    # Per radicchio o verdure, proponi una cottura alla griglia
    if "radicchio" in ingredienti or "verdure" in ingredienti:
        preparazione_variante.append("Griglia il radicchio o le verdure su una piastra ben calda per 5 minuti, per ottenere un sapore intenso e leggermente affumicato.")
    
    # Per noci, proponi di preparare una salsa
    if "noci" in ingredienti:
        preparazione_variante.append("Tosta le noci in padella per 3 minuti, poi frullale con un cucchiaino di olio e un pizzico di cannella per creare una salsa rustica.")
    
    # Per pasta o riso, cuoci normalmente e poi salta in padella
    if "spaghetti" in ingredienti or "pasta" in ingredienti:
        preparazione_variante.append("Cuoci la pasta in abbondante acqua salata al dente, scolala e saltala in padella con un filo d'olio e un pizzico di pepe nero per insaporirla ulteriormente.")
    if "riso" in ingredienti:
        preparazione_variante.append("Cuoci il riso in acqua salata e, una volta scolato, mantecalo in padella con un cucchiaio di burro e una spolverata di pepe nero.")

    # Unione finale dei componenti
    preparazione_variante.append("Unisci tutti i componenti in un piatto, aggiungi un cucchiaino di miele per un tocco di dolcezza naturale e spolvera con un pizzico di cannella per un aroma unico.")
    preparazione_variante.append(f"Impiatta con cura e servi caldo. (Tempo totale: {tempo_totale} minuti)")
    preparazione_variante.append("Buon appetito! 🍽️")
    
    return titolo_variante, difficolta, tempo_preparazione, tempo_cottura, tempo_totale, quantita, preparazione_variante, valori

# Streamlit UI
st.title("🥗 Generatore di Ricette High-Protein per Atleti")
st.write("Inserisci gli ingredienti che hai a disposizione:")

ingredienti_input = st.text_input("🔍 Inserisci gli ingredienti (separati da virgola)")

if st.button("🔎 Genera Ricetta"):
    if ingredienti_input:
        lista_ingredienti = [i.strip().lower() for i in ingredienti_input.split(",")]
        
        # Genera la ricetta base
        titolo_base, difficolta_base, tempo_preparazione_base, tempo_cottura_base, tempo_totale_base, quantita_base, istruzioni_base, valori_base = genera_ricetta(lista_ingredienti)
        
        # Genera la variante migliorata
        titolo_variante, difficolta_variante, tempo_preparazione_variante, tempo_cottura_variante, tempo_totale_variante, quantita_variante, istruzioni_variante, valori_variante = genera_ricetta_migliorata(lista_ingredienti)
        
        # Mostra la ricetta base
        st.subheader(f"🍽️ **{titolo_base}**")
        st.write(f"⏳ Preparazione: {tempo_preparazione_base} min | 🔥 Cottura: {tempo_cottura_base} min | ⭐ Difficoltà: {difficolta_base}")
        st.subheader("📌 Ingredienti:")
        for ingrediente, quant in quantita_base.items():
            st.write(f"- {ingrediente.capitalize()}: {quant}")
        st.subheader("📌 Preparazione:")
        for passo in istruzioni_base:
            st.write(passo)
        st.subheader("🔥 Valori Nutrizionali:")
        for chiave, valore in valori_base.items():
            st.write(f"- {chiave}: {valore}")

        # Mostra la variante migliorata
        st.subheader(f"✨ **{titolo_variante} (Variante con Tocco Magico)**")
        st.write("Ecco la variante che aggiunge un tocco speciale per esaltare i sapori:")
        for passo in istruzioni_variante:
            st.write(passo)
            
    else:
        st.warning("Inserisci gli ingredienti per generare una ricetta.")

