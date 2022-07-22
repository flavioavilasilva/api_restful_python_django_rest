import requests

# GET Avalaições
headers = {"Authorization":"token 4a1ac4b4b9fe1307f56fdd83f64af75a8f022a5b"}
base_url = 'http://127.0.0.1:8000/api/v2/'
data = { "titulo": "CursoY", "url": "https://cursoY.com.br" }
resultado = requests.post(url=base_url + 'cursos/', headers=headers, data=data)

# status do get no sucesso
assert resultado.status_code == 201

# status do get sem passar token
resultado = requests.post(url=base_url + 'cursos/')
assert resultado.status_code == 403

