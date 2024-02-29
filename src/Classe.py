import Funzioni
import Alunno
import os
import csv

class Classe:
    def __init__(self, nomeClasse, parent_dir):
        self.parent_dir = parent_dir
        self.nomeClasse = nomeClasse
        self.directory = os.path.join(parent_dir, nomeClasse)

    def __selezionaAlunno(self):                                                                    # Seleziona un profilo alunn* e avvia il menu dell'alunno
        while True:
            print("Inserire nome dell'alunn*")                                                      # Richiede di inserire il nome dell'alunn* e mette le iniziali maiuscole
            nome = input(" ").capitalize()
            print("Inserire cognome dell'alunn*")                                                   # Richiede all'utente di inserire il cognome dell'alunn* e mette le iniziali maiuscole
            cognome = input(" ").capitalize()

            nome_file = f"{cognome}{nome}.csv"                                                      # Costruisce il nome del file del profilo dell'alunn*
            filepath = os.path.join(self.directory, nome_file)                                      # Crea il percorso completo del file

            if os.path.exists(filepath):                                                            # Controlla se il file del profilo esiste
                Alunno.menuAlunno(filepath, nome, cognome)                                          # Avvia il menu dell'alunno per il profilo selezionato
                break
            print(f"Il profilo dell'alunn* {cognome} {nome} non esiste")                            # Stampa un messaggio di errore se il profilo non esiste


    def __creaProfilo(self):                                                                        # Crea un profilo alunn*
        print("Inserire il nome dell'alunn*")                                                       # Richiede all'utente di inserire il nome dell'alunn* e mette le iniziali maiuscole
        nome = input(" ").capitalize()
        print("Inserire il cognome dell'alunn*")                                                    # Richiede all'utente di inserire il cognome dell'alunn* e mette le iniziali maiuscole
        cognome = input(" ").capitalize()

        while True:
            print(f"Confermare la creazione dell'alunn* {cognome} {nome}? S/n")                     # Chiede all'utente di confermare la creazione del profilo
            conferma = input("").upper()                                                            # Legge l'input e lo converte in maiuscolo
            if conferma == "S":                                                                     # Se l'utente conferma la creazione del profilo
                nome_file = f"{cognome}{nome}.csv"                                                  # Costruisce il nome del file del profilo dell'alunn*
                filepath = os.path.join(self.directory, nome_file)                                  # Crea il percorso completo del file

                if os.path.exists(filepath):                                                        # Controlla se il profilo esiste già
                    print(f"L'alunn* {cognome} {nome} esiste già")                                  # Stampa un messaggio di errore se esiste già
                else:                                                                               # Se il profilo non esiste
                    with open(filepath, 'w'):                                                       # Crea il file del profilo vuoto
                        pass
                    print(f"Il profilo dell'alunn* {cognome} {nome} è stato creato correttamente")  # Stampa un messaggio di conferma per la creazione del profilo
                break                                                                               # Esce dal ciclo dopo la creazione del profilo
              
            elif conferma == "N":                                                                   # Se l'utente annulla la creazione del profilo.
                print("Creazione annullata")                                                        # Stampa un messaggio per confermare l'annullamento
                break                                                                               # Esce dal ciclo senza creare il profilo
              
            else:                                                                                   # Se l'utente inserisce un comando sconosciuto
                print("Comando sconosciuto")                                                        # Stampa un messaggio di errore


    def __elencaAlunni(self):                                                                       # Visualizza la lista degli alunni nella classe
        files = os.listdir(self.directory)                                                          # Ottiene la lista di tutti i file nella directory della classe
        csv_files = [file for file in files if file.endswith('.csv')]                               # Filtra solo i file CSV

        if len(csv_files) == 0:                                                                     # Se non ci sono file CSV
            print("Non hai nessun profilo alunn* in questa classe")                                 # Stampa un messaggio informativo
            return

        print("I nomi dei tuoi alunn* sono:")                                                       # Stampa l'intestazione per la lista dei profili degli alunni
        for file in csv_files:
            nome_formattato = Funzioni.format_file_name(file)                                       # Utilizza la funzione "format_file_name" per formattare il nome del file in modo leggibile
            print(nome_formattato)                                                                  # Stampa il nome formattato del profilo dell'alunno


    def __gMedia(self):                                                                             # Calcola e visualizza la media generale di tutta la classe
        media_generale = Funzioni.mediacl(self.directory, "g")                                      # Chiama la funzione "mediacl"
        if media_generale is not None:                                                              # Se la media generale è stata calcolata correttamente
            print(f"La media generale della classe {self.nomeClasse} è: {media_generale}")          # Stampa la media generale calcolata
            return

        print("Nessun voto presente per calcolare la media generale")                               # Stampa un messaggio informativo se non ci sono voti per calcolare la media generale


    def __pMedia(self):                                                                             # Calcola e visualizza la media pratica di tutta la classe
        media_pratica = Funzioni.mediacl(self.directory, "p")                                       # Chiama la funzione "mediacl"
        if media_pratica is not None:                                                               # Se la media pratica è stata calcolata correttamente
            print(f"La media pratica della classe {self.nomeClasse} è: {media_pratica}")            # Stampa la media pratica calcolata
            return

        print("Nessun voto presente per calcolare la media pratica")                                # Stampa un messaggio informativo se non ci sono voti per calcolare la media pratica

    def __oMedia(self):                                                                             # Calcola e visualizza la media orale di tutta la classe
        media_orale = Funzioni.mediacl(self.directory, "o")                                         # Chiama la funzione "mediacl"
        if media_orale is not None:                                                                 # Se la media orale è stata calcolata correttamente
            print(f"La media orale della classe {self.nomeClasse} è: {media_orale}")                # Stampa la media orale calcolata
            return

        print("Nessun voto presente per calcolare la media orale")                                  # Stampa un messaggio informativo se non ci sono voti per calcolare la media orale

    def __nCompito(self):                                                                           # Aggiunge un compito di classe
        print("Inserisci la data (formato: dd/mm/yyyy):")                                           # Richiede di inserire la data del compito
        data = input(" ")                                                                           # Legge l'input dell'utente riguardante la data del compito

        if not Funzioni.check_data(data):                                                           # Verifica se la data è valida
            print("Data non valida. Riprova.")                                                      # Stampa un messaggio di errore se la data non è valida
            return

        print("Inserisci il tipo di compito (p = pratico, o = orale):")                             # Richiede di inserire il tipo di compito
        tipo = input(" ")                                                                           # Legge l'input riguardante il tipo di compito

        if tipo not in ["p", "o"]:                                                                  # Controlla se il tipo di compito inserito dall'utente è valido
            print("Tipo di compito non valido. Riprova.")                                           # Stampa un messaggio di errore se il tipo di compito non è valido
            return                                                                                  # Esce dalla funzione

        Funzioni.compito(self.directory, data, tipo)                                                # Se il tipo di compito inserito è valido, chiama la funzione "compito" del modulo "Funzioni" per aggiungere il compito alla classe


    def __eliminaAlunno(self):                                                                          # Elimina un profilo alunn* dalla classe
        print("Inserire nome dell'alunn*")                                                              # Richiede il nome dell'alunn*
        nome = input(" ").capitalize()
        print("Inserire cognome dell'alunn*")                                                           # Richiede il cognome dell'alunn*
        cognome = input(" ").capitalize()
        
        nome_file = f"{cognome}{nome}.csv"                                                              # Costruisce il nome del file del profilo dell'alunn*
        filepath = os.path.join(self.directory, nome_file)                                              # Crea il percorso completo del file
    
        if os.path.exists(filepath):                                                                    # Se il file del profilo esiste
            print(f"Sei sicuro di voler eliminare il profilo alunn* {cognome} {nome}? (S/n)")           # Chiede all'utente la conferma per l'eliminazione del profilo
            risposta = input(" ")
    
            if risposta == "S":                                                                         # Se l'utente conferma l'eliminazione del profilo
                os.remove(filepath)                                                                     # Elimina il profilo
                print(f"Il profilo alunn* di {cognome} {nome} è stata eliminata correttamente.")        # Stampa un messaggio di conferma
            elif risposta == "n":                                                                       # Se l'utente annulla l'eliminazione del profilo
                print("Operazione annullata")                                                           # Stampa un messaggio di conferma
            else:                                                                                       # Se l'utente inserisce un comando sconosciuto
                print("Comando non riconosciuto")                                                       # Stampa un messaggio di errore
            return
    
        print(f"Il profilo dell'alunn* {cognome} {nome} non esiste")                                    # Stampa un messaggio se il profilo dell'alunno non esiste


    def select_classe(self):                                                                        # Funzione che avvia il menu principale della classe con tutti i comandi disponibili
        while True:
            Funzioni.start()                                                                        # Chiama la funzione start() del modulo Funzioni
            print("")
            print("1 - Selezionare un profilo alunn*")                                              # Mostra le opzioni tra cui scegliere
            print("2 - Creare un profilo alunn*")
            print("3 - Vedere la lista degli alunn*")
            print("4 - Vedere la media generale di tutta la classe")
            print("5 - Vedere la media pratica di tutta la classe")
            print("6 - Vedere la media orale di tutta la classe")
            print("7 - Aggiungere un compito di classe")
            print("8 - Eliminare un profilo alunn*")
            print("9 - Uscire dalla classe")
            comando = input(" " + self.nomeClasse + " >> ")                                         # Richiede all'utente di scegliere un opzione
            print("")

            if comando == "1":                                                                      # Chiama la funzione __selezionaAlunno()
                self.__selezionaAlunno()
            elif comando == "2":                                                                    # Chiama la funzione __creaProfilo()
                self.__creaProfilo()
            elif comando == "3":                                                                    # Chiama la funzione __elencaAlunni()
                self.__elencaAlunni()
            elif comando == "4":                                                                    # Chiama la funzione __gMedia()
                self.__gMedia()
            elif comando == "5":                                                                    # Chiama la funzione __pMedia()
                self.__pMedia()
            elif comando == "6":                                                                    # Chiama la funzione __oMedia()
                self.__oMedia()
            elif comando == "7":                                                                    # Chiama la funzione __nCompito()
                self.__nCompito()
            elif comando == "8":                                                                    # Chiama la funzione __eliminaAlunno()
                self.__eliminaAlunno()
            elif comando == "9":                                                                    # Ferma la funzione e fa uscire dalla classe
                print("Sei uscito dalla classe " + self.nomeClasse)
                break
            else:                                                                                   # Comunica se il comando non è stato riconosciuto
                print("Comando non riconosciuto.")
