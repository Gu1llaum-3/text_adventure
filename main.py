from colorama import Fore, Style
from typing import Any, Union
import time, random
import yaml

def simulate_typing(text: Union[str, Any]) -> None:
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(0.02, 0.05))
    print('')

def print_colored(text, color):
    return (color + text + Style.RESET_ALL)


def afficher_chapitre(index):
    afficher_chapitre_text(index)
    choice = afficher_chapitre_choices(index)
    return choice


def afficher_chapitre_text(index):
    simulate_typing(chapitre[index]['text'])


def afficher_chapitre_choices(index):
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


def ouvrir_chapitre(chapitre):
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

chapitre = ouvrir_chapitre(1)
user_choice = afficher_chapitre(0)

if user_choice == 1:
    chapitre = ouvrir_chapitre(2)
    user_choice = afficher_chapitre(0)
elif user_choice == 2:
    afficher_chapitre(1)
    # simulate_typing("Vous regarder autour de vous mais ne voyez rien de particulier")