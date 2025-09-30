import re
import random

# Les images disponibles
images = [
    "./images/frieren/frieren_meme.gif",
    "./images/frieren/burnice_meme.gif"
]

# Lire le README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Choisir une image aléatoire (ou basée sur l’heure)
new_image = random.choice(images)

# Remplacer l'ancienne image par la nouvelle
updated = re.sub(r'!\[.*?\]\(.*?\)', f'![]({new_image})', content)

# Sauvegarder
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)
