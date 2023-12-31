# Ransomware
- Desafio de Projeto Santander Bootcamp Cibersegurança

## Ferramentas utilizadas:
- Visual Studio Code (editor de código)
- Kali Linux (executar o código)
- pyaes

## Instruções de uso no Terminal do Kali Linux:

- Instale a biblioteca ``` pyaes ``` utilizando o comando:
```bash
pip install pyaes
```
- Faça o clone do repositório:
```bash
git clone https://github.com/fernandeskelvin/cibersecurity-desafio-ransomware
```
- Entre na pasta do repositorio:
```bash
cd cibersecurity-desafio-ransomware
```
- Para verificar se todos os arquivos estão no diretório digite ``` ls ```

- O conteúdo do arquivo antes da criptografia pode ser conferido com o comando:

```bash
nano teste.txt
```
  
![image](https://github.com/fernandeskelvin/cibersecurity-desafio-ransomware/assets/141537115/5b2d87ae-5ec5-4dc6-a484-2abdf1553c8a)

## Criptografar:

- Para criptografar o arquivo ``` teste.txt ``` execute o script ``` encryoter.py ``` utilizando o comando:
```bash
python encrypter.py
```
- Será solicitado o caminho do arquivo a ser criptografado, caso esteja na mesma pasta, basta digitar o nome do arquivo.

- Em seguida insira a chave para criptografar, que deve conter 16, 24 ou 32 dígitos.
  - A senha não será visível ao ser digitada propositalmente.
  - Caso a chave informada não tenha o comprimento de caracteres, será solicitado novamente.

- O arquivo será criptografado e aparecerá com novo nome:

![image](https://github.com/fernandeskelvin/teste_readme/assets/141537115/110d2f4a-7002-4400-82d8-71f53d01c7eb)

- Arquivo criptografado:

![image](https://github.com/fernandeskelvin/cibersecurity-desafio-ransomware/assets/141537115/b9a3656b-cc2f-4638-a0b7-d9c5e5603eeb)

## Descriptografar:

- Para descriptografar o arquivo execute o script ``` decryoter.py ``` utilizando o comando:
```bash
python encrypter.py
```

- O passo a passo para descriptografar é igual ao script de criptografia.

- Para demonstrar como utilizar o script inserindo o caminho do arquivo:

  - Altere o arquivo criptografado de local **(passo não necessário)**
  - Crie uma pasta ``` mkdir -p criptografado ``` mover o arquivo ``` mv teste.txt.ransomwaretroll cripitografado ```
  - Quando for solicitado o caminho informe: ``` criptografado/teste.txt.ransomwaretroll ```

- Ao final o arquivo criptografado será excluído e removido o prefixo adicionado na criptografia:

![image](https://github.com/fernandeskelvin/cibersecurity-desafio-ransomware/assets/141537115/fa56efd1-0af3-473b-a1f8-1573ef7c1bb5)

- Arquivo descriptografado:

![image](https://github.com/fernandeskelvin/cibersecurity-desafio-ransomware/assets/141537115/511a71ec-d249-44c6-b231-495be3a24835)

> [!NOTE]
> - **Este repositório é exclusivamente para fins educacionais.**
> - **O uso deste conteúdo para atividades ilegais é proibido.**
> - **O autor não se responsabiliza por qualquer uso indevido das informações disponibilizadas.**
