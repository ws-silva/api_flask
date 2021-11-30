from flask import Flask
from flask_restx import Resource
from src.server.instance import server

app = server.app
api = server.api

dados_bd = [
    {'id': 0, 'title': 'Pegasus'},
    {'id': 1, 'title': 'Clean Code'}
]

@api.route('/books/<int:id>')
class LivroLista(Resource):
    def get(self, id):
        return dados_bd[id]
    
    
    def put(self, id):
        response = api.payload
        dados_bd[id]['title'] = response['title']
        return response, 200


@api.route('/novobook/')
class CriarLivro(Resource):
    def post(self):
        response = api.payload
        dados_bd.append(response)
        return response, 200