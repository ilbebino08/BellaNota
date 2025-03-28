import os
import csv
import datetime

def start():                                                                                              # Stampa la splash screen e attende conferma dall'utente
  print("\n\n")
  print("Premere invio per continuare")                                                                  
  input("")
  if os.name == 'nt':                                                                                     # Pulisce il terminale per Windows
    os.system('cls')
  else:                                                                                                   # Pulisce il terminale per Linux
    os.system('clear')
  print("\n".join([
    "╔══╗️️️️️️╔╗╔╗️️️️️️╔═╗️╔╗️️╔╗",
    "║══║️️️️║╗║╗️️️️║╗╚╗╗",
    "║╚╝╚═══║╗╗╗╔══╗╚╝═╗╔═══╗",
    "║╔═║║══║╗╗╗║╗╚╗╗╗║║╗═╗",
    "║╚═║║══║╚╝║╗╗╗║╗╗╗║╗╗╗",
    "╚══╝╚══╝╚══╝╚╝╚╝╚╝╚╝╚╝"
  ]))
  print("Created by Tommaso Bellandi")

def compito(directory, data, tipo):                                                                       # Aggiunge un voto ai file CSV degli studenti
  files = os.listdir(directory)
  csv_files = [file for file in files if file.endswith('.csv')]
  for file in csv_files:
    filepath = os.path.join(directory, file)
    nome_formattato = format_file_name(file)
    while True:
      voto = input(f"Voto dell'alunno/a '{nome_formattato}': ")
      if float(voto) <= 10 and float(voto) >= 2:
        break
      print("Impossibile mettere voti maggiori di 10 o minori di 2")
    with open(filepath, 'a', newline='') as file:
      writer = csv.writer(file)
      writer.writerow([voto, data, tipo])

def format_file_name(filename):                                                                           # Riformatta il nome del file rimuovendo l'estensione e separando le lettere maiuscole con spazi
  nome_file = os.path.splitext(filename)[0]
  nome_formattato = ''.join([f' {c}' if c.isupper() and i > 0 else c for i, c in enumerate(nome_file)])
  return nome_formattato

def check_data(data):                                                                                     # Controlla che la data sia nel formato corretto (dd/mm/yyyy)
  try:
    datetime.datetime.strptime(data, '%d/%m/%Y')
    return True
  except ValueError:
    return False

def mediacl(directory, metodo):                                                                          # Calcola la media dei voti in base al metodo selezionato
  numeri = []
  for filename in os.listdir(directory):
    if filename.endswith(".csv"):
      filepath = os.path.join(directory, filename)
      with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
          if metodo == "g":                                                                              # Prende tutti i voti
            if len(row) > 0:
              numero = row[0]
              if numero.isdigit():
                numeri.append(int(numero))
          elif metodo == "o":                                                                            # Prende solo i voti orali
            if len(row) > 0 and row[2] != "p":
              numero = row[0]
              if numero.isdigit():
                numeri.append(int(numero))
          elif metodo == "p":                                                                            # Prende solo i voti pratici
            if len(row) > 0 and row[2] != "o":
              numero = row[0]
              if numero.isdigit():
                numeri.append(int(numero))

  if len(numeri) > 0:
    media = sum(numeri) / len(numeri)
    media = round(media, 2)
    return media
  else:
    return None
