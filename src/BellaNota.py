from Malloppini import MenuPrincipale
from Malloppini import Funzioni
import os 
import json
import sys



if len(sys.argv) > 1:
  command_path = sys.argv[1]
else:
  if os.name == 'nt':
    settings_file = "settings_win.json"
  else:
    settings_file = "settings_linux.json"
  
  command_path = os.path.dirname(__file__)
  command_path = os.path.join(command_path, "..", "resources", settings_file)

command_path = os.path.realpath(command_path)

if not os.path.exists(command_path):
  print("File di configurazione mancante")
  print(command_path)

with open(command_path) as settings:
  data = json.load(settings)

print(command_path)
print(data['workdir'])


#if os.name == 'nt':
#  os.system('cls')
#else:
#  os.system('clear')
print("╔══╗───╔╗╔╗───╔═╗─╔╗──╔╗")
print("║╔╗║───║║║║───║║╚╗║║─╔╝╚╗")
print("║╚╝╚╦══╣║║║╔══╣╔╗╚╝╠═╩╗╔╬══╗")
print("║╔═╗║║═╣║║║║╔╗║║╚╗║║╔╗║║║╔╗║")
print("║╚═╝║║═╣╚╣╚╣╔╗║║─║║║╚╝║╚╣╔╗║")
print("╚═══╩══╩═╩═╩╝╚╩╝─╚═╩══╩═╩╝╚╝")
print("Created by Tommaso Bellandi")

#MenuPrincipale.inizio(parent_dir)
print("Grazie per aver utilizzato BellaNota")