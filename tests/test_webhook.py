def test_lost_webhooks(test_client):
    response = test_client.webhook.list()

    assert response
