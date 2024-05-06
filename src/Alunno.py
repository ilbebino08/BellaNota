import Funzioni                                                                             # Importa i moduli necessari
import csv

class Alunno:
    def __init__(self, parent_dir, nome, cognome):
        self.parent_dir = parent_dir
        self.nome       = nome
        self.cognome    = cognome

    def __aggiungiVoto(self):
        print("Inserisci la data (formato: dd/mm/yyyy):")
        data = input(" ")                                                                   # Richiede di inserire la data del voto

        if not Funzioni.check_data(data):                                                   # Verifica se la data inserita è valida
            print("Data non valida. Riprova.")
            return                                                                          # Se la data non è valida, interrompi la funzione

        print("Inserisci il tipo di compito (p = pratico, o = orale):")
        tipo = input(" ")                                                                   # Richiede di inserire il tipo di compito

        if tipo not in ["p", "o"]:                                                          # Verifica se il tipo di compito inserito è valido
            print("Tipo di compito non valido. Riprova.")
            return                                                                          # Se il tipo di compito non è valido, interrompi la funzione

        while True:
            voto = input("Inserire voto: ")                                                 # Richiede all'utente di inserire il voto

            if not (2 <= float(voto) <= 10):                                                # Verifica se il voto è un numero compreso tra 2 e 10
                print("Impossibile impostare un voto maggiore di 10 e minore di 2.")
                return                                                                      # Se il voto non è valido, interrompi la funzione

            with open(self.parent_dir, 'a', newline='') as file:
                writer = csv.writer(file)                                                   # Crea un oggetto writer per scrivere nel file CSV
                writer.writerow([voto, data, tipo])                                         # Scrive una nuova riga nel file con il voto, data e tipo compito
                print("Voto inserito correttamente")
            break                                                                           # Interrompi il ciclo while e termina la funzione


    def __vediMedia(self, metodo):
        numeri = []                                                                         # Crea una lista vuota per memorizzare i voti estratti dal file CSV

        with open(self.parent_dir, 'r') as file:                                            # Apre il file CSV in modalità lettura
            reader = csv.reader(file)                                                       # Crea un oggetto reader per leggere il contenuto del file CSV
            for row in reader:
                if metodo == "g":                                                           # Se il metodo è "g" considera tutti i voti numerici
                    if len(row) > 0:                                                        # Controlla che la riga non sia vuota
                        numero = row[0]                                                     # Legge il valore del voto
                        if numero.isdigit():                                                # Verifica se il voto è un numero
                            numeri.append(int(numero))                                      # Aggiunge il voto alla lista dei voti

                elif metodo == "o":                                                         # Se il metodo è "o" considera solo i voti orali
                    if len(row) > 0 and row[2] != "p":                                      # Controlla che la riga non sia vuota e che il tipo di compito sia "o"
                        numero = row[0]
                        if numero.isdigit():
                            numeri.append(int(numero))
                elif metodo == "p":                                                         # Se il metodo è "p" considera solo i voti pratici
                    if len(row) > 0 and row[2] != "o":                                      # Controlla che la riga non sia vuota e che il tipo di compito sia "p"
                        numero = row[0]
                        if numero.isdigit():
                            numeri.append(int(numero))

        if len(numeri) > 0:                                                                 # Se ci sono voti nella lista numeri
            media = sum(numeri) / len(numeri)                                               # Calcola la media dei voti
            media = round(media, 2)                                                         # Arrotonda la media a due cifre decimali
            if metodo == "g":                                                               # Se il metodo è "g", stampa la media generale dell'alunn*
                print(f"La media dell'alunn* {self.cognome} {self.nome} è {media}")
            elif metodo == "o":                                                             # Se il metodo è "o", stampa la media orale dell'alunn*
                print(f"La media orale dell'alunn* {self.cognome} {self.nome} è {media}")
            elif metodo == "p":                                                             # Se il metodo è "p", stampia la media pratica dell'alunn*
                print(f"La media pratica dell'alunn* {self.cognome} {self.nome} è {media}")
        else:                                                                               # Se la lista numeri è vuota, stampa il messaggio appropriato.
            if metodo == "g":
                print(f"L'alunn* {self.cognome} {self.nome} non ha voti")
            elif metodo == "o":
                print(f"L'alunn* {self.cognome} {self.nome} non ha voti orali")
            elif metodo == "p":
                print(f"L'alunn* {self.cognome} {self.nome} non ha voti pratici")


    def __listaVoti(self):
        voti = []                                                                           # Crea un vettore vuoto per memorizzare i voti

        with open(self.parent_dir, 'r') as file:                                            # Apre il file dell'alunn* in modalità lettura
            reader = csv.reader(file)                                                       # Crea un oggetto reader per leggere il contenuto del file CSV
            for riga in reader:                 
                if len(riga) >= 3:                                                          # Controlla che ci siano almeno 3 colonne nella riga
                    colonna0 = riga[0]                                                      # Legge i valori delle colonne
                    colonna1 = riga[1]
                    colonna2 = riga[2]

                    tipo_compito = "Orale" if colonna2.lower() == "o" else "Pratico"        # Determina il tipo di compito
                    voti.append((colonna0, colonna1, tipo_compito))

        return voti                                                                         # Restituisce la lista contenente i voti letti dal file CSV


    def menuAlunno(self):
        while True:
            Funzioni.start()                                                                # Chiama la funzione start() del modulo Funzioni

            print("")                                                                       # Mostra le opzioni tra cui scegliere
            print("1 - Aggiungere un voto")
            print("2 - Vedere la media generale")
            print("3 - Vedere la media pratica")
            print("4 - Vedere la media orale")
            print("5 - Vedere la lista dei voti")
            print("6 - Uscire dal profilo alunn*")

            comando = input(" " + self.nome + " " + self.cognome + " >> ")                  # Richiede all'utente di scegliere un opzione

            print("")

            if comando == "1":                                                              # Chiama la funzione __aggiungiVoto() 
                self.__aggiungiVoto()
            elif comando == "2":                                                            # Chiama la funzione __vediMedia() con argomento "g" per richiedere la media di tutti i voti
                self.__vediMedia("g")  
            elif comando == "3":                                                            # Chiama la funzione __vediMedia() con argomento "p" per richiedere la media di tutti i voti pratici
                self.__vediMedia("p")
            elif comando == "4":                                                            # Chiama la funzione __vediMedia() con argomento "o" per richiedere la media di tutti i voti orali
                self.__vediMedia("o")
            elif comando == "5":                                                            # Chiama la funzione __listaVoti() per richiedere la media di tutti i voti
                voti = self.__listaVoti()
                for voto in voti:
                    colonna0, colonna1, tipo_compito = voto
                    print(f"{colonna0} {colonna1} {tipo_compito}")
            elif comando == "6":                                                            # Ferma la funzione e fa uscire dal profilo alunn*
                print("Sei uscito dal profilo alunn*")
                break
            else:                                                                           # Comunica se il comando non è stato riconosciuto
                print("Comando non riconosciuto.")
