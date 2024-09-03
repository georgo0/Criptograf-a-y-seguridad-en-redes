import sys
import time
import struct
import scapy.all as scapy
from cesar import cifrado_cesar  # Importar la función desde cesar.py

# Cargar o inicializar el identificador ICMP
try:
    with open("identifier.txt", "r") as file:
        id_icmp = int(file.read())
except FileNotFoundError:
    id_icmp = 1

with open("identifier.txt", "w") as file:
    file.write(str(id_icmp + 1))

id_ipv4 = scapy.RandShort()  # Generar un identificador IPv4 aleatorio
timestamp = struct.pack("<Q", int(time.time()))  # Crear un timestamp

# Datos ICMP y valores de ping
icmp_ping = bytes(range(0x10, 0x38))

# Verificar los argumentos de la línea de comandos
if len(sys.argv) != 2:
    print("Uso: python3 pingv4.py <mensaje_cifrado>")
    sys.exit(1)

mensaje_cifrado = sys.argv[1]

# Crear y enviar paquetes
packets = []
for i, caracter in enumerate(mensaje_cifrado):
    # Crear el payload del paquete ICMP
    payload = timestamp + icmp_ping + caracter.encode()
    # Crear el paquete ICMP con el campo 'seq' secuencial
    packet = scapy.IP(dst="127.0.0.1", id=id_ipv4, flags="DF") / scapy.ICMP(id=id_icmp, seq=i + 1) / payload
    packets.append(packet)
    
    # Enviar el paquete individualmente
    scapy.send(packet, verbose=False)
    
    # Mostrar mensaje de confirmación
    print(f"Sent packet {i + 1}.")

# Mensaje final indicando que todos los paquetes fueron enviados 
print("Todos los paquetes han sido enviados.")