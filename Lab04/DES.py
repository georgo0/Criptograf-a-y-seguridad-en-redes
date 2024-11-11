from Cryptodome.Cipher import DES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

# Solicitar datos y ajustar clave e IV
def solicitar_datos():
    key_hex = input("Ingrese la clave para DES en hexadecimal (16 caracteres para 8 bytes): ")
    iv_hex = input("Ingrese el Vector de Inicialización (IV) para DES en hexadecimal (16 caracteres para 8 bytes): ")
    mensaje = input("Ingrese el texto plano a cifrar: ").encode()

    # Convertir clave e IV de hexadecimal a bytes
    key = bytes.fromhex(key_hex)
    iv = bytes.fromhex(iv_hex)

    # Ajuste de clave e IV (por si acaso no cumplen con el tamaño)
    if len(key) < 8:
        key += get_random_bytes(8 - len(key))
    else:
        key = key[:8]

    if len(iv) < 8:
        iv += get_random_bytes(8 - len(iv))
    else:
        iv = iv[:8]
    print("--------------------------------------")
    print(f"\033[93mClave ajustada: {key.hex()}\033[0m")
    print(f"\033[93mIV ajustado: {iv.hex()}\033[0m")
    return key, iv, mensaje

# Cifrado y Descifrado con DES
def des_cifrar_descifrar():
    key, iv, mensaje = solicitar_datos()
    cipher = DES.new(key, DES.MODE_CBC, iv)
    mensaje_cifrado = cipher.encrypt(pad(mensaje, DES.block_size))
    print("--------------------------------------")
    print(f"\033[92mTexto cifrado (DES): {mensaje_cifrado.hex()}\033[0m")
    
    cipher_dec = DES.new(key, DES.MODE_CBC, iv)
    mensaje_descifrado = unpad(cipher_dec.decrypt(mensaje_cifrado), DES.block_size)
    print(f"\033[92mTexto descifrado (DES): {mensaje_descifrado.decode()}\033[0m")

if __name__ == "__main__":
    des_cifrar_descifrar()
