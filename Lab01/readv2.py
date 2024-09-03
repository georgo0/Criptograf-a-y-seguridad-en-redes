import scapy.all as scapy
import string
import sys

# Función para el descifrado César
def descifrar_cesar(texto, shift):
    resultado = []
    for char in texto:
        if char in string.ascii_letters:
            shift_amount = shift if char.islower() else shift
            shifted = chr((ord(char) - shift_amount - 65) % 26 + 65) if char.isupper() else chr((ord(char) - shift_amount - 97) % 26 + 97)
            resultado.append(shifted)
        else:
            resultado.append(char)
    return ''.join(resultado)

# Función para contar las palabras válidas en el mensaje
def contar_palabras_validas(mensaje, diccionario):
    palabras = mensaje.split()
    return sum(1 for palabra in palabras if palabra.lower() in diccionario)

# Función para extraer el último carácter de información de cada paquete ICMP
def extract_last_char_from_pcap(pcap_file):
    packets = scapy.rdpcap(pcap_file)
    last_chars = []

    for packet in packets:
        if scapy.ICMP in packet and len(packet[scapy.ICMP].payload) > 0:
            payload = bytes(packet[scapy.ICMP].payload)
            last_char = payload[-1:].decode(errors='ignore')
            last_chars.append(last_char)
    
    combined_string = ''.join(last_chars)
    return combined_string

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 descifrar.py <archivo_pcap>")
        sys.exit(1)
    
    pcap_file = sys.argv[1]
    texto_cifrado = extract_last_char_from_pcap(pcap_file)

    diccionario_file = 'diccionario.txt'

    # Cargar el diccionario de palabras válidas
    with open(diccionario_file, 'r') as f:
        diccionario = set(line.strip().lower() for line in f)

    mejor_mensaje = None
    max_coincidencias = 0
    desplazamiento_mejor_mensaje = 0

    resultados = []

    # Intentar todos los desplazamientos posibles
    for shift in range(26):
        decrypted_message = descifrar_cesar(texto_cifrado, shift)
        coincidencias = contar_palabras_validas(decrypted_message, diccionario)
            
        resultados.append((shift, decrypted_message, coincidencias))
            
        if coincidencias > max_coincidencias:
            max_coincidencias = coincidencias
            mejor_mensaje = decrypted_message
            desplazamiento_mejor_mensaje = shift

    # Imprimir todos los mensajes, destacando el mejor
    for idx, (shift, mensaje, coincidencias) in enumerate(resultados, start=1):
        if mensaje == mejor_mensaje:
            print(f"{idx} \033[92m{mensaje}\033[0m")
        else:
            print(f"{idx} {mensaje}")

    # Mostrar la palabra en texto claro más probable
    print(f"\nPalabra en texto claro más probable: \033[92m{mejor_mensaje}\033[0m")

if __name__ == "__main__":
    main()
