import json

import pytest

from somemart.models import Item, Review


class TestViews(object):

    def test_post_item(self, client, db):
        """/api/v1/goods/ (POST) сохраняет товар в базе."""
        url = '/api/v1/goods/'
        data = json.dumps({
            'title': 'Сыр "Российский"',
            'description': 'Очень вкусный сыр, да еще и российский.',
            'price': 100
        })
        response = client.post(url, data=data, content_type='application/json')
        assert response.status_code == 201
        document = response.json()
        # Объект был сохранен в базу
        item = Item.objects.get(pk=document['id'])
        assert item.title == 'Сыр "Российский"'
        assert item.description == 'Очень вкусный сыр, да еще и российский.'
        assert item.price == 100

    # def test_post_review(self, client, db):
        """/api/v1/goods/:id/reviews/ (POST) создать отзыв к товару :id - сохраняет отзыв в базе."""
        url = '/api/v1/goods/1/reviews/'
        data = json.dumps({
            "text": "Best. Cheese. Ever.",
            "grade": 9
        })
        response = client.post(url, data=data, content_type='application/json')
        assert response.status_code == 201
        document = response.json()
        # Объект был сохранен в базу
        review = Review.objects.get(pk=document['id'])
        assert review.text == 'Best. Cheese. Ever.'
        assert review.grade == 9

    # def test_get_item(self, client, db):
        """/api/v1/goods/:id/ (GET) получает товар из базы."""
        url = '/api/v1/goods/1/'

        response = client.get(url)
        assert response.status_code == 200
        document = response.json()
        # Объект был сохранен в базу
        item = Item.objects.get(pk=document['id'])
        review = Review.objects.get(pk=document['id'])
        assert item.title == 'Сыр "Российский"'
        assert item.description == 'Очень вкусный сыр, да еще и российский.'
        assert item.price == 100
        assert review.id == 1
        assert review.grade == 9
        assert review.text == 'Best. Cheese. Ever.'


