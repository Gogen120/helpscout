def test_list_tags(test_client):
    response = test_client.tag.list()

    assert response
