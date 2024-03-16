from MenuPrincipale import MenuPrincipale                                       # Importa i moduli necessari
import os
import json
import sys

if os.name == 'nt':                                                             # Win
    settings_file = "settings_win.json"
else:                                                                           # Linux based
    settings_file = "settings_linux.json"

command_path = os.path.dirname(__file__)                                        # Costruisce il percorso completo del file di configurazione
command_path = os.path.join(command_path, "..", "resources", settings_file)

command_path = os.path.realpath(command_path)                                   # Ottiene il percorso del file di configurazione

if not os.path.exists(command_path):                                            # Verifica se il file di configurazione esiste
    print("File di configurazione mancante")
    print(command_path)



with open(command_path) as settings:                                            # Legge i dati dal file di configurazione
    data = json.load(settings)

if len(sys.argv) > 1:                                                           # Controlla se sono stati passati argomenti da riga di comando
    classe = sys.argv[1]                                                        # Se sono presenti argomenti, considera il primo come percorso del file di configurazione
    classe = classe.upper()
    controlpath = os.path.join(data['workdir'], classe)
    if not os.path.exists(controlpath):
        print("Nessuna classe corrispondente al nome inserito")
    else:
        nome = sys.argv[2].capitalize()
        cognome = sys.argv[3].capitalize()

        nome_file = f"{cognome}{nome}.csv"                                      # Costruisce il nome del file del profilo dell'alunn*
        filepath = os.path.join(controlpath, nome_file)                         # Crea il percorso completo del file

        if os.path.exists(filepath):                                            # Controlla se il file del profilo esiste
            mioAlunno = mioAlunno(classe, parent_dir)
            mioAlunno.menuAlunno()
        print(
            f"Il profilo dell'alunn* {cognome} {nome} non esiste")              # Stampa un messaggio di errore se il profilo non esiste


print(command_path)                                                             # Stampa il percorso del file di configurazione e il valore della chiave 'workdir' dai dati letti
print(data['workdir'])
parent_dir = data['workdir']
if not os.path.exists(parent_dir):
    os.mkdir(parent_dir)
    print(f"Cartella dei file creata in {parent_dir}")

print("╔══╗───╔╗╔╗───╔═╗─╔╗──╔╗")                                               # Stampa una splash screen
print("║╔╗║───║║║║───║║╚╗║║─╔╝╚╗")
print("║╚╝╚╦══╣║║║╔══╣╔╗╚╝╠═╩╗╔╬══╗")
print("║╔═╗║║═╣║║║║╔╗║║╚╗║║╔╗║║║╔╗║")
print("║╚═╝║║═╣╚╣╚╣╔╗║║─║║║╚╝║╚╣╔╗║")
print("╚═══╩══╩═╩═╩╝╚╩╝─╚═╩══╩═╩╝╚╝")
print("Created by Tommaso Bellandi")

menuPrincipale = MenuPrincipale(parent_dir)                                     # Crea un'istanza della classe MenuPrincipale
menuPrincipale.inizio()                                                         # Iniziallizza il menu principale

print("Grazie per aver utilizzato BellaNota")                                   # Alla chiusura del programma stampa un messaggio di ringraziamento
