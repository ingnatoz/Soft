import pytest
from apps.users.models import *


@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user(
        username='Juan',
        email='juan@test.com',
        name='Manuel',
        last_name='last name',
        password='123456789'
    )
    assert user.username == 'Juan'
