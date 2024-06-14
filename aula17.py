# python -m pip install requests
import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    data = response.json()

    if "erro" not in data:
        endereco = data["logradouro"]
        bairro = data["bairro"]
        cidade = data["localidade"]
        estado = data["uf"]

        print(f"Endereço: {endereco}\n")
        print(f"Bairro: {bairro}\n")
        print(f"Cidade: {cidade}\n")
        print(f"Estado: {estado}\n")
    else:
        print(f" Endereço não encontrado. Verifique o CEP!\n")

cep = input("Digite o CEP:\n")
consultar_cep(cep)