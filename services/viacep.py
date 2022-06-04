import json
import sys
import requests
sys.path.append('..')
from src import exceptions

URL = 'http://www.viacep.com.br/ws/{}/json/'

def fetch_address(cep):
  """ Buscar endereço pelo CEP via API do ViaCEP """
  try:
    if len(cep) != 8 or not cep.isdigit():
      return exceptions.InvalidCep()

    response = requests.get(URL.format(cep))
    if response.ok:
      response = response.json()
      return {
        'cep': response['cep'],
        'street': response['logradouro'],
        'neighborhood': response['bairro'],
        'complement': response['complemento'],
        'city': response['localidade'],
        'state': response['uf'],
        'ibge_code': response['ibge'],
        'ddd': response['ddd'],
        'coordinates': {
          'latitude': None,
          'longitude': None,
        }
      }

    else:
      return exceptions.CepNotFound()
      
  except:
    return exceptions.InternalServerError()