from tiers.models import Size


def test_size_creation(db, create_test_size):
    assert isinstance(create_test_size, Size)
    assert create_test_size.height == 200
    assert create_test_size.__str__() == '200 px'


def test_size_fields(db, create_test_size):
    assert [*create_test_size.__dict__] == ['_state', 'id', 'height']
