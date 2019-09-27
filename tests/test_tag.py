def test_list_tags(test_client):
    response = test_client.tag.list_()

    assert response.ok
    assert response.json()
