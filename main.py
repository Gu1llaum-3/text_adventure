from colorama import Fore, Style
from typing import Any, Union
import time, random, os
import yaml

# Effacer la console
def clear_console():
    os.system('clear')

# Simuler une frappe humaine
def simulate_typing(text: Union[str, Any]) -> None:
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(0.02, 0.05))
    print('')

# Colorer des mots ou de texte
def print_colored(text, color):
    return (color + text + Style.RESET_ALL)

# Afficher l'index complet (text et choix)
def afficher_index(index):
    afficher_index_text(index)
    choice = afficher_index_choices(index)
    return choice

# Afficher seulement le text d'un index
def afficher_index_text(index):
    simulate_typing(chapitre[index]['text'])

# Afficher seulement les choix dun index
def afficher_index_choices(index):
    print("Que faites-vous ?")
    try:
        choices = chapitre[index]['choices']
        nb_choices = len(choices)
        choices_list = []  # Créer une liste vide pour stocker les choix
        for i in range(nb_choices):
            choice_text = f"{i+1}. {choices[i]['name']}"
            choices_list.append(choice_text)  # Ajouter chaque choix à la liste
            simulate_typing(choice_text)
        while True:
            choice = input("> ")
            if choice.isdigit() and int(choice) in range(1, nb_choices+1):
                return int(choice)  # Renvoyer l'indice du choix sélectionné dans la liste
            else:
                simulate_typing("Veuillez entrer un choix valide.")
    except:
        return

# charger le chapitre depuis le fichier yaml
def charger_chapitre(chapitre):
    with open(f'chapitres/chapitre_{chapitre}.yml', 'r', encoding='utf-8') as file:
        chapitre = yaml.load(file, Loader=yaml.FullLoader)
        return chapitre


# with open('chapitres/chapitre_1.yml', 'r', encoding='utf-8') as file:
#     chapitres = yaml.load(file, Loader=yaml.FullLoader)
# with open('chapitres/chapitre_2', 'r', encoding='utf-8') as file:
#     chapitres = yaml.load(file, Loader=yaml.FullLoader)


name = input("Entrez votre nom : ")
oui = print_colored("oui", Fore.GREEN)
non = print_colored("non", Fore.RED)

while True:
    simulate_typing(f"Bonjour {name} ! Prêt pour l'aventure ? ({oui}/{non})")
    start = input("> ")
    if start.lower() == "oui":
        break
    elif start.lower() == "non":
        simulate_typing("Alors je vous dis au revoir !")
        exit(0)
    else:
        simulate_typing("Veuillez répondre par 'oui' ou 'non'.")

# Chapitre 1
clear_console()
chapitre = charger_chapitre(1)
user_choice = afficher_index(0)
while not user_choice == 1:
    if user_choice == 1:
        break
    elif user_choice == 2:
        print()
        afficher_index_text(1)
        user_choice = afficher_index_choices(0)

# Chapitre 2
clear_console()
chapitre = charger_chapitre(2)
# Index 0
user_choice = afficher_index(0)
if user_choice == 1:
  # Index 1
  print()
  afficher_index(1)
  if user_choice == 1:
    # Index 2
    print()
    afficher_index(2)
    if user_choice == 1:
      print()
      afficher_index(3)
    elif user_choice == 2:
      print()
      afficher_index(4)
elif user_choice == 2:
  # Index 4
  print()
  afficher_index(4)