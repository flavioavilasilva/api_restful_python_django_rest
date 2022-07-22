import requests

# GET Avalaições
headers = {"Authorization":"token 4a1ac4b4b9fe1307f56fdd83f64af75a8f022a5b"}
avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/', headers=headers)

#status
print(avaliacoes.status_code)

#dictionary
print(avaliacoes.json())
