def CepNotFound(message='CEP não encontrado'):
  """ Quando o CEP não for encontrado """
  return { 'error': message, 'status': 404 }

def InvalidCep(message='CEP inválido'):
  """ Quando o CEP for inválido """
  return { 'error': message, 'status': 400 }

def InternalServerError(message='Erro interno no servidor'):
  """ Quando ocorrer algum erro interno no servidor """
  return { 'error': message, 'status': 500 }

def NotFound(message='Recurso não encontrado'):
  """ Quando o recurso não for encontrado """
  return { 'error': message, 'status': 404 }