import os
import csv
import datetime

def start():
  print("")
  print("")
  print("Premere invio per continuare")
  input("")
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
  print("╔══╗───╔╗╔╗───╔═╗─╔╗──╔╗")
  print("║╔╗║───║║║║───║║╚╗║║─╔╝╚╗")
  print("║╚╝╚╦══╣║║║╔══╣╔╗╚╝╠═╩╗╔╬══╗")
  print("║╔═╗║║═╣║║║║╔╗║║╚╗║║╔╗║║║╔╗║")
  print("║╚═╝║║═╣╚╣╚╣╔╗║║─║║║╚╝║╚╣╔╗║")
  print("╚═══╩══╩═╩═╩╝╚╩╝─╚═╩══╩═╩╝╚╝")
  print("Created by Tommaso Bellandi")

def compito(directory, data, tipo):                                 #Definisco la funzione compito
  files = os.listdir(directory)
  csv_files = [file for file in files if file.endswith('.csv')]
  for file in csv_files:
    filepath = os.path.join(directory, file)
    nome_formattato = format_file_name(file)
    while True:
      voto = input(f"Voto dell'alunn* '{nome_formattato}': ")
      if float(voto) <= 10 and float(voto) >= 2:
        break
      print("impossibile mettere voti maggiori di 10 o minori di 2")
    with open(filepath, 'a', newline='') as file:
      writer = csv.writer(file)
      writer.writerow([voto, data, tipo])
def format_file_name(filename):
  nome_file = os.path.splitext(filename)[0]
  nome_formattato = ''.join([f' {c}' if c.isupper() and i > 0 else c for i, c in enumerate(nome_file)])
  return nome_formattato
def check_data(data):
  try:
    datetime.datetime.strptime(data, '%d/%m/%Y')
    return True
  except ValueError:
    return False
def mediacl(directory, metodo):
  numeri = []
  for filename in os.listdir(directory):
    if filename.endswith(".csv"):
      filepath = os.path.join(directory, filename)
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
    return media
  else:
    return None