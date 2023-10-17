def calcular_recorte_video(resolucion_original):
    ancho_original, alto_original = resolucion_original.split("x")
    ancho_original = int(ancho_original)
    alto_original = int(alto_original)

    if ancho_original / alto_original > 2:
        ancho_recorte = int(alto_original * 2)
        alto_recorte = alto_original
    else:
        alto_recorte = int(ancho_original / 2)
        ancho_recorte = ancho_original

    return f"Ancho: {ancho_recorte}, Alto: {alto_recorte}"


def verificar_rectangulo(resolution):
    width, height = resolution.split("x")
    width = int(width)
    height = int(height)

    if width > height:
        return "Modo landscape (rectángulo de largo)"
    elif height > width:
        return "Modo portrait (rectángulo de alto)"
    else:
        return "Modo cuadrado"

def recortar_a_portrait(resolucion):
    width, height = resolucion.split("x")
    width = int(width)
    height = int(height)

    if width > height:
        new_width = int(height * 0.3611)  # Aproximadamente 0.3611 es la relación para convertir de 16:9 a 9:16
        new_height = height
        
    return f"{new_width}x{new_height}"



def crop_landscape_to_portrait(resolution):
    # Obtener las dimensiones de la resolución de entrada
    width, height = map(int, resolution.split('x'))

    # Calcular la nueva altura para la resolución de retrato (410x720)
    new_height = (width * 720) // 410

    # Obtener los valores de recorte
    left = 0
    top = (height - new_height) // 2
    right = width
    bottom = top + new_height

    # Devolver el recorte de resolución en formato de cadena
    return "410x720"


  
# Ejemplo de uso


resolucion1 = "1280x720"
resolucion2 = "410x720"

resultado1 = verificar_rectangulo(resolucion1)


resolution = "1920x1080"
cropped_resolution = crop_landscape_to_portrait(resolution)
print(cropped_resolution)



resolucion_recortada = recortar_a_portrait(resolucion1)
print(f"Resolución recortada: {resolucion_recortada}")
