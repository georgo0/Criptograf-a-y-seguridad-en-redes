from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

# Solicitar datos y ajustar clave e IV
def solicitar_datos():
    key_hex = input("Ingrese la clave para AES-256 en hexadecimal (64 caracteres para 32 bytes): ")
    iv_hex = input("Ingrese el Vector de Inicialización (IV) para AES-256 en hexadecimal (32 caracteres para 16 bytes): ")
    mensaje = input("Ingrese el texto a cifrar: ").encode()

    # Convertir clave e IV de hexadecimal a bytes
    key = bytes.fromhex(key_hex)
    iv = bytes.fromhex(iv_hex)

    # Ajuste de clave
    if len(key) < 32:
        key += get_random_bytes(32 - len(key))
    else:
        key = key[:32]

    # Ajuste de IV
    if len(iv) < 16:
        iv += get_random_bytes(16 - len(iv))
    else:
        iv = iv[:16]

    print("--------------------------------------")
    print(f"\033[93mClave ajustada: {key.hex()}\033[0m")
    print(f"\033[93mIV ajustado: {iv.hex()}\033[0m")
    return key, iv, mensaje

# Cifrado y Descifrado con AES-256
def aes_256_cifrar_descifrar():
    key, iv, mensaje = solicitar_datos()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    mensaje_cifrado = cipher.encrypt(pad(mensaje, AES.block_size))
    print("--------------------------------------")
    print(f"\033[92mTexto cifrado (AES-256): {mensaje_cifrado.hex()}\033[0m")
   
    cipher_dec = AES.new(key, AES.MODE_CBC, iv)
    mensaje_descifrado = unpad(cipher_dec.decrypt(mensaje_cifrado), AES.block_size)
    print(f"\033[92mTexto descifrado (AES-256): {mensaje_descifrado.decode()}\033[0m")

if __name__ == "__main__":
    aes_256_cifrar_descifrar()