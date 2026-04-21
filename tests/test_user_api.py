import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_user_has_geo(user, user_geo):
    client = APIClient()

    response = client.get(f'/api/users/{user.id}/')

    assert response.status_code == 200
    assert response.data['geo']['country']['name'] == "Russia"