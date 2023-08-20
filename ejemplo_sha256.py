import hashlib

def sha256_hash(message):
    # Crear un objeto hash SHA-256
    sha256_hasher = hashlib.sha256()

    # Convertir el mensaje a bytes (ya que hashlib trabaja con bytes)
    message_bytes = message.encode('utf-8')

    # Actualizar el objeto hash con los bytes del mensaje
    sha256_hasher.update(message_bytes)

    # Calcular el hash en formato hexadecimal
    hash_result = sha256_hasher.hexdigest()

    return hash_result

# Mensaje de ejemplo
message = "Hola, este es un mensaje de ejemplo."

# Obtener el hash SHA-256 del mensaje
hash_value = sha256_hash(message)

# Imprimir el resultado
print(f"Mensaje: {message}")
print(f"Hash SHA-256: {hash_value}")
