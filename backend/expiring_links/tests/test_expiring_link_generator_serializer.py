from expiring_links.serializers import ExpiringLinkGeneratorSerializer


def test_fields(db, create_test_expiring_link_serializer_data):
    assert list(create_test_expiring_link_serializer_data.keys()) == ['image_id', 'expiration_time']


def test_valid_serializer(db, create_test_expiring_link_serializer_data, create_test_image, create_test_user,
                          remove_test_data):
    serializer = ExpiringLinkGeneratorSerializer(data=create_test_expiring_link_serializer_data,
                                                 context={'user': create_test_user})

    assert serializer.is_valid()


def test_user_without_permission(db, create_test_expiring_link_serializer_data, create_test_image, create_test_user,
                                 remove_test_data):
    create_test_user.tier.expiring_links = False

    serializer = ExpiringLinkGeneratorSerializer(data=create_test_expiring_link_serializer_data,
                                                 context={'user': create_test_user})

    assert not serializer.is_valid()
    assert set(serializer.errors) == {'non_field_errors'}


def test_wrong_image_id(db, create_test_expiring_link_serializer_data, create_test_image, create_test_user,
                        remove_test_data):
    create_test_expiring_link_serializer_data['image_id'] = create_test_image.pk + 1

    serializer = ExpiringLinkGeneratorSerializer(data=create_test_expiring_link_serializer_data,
                                                 context={'user': create_test_user})

    assert not serializer.is_valid()
    assert set(serializer.errors) == {'image_id'}


def test_too_short_expiration_time(db, create_test_expiring_link_serializer_data, create_test_image, create_test_user,
                                   remove_test_data):
    create_test_expiring_link_serializer_data['expiration_time'] = 200

    serializer = ExpiringLinkGeneratorSerializer(data=create_test_expiring_link_serializer_data,
                                                 context={'user': create_test_user})

    assert not serializer.is_valid()
    assert set(serializer.errors) == {'expiration_time'}


def test_too_long_expiration_time(db, create_test_expiring_link_serializer_data, create_test_image, create_test_user,
                                  remove_test_data):
    create_test_expiring_link_serializer_data['expiration_time'] = 40000

    serializer = ExpiringLinkGeneratorSerializer(data=create_test_expiring_link_serializer_data,
                                                 context={'user': create_test_user})

    assert not serializer.is_valid()
    assert set(serializer.errors) == {'expiration_time'}
