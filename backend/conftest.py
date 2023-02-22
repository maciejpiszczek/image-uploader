import os
import shutil
import pytest
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings

from images.models import Thumbnail, Image
from tiers.models import Tier, Size


@pytest.fixture
def image():
    yield SimpleUploadedFile('test_file.png', content=open(os.path.join('tests', 'test_image.png'), 'rb').read())


@pytest.fixture(scope='function')
def remove_test_data():
    yield
    try:
        shutil.rmtree(os.environ.get('TEST_DIR'))
    except OSError:
        pass


@pytest.fixture()
def api_rf():
    from rest_framework.test import APIRequestFactory
    return APIRequestFactory()


@pytest.fixture(scope='function')
def create_test_size():
    size = Size.objects.create(
        height=200
    )
    return size


@pytest.fixture(scope='function')
def create_test_tier(create_test_size):
    tier = Tier.objects.create(
        name='test tier',
        expiring_links=True
    )
    tier.size.add(create_test_size)
    return tier


@pytest.fixture(scope='function')
def create_test_user(create_test_tier):
    user = get_user_model().objects.create_user(
        username='testuser',
        password='testpass123',
        tier=create_test_tier
    )
    return user


@pytest.fixture(scope='function')
@override_settings(MEDIA_ROOT=(os.environ.get('TEST_DIR') + '/media'))
def create_test_image(create_test_user):
    image = Image.objects.create(
        author=create_test_user,
        url=SimpleUploadedFile('test_file.png',
                               content=open(os.path.join('tests', 'test_image.png'), 'rb').read())
    )
    return image


@pytest.fixture(scope='function')
@override_settings(MEDIA_ROOT=(os.environ.get('TEST_DIR') + '/media'))
def create_test_thumbnail(create_test_image):
    thumbnail = Thumbnail.objects.create(
        image=create_test_image,
        url=SimpleUploadedFile('test_resized_file.png',
                               content=open(os.path.join('tests', 'test_image.png'), 'rb').read()),
        height=200
    )
    return thumbnail


@pytest.fixture(scope='function')
def create_test_thumbnail_serializer_data(create_test_image):
    serializer_data = {
        'image_id': create_test_image.pk,
        'heights': [200]
    }
    return serializer_data
