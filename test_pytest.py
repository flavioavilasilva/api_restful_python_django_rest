import requests

class TestCursos:
    headers = {"Authorization":"token 4a1ac4b4b9fe1307f56fdd83f64af75a8f022a5b"}
    base_url = 'http://127.0.0.1:8000/api/v2/'

    def test_get_cursos(self):
        url = f'{self.base_url}cursos/'
        print(url)
        resultado = requests.get(url=url, headers=self.headers)

        assert resultado.status_code == 200

    def test_get_curso(self):
        url = f'{self.base_url}cursos/5/'
        print(url)
        resultado = requests.get(url=url, headers=self.headers)

        assert resultado.status_code == 200