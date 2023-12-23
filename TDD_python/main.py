# Test for creating a recipe

from decimal import Decimal


def test_create_recipe(self):
    """ Creating a recipe test"""
    user = get_user_model().objects.create_user(
        'test@example.com',
        'testpass123'
    )
