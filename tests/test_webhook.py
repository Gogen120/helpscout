def test_lost_webhooks(test_client):
    response = test_client.webhook.list_()

    assert response.ok
    assert response.json()
