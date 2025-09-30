import re
import random
import sys # On importe sys pour pouvoir quitter le script proprement

print("--- DÉBUT DU SCRIPT DE MISE À JOUR DU README ---")

# La liste complète des images disponibles
all_images = [
    "./images/Frieren/frieren_meme.gif",
    # "./images/burnice/burnice_meme.gif",
]
print(f"Images disponibles: {len(all_images)}")

# Lire le contenu du README
try:
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    print("Fichier README.md lu avec succès.")
except FileNotFoundError:
    print("ERREUR: Le fichier README.md est introuvable.")
    sys.exit(1) # On quitte le script avec un code d'erreur

# Le pattern pour trouver la ligne et extraire l'image actuelle
pattern = r'(## <img src=")(.*?)(" width="50"> About me)'
match = re.search(pattern, content, flags=re.MULTILINE)

if not match:
    print("ERREUR: Impossible de trouver la ligne correspondante dans le README.")
    print("Le script cherche une ligne qui ressemble à : '## <img src=\"...\" width=\"50\"> About me'")
    sys.exit(0) # On quitte sans erreur, car le fichier n'est pas celui attendu

current_image = match.group(2)
print(f"Image actuelle détectée : {current_image}")

possible_choices = [img for img in all_images if img != current_image]

if not possible_choices:
    print("Aucune autre image disponible pour le changement. Le fichier reste inchangé.")
    sys.exit(0)

new_image = random.choice(possible_choices)
print(f"Nouvelle image choisie : {new_image}")

replacement = r'\1' + new_image + r'\3'
updated_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_content)

print("SUCCÈS: README.md a été mis à jour.")
print("--- FIN DU SCRIPT ---")