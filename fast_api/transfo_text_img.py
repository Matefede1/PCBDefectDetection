from PIL import Image
import cv2

def array_to_image(array, width, height):
    # Créer une nouvelle image
    image = Image.new("RGB", (width, height))

    # Définir les pixels de l'image
    pixels = image.load()
    for y in range(height):
        for x in range(width):
            index = (y * width + x) * 3
            r, g, b = array[index:index + 3]
            pixels[x, y] = (r, g, b)

    return image



def save_image(cv2_img, output_path):
    try:
        # Save the image
        cv2.imwrite(output_path, cv2_img)
        print(f"Image saved successfully at: {output_path}")
    except Exception as e:
        print(f"Error saving image: {e}")

if __name__ == "__main__":
    # Assuming cv2_img is your OpenCV image and output_path is the desired output path
    #cv2_img =  # Your OpenCV image
    #output_path = "img_output/image.jpg"

    # Save the image
    #save_image(cv2_img, output_path)

    # Charger le tableau depuis le fichier texte
    with open('array_data.txt', 'r') as file:
        lines = file.readlines()

    # Convertir les données du tableau en liste d'entiers
    array_data = [int(value) for line in lines for value in line.split(',')]

    # Déterminer les dimensions de l'image
    width = len(array_data) // 3  # Chaque triplet de valeurs représente un pixel
    height = len(lines)

    # Convertir le tableau en une image
    image = array_to_image(array_data, width, height)

    # Sauvegarder l'image en tant que fichier JPG
    image.save('output_image.jpg')

#if __name__ == "__main__":
    #main()
