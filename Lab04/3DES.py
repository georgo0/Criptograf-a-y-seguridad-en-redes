from Cryptodome.Cipher import DES3
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

# Función para ajustar clave o IV a 8 bytes
def ajustar_longitud(data, length=8):
    if len(data) < length:
        data += get_random_bytes(length - len(data))
    else:
        data = data[:length]
    return data

# Solicitar datos y ajustar tres claves de 8 bytes y IV
def solicitar_datos():
    k1_hex = input("Ingrese la clave K1 para 3DES en hexadecimal (16 caracteres para 8 bytes): ")
    k2_hex = input("Ingrese la clave K2 para 3DES en hexadecimal (16 caracteres para 8 bytes): ")
    k3_hex = input("Ingrese la clave K3 para 3DES en hexadecimal (16 caracteres para 8 bytes): ")
    iv_hex = input("Ingrese el Vector de Inicialización (IV) para 3DES en hexadecimal (16 caracteres para 8 bytes): ")
    mensaje = input("Ingrese el texto a cifrar: ").encode()

    # Convertir claves e IV de hexadecimal a bytes y ajustar longitud si es necesario
    k1 = ajustar_longitud(bytes.fromhex(k1_hex))
    k2 = ajustar_longitud(bytes.fromhex(k2_hex))
    k3 = ajustar_longitud(bytes.fromhex(k3_hex))
    iv = ajustar_longitud(bytes.fromhex(iv_hex))

    # Concatenar las claves para formar la clave completa de 24 bytes para 3DES
    key = k1 + k2 + k3
    print("--------------------------------------")
    print(f"\033[93mClave ajustada: {key.hex()}\033[0m")
    print(f"\033[93mIV ajustado: {iv.hex()}\033[0m")
    return key, iv, mensaje

# Cifrado y Descifrado con 3DES
def triple_des_cifrar_descifrar():
    key, iv, mensaje = solicitar_datos()
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    mensaje_cifrado = cipher.encrypt(pad(mensaje, DES3.block_size))
    print("--------------------------------------")
    print(f"\033[92mTexto cifrado (3DES): {mensaje_cifrado.hex()}\033[0m")
    
    cipher_dec = DES3.new(key, DES3.MODE_CBC, iv)
    mensaje_descifrado = unpad(cipher_dec.decrypt(mensaje_cifrado), DES3.block_size)
    print(f"\033[92mTexto descifrado (3DES): {mensaje_descifrado.decode()}\033[0m")
    

if __name__ == "__main__":
    triple_des_cifrar_descifrar()