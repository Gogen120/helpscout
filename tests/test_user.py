def test_list_users(test_client):
    response = test_client.user.list_()

    assert response
