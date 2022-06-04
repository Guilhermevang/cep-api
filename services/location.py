import sys
import requests
sys.path.append('..')
from src import exceptions

URL = "https://nominatim.openstreetmap.org/search?format=json&addressdetails=1&country=${}&state=${}&city=${}&street=${}&limit=1"

def fetch_location(street, city, state, country = 'Brazil', **kwargs):
  """ Buscar informações de localização pelo endereço """
  try:
    response = requests.get(URL.format(country, state, city, street))
    if response.ok:
      return response.json()

    else:
      return exceptions.NotFound()

  except:
    return exceptions.InternalServerError()

def fetch_coordinates(address):
  """ Buscar coordenadas pelo endereço """
  try:
    response = fetch_location(**address)
    if not hasattr(response, 'error'):
      if len(response) > 0:
        return {
          'latitude': response[0]['lat'],
          'longitude': response[0]['lon'],
        }

      else:
        return exceptions.NotFound()

    else:
      return response

  except:
    return exceptions.InternalServerError()