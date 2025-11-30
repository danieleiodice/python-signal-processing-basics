import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# 1. PREPARAZIONE ASSE TEMPORALE
# ------------------------------

durata = 10  # durata totale della simulazione in secondi

# L'utente sceglie quanti campioni usare.
# Più sono i campioni, più il segnale sarà dettagliato.
n_campioni = int(input("Inserire il numero di campioni: "))

# Genero un array di tempi da 0 a 'durata', composto da 'n_campioni' punti.
tempo = np.linspace(0, durata, n_campioni)


# ------------------------------
# 2. GENERAZIONE SEGNALE PULITO
# ------------------------------

# L'utente sceglie l'ampiezza della sinusoide.
ampiezza = float(input("Inserire l'ampiezza del segnale [m]: "))

# L'utente sceglie la frequenza della sinusoide.
frequenza = float(input("Inserire la frequenza del segnale [Hz]: "))

# Creo la sinusoide pulita (senza rumore).
# Formula: A * sin(2πft)
segnale_pulito = ampiezza * np.sin(2 * np.pi * frequenza * tempo)


# ------------------------------
# 3. GENERAZIONE DEL RUMORE
# ------------------------------

# L'utente decide quanto deve essere forte il rumore (deviazione standard).
deviazione_standard = float(input("Inserire la deviazione standard: "))

# Media del rumore (bias). Può essere 0 oppure un valore impostato dall'utente.
media = float(input("Inserire la media: "))

# Genero rumore gaussiano con media e deviazione standard specificati.
# Ogni campione è indipendente dagli altri.
rumore = np.random.normal(media, deviazione_standard, n_campioni)

# Il segnale reale è il segnale pulito + la componente di rumore.
segnale_rumoroso = segnale_pulito + rumore


# ------------------------------
# 4. MEDIA MOBILE (FILTRO)
# ------------------------------

# Lunghezza della finestra per la media mobile.
# Una finestra più larga = più filtraggio ma anche perdita di dettagli.
finestra = 20

# Creo un array vuoto che conterrà il segnale filtrato.
# Ha la stessa dimensione del segnale rumoroso.
segnale_filtrato = np.zeros_like(segnale_rumoroso)

# Ciclo su tutti i campioni per calcolare la media mobile centrata.
for i in range(n_campioni):

    # Calcolo i limiti della finestra per evitare di uscire dai bordi dell'array.
    start = max(0, i - finestra // 2)
    end = min(n_campioni, i + finestra // 2 + 1)

    # Calcolo la media del tratto selezionato del segnale rumoroso.
    segnale_filtrato[i] = np.mean(segnale_rumoroso[start:end])


# ------------------------------
# 5. PLOT DEI RISULTATI
# ------------------------------

plt.figure(figsize=(10, 5))

# Mostro il segnale rumoroso in rosso
plt.plot(segnale_rumoroso, label='Segnale rumoroso', color='red')

# Mostro il segnale filtrato in blu
plt.plot(segnale_filtrato, label='Segnale filtrato', color='blue')

plt.xlabel('Campioni')
plt.ylabel('Ampiezza')
plt.title('Segnale Rumoroso Vs. Segnale Filtrato')
plt.legend()
plt.grid(True)
plt.show()