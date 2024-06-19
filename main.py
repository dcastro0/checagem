import requests
import json

def enfeite(): 
  print("-+" * 10)

def getCep():
  cep = input("Digite seu cep: ")
  return cep


def buscar_dados():
  cep = getCep()
  request = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
  data = json.loads(request.content)
  enfeite()
  print('CEP: {}'.format(data['cep']))
  print('Cidade: {}'.format(data['localidade']))
  print('UF: {}'.format(data['uf']))
  if data['logradouro'] != '':
    print('Logradouro: {}'.format(data['logradouro']))
  if data['complemento'] != '':
    print('Complemento: {}'.format(data['complemento']))
  enfeite()


if __name__ == '__main__':
  buscar_dados()