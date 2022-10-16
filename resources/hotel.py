"""
Resource hotel
"""

# External imports
from ast import Delete
from flask_restful import Resource


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

    def get(self, hotel_id):
        
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel

        return {'message': 'Hotel not found'}, 404
    
    def post(self, hotel_id):
        pass

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
