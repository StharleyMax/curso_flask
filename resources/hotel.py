"""
Resource hotel
"""

# External imports
from flask_restful import Resource, reqparse


hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Goiás'
    },
    {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'estrelas': 4.1,
        'diaria': 410.34,
        'cidade': 'Brasília'
    },
    {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'estrelas': 3.9,
        'diaria': 330.34,
        'cidade': 'São paulo'
    }
]


class Hoteis(Resource):
    """
    Class Hoteis
    """

    def get(self):
        """
        Get all hoteis
        """

        return {'hoteis': hoteis}

class Hotel(Resource):
    """
    Class Hotel
    """

    def get(self, hotel_id) -> dict:
        """
        Handle get hotel.

        :params hotel_id: id hotel to find.

        :return: hotel dict
        """

        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel

        return {'message': 'Hotel not found'}, 404
    
    def post(self, hotel_id) -> dict:
        """
        Handle post hotel.

        :params hotel_id: id hotel to create.

        :return: hotel dict create
        """

        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')

        dados = argumentos.parse_args()
        novo_hotel = {
            'hotel_id': hotel_id,
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade'],
        }

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
