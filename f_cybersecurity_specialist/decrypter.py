import os
import pyaes

# abrir o arquivo criptografado.
file_name = "teste.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

#chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
descrypt_data = aes.decrypet(file_data)

#remover o arquivo criptogradado
os.remove(file_name)

#criar o arquivo descriptografado
new_file = "teste.txt"
new_file = open(f'{new_file}' "wb")
new_file.write(descrypt_data)
new_file.close()

