import re
import random

# Les images disponibles
images = [
    # "./images/Frieren/frieren_meme.gif",
    "./images/burnice/burnice_meme.gif",
]

# Lire le contenu du README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Choisir une nouvelle image au hasard
new_image = random.choice(images)

pattern = r'(## <img src=")(.*?)(" width="50"> About me)'
replacement = r'\1' + new_image + r'\3'

# Appliquer le remplacement
updated_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

# Sauvegarder les modifications dans le README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_content)

print(f"README updated with image: {new_image}")