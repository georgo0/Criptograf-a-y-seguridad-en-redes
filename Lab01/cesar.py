import argparse

def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    
    # Recorrer cada carácter en el texto
    for letra in texto:
        if letra.isalpha():  # Verificar si es una letra
            ascii_offset = 65 if letra.isupper() else 97  # Determina si es mayúscula o minúscula
            # Desplazar la letra y ajustar para el ciclo en el alfabeto
            letra_cifrada = chr((ord(letra) - ascii_offset + desplazamiento) % 26 + ascii_offset)
            resultado += letra_cifrada
        else:
            # Si no es una letra, no la cifra (ej. espacios, signos de puntuación)
            resultado += letra
    
    return resultado

if __name__ == "__main__":
    # Crear el analizador de argumentos
    parser = argparse.ArgumentParser(description='Cifrado Cesar en Python')
    
    # Añadir argumentos para el texto de entrada y el desplazamiento
    parser.add_argument('texto', type=str, help='Texto a cifrar')
    parser.add_argument('desplazamiento', type=int, help='Número de desplazamiento')

    # Parsear los argumentos
    args = parser.parse_args()

    # Ejecutar la función de cifrado
    texto_cifrado = cifrado_cesar(args.texto, args.desplazamiento)

    # Mostrar el resultado en la consola
    print("Texto cifrado:", texto_cifrado)