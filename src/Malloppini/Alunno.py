from Malloppini import Funzioni
import csv

def __aggiungiVoto(filepath):
    print("Inserisci la data (formato: dd/mm/yyyy):")
    data = input(" ")
    if not Funzioni.check_data(data):
        print("Data non valida. Riprova.")
        return
    print("Inserisci il tipo di compito (p = pratico, o = orale):")
    tipo = input(" ")
    if tipo not in ["p", "o"]:
        print("Tipo di compito non valido. Riprova.")
        return
    while True:
        voto = input("Inserire voto: ")
        if not float(voto) <= 10 and float(voto) >= 2:
            print("Impossibile impostare un voto maggiore di 10 e minore di 2.")
            return
        with open(filepath, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([voto, data, tipo])
            print("Voto inserito correttamente")
        break

def __vediMedia(filepath, metodo, cognome, nome):
    numeri = []  # Lista per memorizzare i numeri dei voti

    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if metodo == "g":
                if len(row) > 0:
                    numero = row[0]
                    if numero.isdigit():
                        numeri.append(int(numero))
            elif metodo == "o":
                if len(row) > 0 and row[2] != "p":
                    numero = row[0]
                    if numero.isdigit():
                        numeri.append(int(numero))
            elif metodo == "p":
                if len(row) > 0 and row[2] != "o":
                    numero = row[0]
                    if numero.isdigit():
                        numeri.append(int(numero))

    if len(numeri) > 0:
        media = sum(numeri) / len(numeri)
        media = round(media, 2)
        if metodo == "g":
            print(f"La media dell'alunn* {cognome} {nome} è {media}")
        elif metodo == "o":
            print(f"La media orale dell'alunn* {cognome} {nome} è {media}")
        elif metodo == "p":
            print(f"La media pratica dell'alunn* {cognome} {nome} è {media}")
    else:
        if metodo == "g":
            print(f"L'alunn* {cognome} {nome} non ha voti")
        elif metodo == "o":
            print(f"L'alunn* {cognome} {nome} non ha voti orali")
        elif metodo == "p":
            print(f"L'alunn* {cognome} {nome} non ha voti pratici")

def __listaVoti(filepath):
    voti = []  # Lista per memorizzare i voti

    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for riga in reader:
            if len(riga) >= 3:
                colonna0 = riga[0]
                colonna1 = riga[1]
                colonna2 = riga[2]

                tipo_compito = "Orale" if colonna2.lower() == "o" else "Pratico"
                voti.append((colonna0, colonna1, tipo_compito))
    
    return voti

def menuAlunno(filepath, nome, cognome):
    while True:
        Funzioni.start()
        print("")
        print("1 - Aggiungere un voto")
        print("2 - Vedere la media generale")
        print("3 - Vedere la media pratica")
        print("4 - Vedere la media orale")
        print("5 - Vedere la lista dei voti")
        print("6 - Uscire dal profilo alunn*")
        comando = input(" " + nome + " " + cognome + " >> ")
        print("")
        if comando == "1":
            __aggiungiVoto(filepath)
        elif comando == "2":
            __vediMedia(filepath, "g", cognome, nome)
        elif comando == "3":
            __vediMedia(filepath, "p", cognome, nome)
        elif comando == "4":
            __vediMedia(filepath, "o", cognome, nome)
        elif comando == "5":
            voti = __listaVoti(filepath)
            for voto in voti:
                colonna0, colonna1, tipo_compito = voto
                print(f"{colonna0} {colonna1} {tipo_compito}")
        elif comando == "6":
            print("Sei uscito dal profilo alunn*")
            break
        else:
            print("Comando non riconosciuto.")