from rembg import remove # type: ignore
from PIL import Image, ImageSequence

# Charger ton GIF
input_gif = r"C:\Users\pokem\Desktop\Code\TMCooper\images\Frieren\frieren_meme.gif"
output_gif = r"C:\Users\pokem\Desktop\Code\TMCooper\images\Frieren\frieren_meme_i.gif"

gif = Image.open(input_gif)
frames = []

# Parcourir chaque frame
for frame in ImageSequence.Iterator(gif):
    # Convertir en RGBA
    frame = frame.convert("RGBA")

    # Supprimer le fond
    new_frame = remove(frame)

    # Ajouter aux frames
    frames.append(new_frame)

# Sauvegarder un nouveau GIF avec transparence
frames[0].save(
    output_gif,
    save_all=True,
    append_images=frames[1:],
    loop=0,
    disposal=2,
    transparency=0
)

print("✅ Nouveau GIF créé :", output_gif)
