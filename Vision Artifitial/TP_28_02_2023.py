from PIL import Image

# Charger l'image
img = Image.open("Vision Artifitial/img/img1.jpg")

# Convertir l'image en niveaux de gris
img_gray = img.convert('L')

# Calculer la luminosit√© moyenne
luminance = sum(img_gray.getdata()) / len(img_gray.getdata())

# Afficher la luminosit√©
print("Luminosit√© : ", luminance)

