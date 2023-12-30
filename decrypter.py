import os
import pyaes
import getpass

# inserir caminho do arquivo criptografado
path = input('Digite o caminho do arquivo: ')

# ler o arquivo criptografado
with open(path, "rb") as f:
    file_data = f.read()

# inserir a chave de descriptografia
key = getpass.getpass('\nInsira a CHAVE de descriptografia!\n\nCertifique-se que a CHAVE tenha 16, 24 ou 32 caracteres de comprimento: ').encode('utf-8')

# loop para verificar o comprimento da chave
while True:
    if len(key) not in [16, 24, 32]:
        key = getpass.getpass('\nCHAVE inválida!\n\nCertifique-se que a CHAVE tenha 16, 24 ou 32 caracteres de comprimento! ').encode('utf-8')
    else:
        break

# descriptografar o arquivo
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# remover o arquivo criptografado
os.remove(path)

# criar o arquivo descriptografado
with open(os.path.splitext(path)[0], "wb") as decrypted_f:
    decrypted_f.write(decrypt_data)

print('\nArquivo descriptografado!')