from Malloppini.Classe import Classe
from Malloppini import Funzioni
import os
import csv

def __selezionaClasse(parent_dir):      #Comando 1
  print("Inserire nome della classe")
  classe = input(" ")
  classe = classe.upper()
  controlpath = os.path.join(parent_dir, classe)
  if not os.path.exists(controlpath):
    print("Nessuna classe corrispondente al nome inserito")
  elif classe == "":
    print("Nessuna classe selezionata")
  else:
    miaClasse = Classe(classe, parent_dir)
    miaClasse.select_classe()
def __vedereLista(parent_dir):          #Comando 2
  numclassi = 0
  directories = [name for name in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, name))]
  for dir_name in directories:
    numclassi += 1
  if numclassi == 0:
    print("Non hai nessuna classe")
  else:
    print("Lista delle tue " + str(numclassi) + " classi è:")
    for dir_name in directories:
      print(dir_name)
def __creaClasse(parent_dir):           #Comando 3
  print("Inserire nome della classe")
  directory = input(" ")
  directory = directory.upper()
  controlpath = os.path.join(parent_dir, directory)

  if not os.path.exists(controlpath):
    os.makedirs(controlpath)
    print(f"La classe '{directory}' è stata creata.")
    return
  print(f"La classe '{directory}' esiste già.")
def __cancellaClasse(parent_dir):       #Comando 4
  print("Inserire il nome della classe che vuoi eliminare?")
  directory = input(" ")
  directory = directory.upper()
  controlpath = os.path.join(parent_dir, directory)
  if not os.path.exists(controlpath):
    print(f"La classe '{directory}' non esiste.")
    return
  while True:
    print("Sei sicuro di voler eliminare la classe? (S/n)")
    risposta = input(" ")
    if risposta == "S":
      os.rmdir(controlpath)
      print(f"La classe {directory} è stata eliminata correttamente.")
      break
    elif risposta == "n":
      print("Operazione annullata")
      break
    else:
      print("Comando non riconosciuto")


def inizio(parent_dir):
  while True:
    print("")
    print("1 - Selezionare la classe")
    print("2 - Vedere la lista delle classi")
    print("3 - Creare una classe")
    print("4 - Eliminare una classe")
    print("5 - Uscire dal programma")
    comando = input("  >> ")
    print("")

    if comando == "1":
      __selezionaClasse(parent_dir)
    elif comando == "2":
      __vedereLista(parent_dir)
    elif comando == "3":
      __creaClasse(parent_dir)
    elif comando == "4":
      __cancellaClasse(parent_dir)
    elif comando == "5":
      break
    else:
      print("Comando non riconosciuto.")
    Funzioni.start()