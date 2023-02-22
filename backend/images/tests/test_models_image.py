from images.models import Image


def test_image_creation(db, create_test_image, create_test_user, remove_test_data):
    assert isinstance(create_test_image, Image)
    assert create_test_image.author == create_test_user
    assert create_test_image.url.url == '/media/images/test_file.png'
    assert create_test_image.name == 'test_file.png'
    assert create_test_image.__str__() == 'test_file.png'


def test_image_fields(db, create_test_image, remove_test_data):
    assert [*create_test_image.__dict__] == ['_state', 'id', 'author_id', 'url', 'name', 'created_at', 'updated_at']
