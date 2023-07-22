from Malloppini import MenuPrincipale                   # Importa i moduli necessari
from Malloppini import Funzioni
import os
import json
import sys


if len(sys.argv) > 1:                                   # Controlla se sono stati passati argomenti da riga di comando
    command_path = sys.argv[1]                          # Se sono presenti argomenti, considera il primo come percorso del file di configurazione
else:                                                   # Se non ci sono argomenti, imposta il file di configurazione in base all'OS
    if os.name == 'nt':                                 # Win
        settings_file = "settings_win.json"
    else:                                               # Linux based
        settings_file = "settings_linux.json"
    
    command_path = os.path.dirname(__file__)            # Costruisce il percorso completo del file di configurazione
    command_path = os.path.join(command_path, "..", "resources", settings_file)

command_path = os.path.realpath(command_path)           # Ottiene il percorso del file di configurazione

if not os.path.exists(command_path):                    # Verifica se il file di configurazione esiste
    print("File di configurazione mancante")
    print(command_path)


with open(command_path) as settings:                    # Legge i dati dal file di configurazione
    data = json.load(settings)


print(command_path)                                     # Stampa il percorso del file di configurazione e il valore della chiave 'workdir' dai dati letti
print(data['workdir'])

print("╔══╗───╔╗╔╗───╔═╗─╔╗──╔╗")                       # Stampa una splash screen
print("║╔╗║───║║║║───║║╚╗║║─╔╝╚╗")
print("║╚╝╚╦══╣║║║╔══╣╔╗╚╝╠═╩╗╔╬══╗")
print("║╔═╗║║═╣║║║║╔╗║║╚╗║║╔╗║║║╔╗║")
print("║╚═╝║║═╣╚╣╚╣╔╗║║─║║║╚╝║╚╣╔╗║")
print("╚═══╩══╩═╩═╩╝╚╩╝─╚═╩══╩═╩╝╚╝")
print("Created by Tommaso Bellandi")

MenuPrincipale.inizio(command_path)                     # Iniziallizza il menu principale

print("Grazie per aver utilizzato BellaNota")           # Alla chiusura del programma stampa un messaggio di ringraziamento
