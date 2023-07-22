from Malloppini import Funzioni
from Malloppini import Alunno
import os
import csv

class Classe:
  def __init__(self, nomeClasse, parent_dir):
    self.parent_dir = parent_dir
    self.nomeClasse = nomeClasse
    self.directory = os.path.join(parent_dir, nomeClasse)
  def __selezionaAlunno(self):      #Comando 1
    while True:
      print("Inserire nome dell'alunn*")
      nome = input(" ").capitalize()
      print("Inserire cognome dell'alunn*")
      cognome = input(" ").capitalize()
      nome_file = f"{cognome}{nome}.csv"
      filepath = os.path.join(self.directory, nome_file)
      if os.path.exists(filepath):
        Alunno.menuAlunno(filepath, nome, cognome)
        break
      print(f"il profilo dell'alunn* {cognome} {nome} non esiste")
  def __creaProfilo(self):          #Comando 2
    print("Inserire il nome dell'alunn*")
    nome = input(" ").capitalize()
    print("Inserire il cognome dell'alunn*")
    cognome = input(" ").capitalize()
    while True:
      print(f"Confermare la creazione dell'alunn* {cognome} {nome}? S/n")
      conferma = input("").upper()
      if conferma == "S":
        nome_file = f"{cognome}{nome}.csv"
        filepath = os.path.join(self.directory, nome_file)
        if os.path.exists(filepath):
          print(f"L'alunn* {cognome} {nome} esiste già")
        else:
          with open(filepath, 'w'):
            pass
          print(f"Il profilo dell'alunn* {cognome} {nome} è stato creato correttamente")
        break
      elif conferma == "N":
        print("Creazione annullata")
        break
      else:
        print("Comando sconosciuto")
  def __elencaAlunni(self):         #Comando 3
    files = os.listdir(self.directory)
    csv_files = [file for file in files if file.endswith('.csv')]
    if len(csv_files) == 0:
      print("Non hai nessun profilo alunn* in questa classe")
      return

    print("I nomi dei tuoi alunn* sono:")
    for file in csv_files:
      nome_formattato = Funzioni.format_file_name(file)
      print(nome_formattato)
  def __gMedia(self):               #Comando 4
    media_generale = Funzioni.mediacl(self.directory, "g")
    if media_generale is not None:
      print(f"La media generale della classe {self.nomeClasse} è: {media_generale}")
      return
    print("Nessun voto presente per calcolare la media generale")
  def __pMedia(self):               #Comando 5
    media_pratica = Funzioni.mediacl(self.directory, "p")
    if media_pratica is not None:
      print(f"La media pratica della classe {self.nomeClasse} è: {media_pratica}")
      return
    print("Nessun voto presente per calcolare la media pratica")
  def __oMedia(self):               #Comando 6
    media_orale = Funzioni.mediacl(self.directory, "o")
    if media_orale is not None:
      print(f"La media orale della classe {self.nomeClasse} è: {media_orale}")
      return
    print("Nessun voto presente per calcolare la media orale")
  def __nCompito(self):             #Comando 7
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
    Funzioni.compito(self.directory, data, tipo)
  def __eliminaAlunno(self):        #Comando 8
    print("Inserire nome dell'alunn*")
    nome = input(" ").capitalize()
    print("Inserire cognome dell'alunn*")
    cognome = input(" ").capitalize()
    nome_file = f"{cognome}{nome}.csv"
    filepath = os.path.join(self.directory, nome_file)
    if os.path.exists(filepath):
      print(f"Sei sicuro di voler eliminare il profilo alunn* {cognome} {nome}? (S/n)")
      risposta = input(" ")
      if risposta == "S":
        os.remove(filepath)
        print(f"Il profilo alunn* di {cognome} {nome} è stata eliminata correttamente.")
      elif risposta == "n":
        print("Operazione annullata")
      else:
        print("Comando non riconosciuto")
      return
    print(f"il profilo dell'alunn* {cognome} {nome} non esiste")

  def select_classe(self):
    while True:
      Funzioni.start()
      print("")
      print("1 - Selezionare un profilo alunn*")
      print("2 - Creare un profilo alunn*")
      print("3 - Vedere la lista degli alunn*")
      print("4 - Vedere la media generale di tutta la classe")
      print("5 - Vedere la media pratica di tutta la classe")
      print("6 - Vedere la media orale di tutta la classe")
      print("7 - Aggiungere un compito di classe")
      print("8 - Eliminare un profilo alunn*")
      print("9 - Uscire dalla classe")
      comando = input(" " + self.nomeClasse + " >> ")
      print("")

      if comando == "1":
        self.__selezionaAlunno()
      elif comando == "2":
        self.__creaProfilo()
      elif comando == "3":
        self.__elencaAlunni()
      elif comando == "4":
        self.__gMedia()
      elif comando == "5":
        self.__pMedia()
      elif comando == "6":
        self.__oMedia()
      elif comando == "7":
        self.__nCompito()
      elif comando == "8":
        self.__eliminaAlunno()
      elif comando == "9":
        print("Sei uscito dalla classe "+self.nomeClasse)
        break
      else:
        print("Comando non riconosciuto.")
