import pytest


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUser', password='1234567'
    )


@pytest.fixture
def user_2(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUser2', password='1234567'
    )


@pytest.fixture
def another_user(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUserAnother', password='1234567'
    )


@pytest.fixture
def token(user):
    from rest_framework_simplejwt.tokens import RefreshToken
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@pytest.fixture
def user_client(token):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')
    return client

import pytest
from api.models import Country, City, UserGeo


@pytest.fixture
def country(db):
    return Country.objects.create(name="Russia")


@pytest.fixture
def city(db, country):
    return City.objects.create(name="Moscow", country=country)


@pytest.fixture
def user_geo(db, user, country, city):
    return UserGeo.objects.create(
        user=user,
        country=country,
        city=city
    )