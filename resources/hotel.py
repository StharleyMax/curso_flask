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

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def find_hotel(self, hotel_id: str) -> dict:
        """
        find hotel.

        :params hotel_id: id hotel to find.

        :return: hotel dict
        """

        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id: str) -> dict:
        """
        Handle get hotel.

        :params hotel_id: id hotel to find.

        :return: hotel dict
        """

        hotel = self.find_hotel(hotel_id)
        if not hotel:
            return {'message': 'Hotel not found'}, 404
        return hotel
    
    def post(self, hotel_id: str) -> dict:
        """
        Handle post hotel.

        :params hotel_id: id hotel to create.

        :return: hotel dict create
        """

        hotel =  self.find_hotel(hotel_id)
        if hotel:
            return {'message': f'Hotel {hotel_id} already exists'}

        dados = self.argumentos.parse_args()
        novo_hotel = {'hotel_id': hotel_id, **dados}
        hoteis.append(novo_hotel)

        return novo_hotel, 201

    def put(self, hotel_id) -> dict:
        """
        Handle put hotel.

        :params hotel_id: id hotel to update.

        :return: hotel dict update
        """

        hotel = self.find_hotel(hotel_id)
        if not hotel:
            return {'message:': f'Hotel {hotel_id} not exists'}

        dados = self.argumentos.parse_args()
        novo_hotel = {'hotel_id': hotel_id, **dados}
        hotel.update(novo_hotel)

        return novo_hotel, 200

    def delete(self, hotel_id) -> dict:
        """
        Handle delete hotel.

        :params hotel_id: id hotel to delete.

        :return: message of delete.
        """

        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted.'}
