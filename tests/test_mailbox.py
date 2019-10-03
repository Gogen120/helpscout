def test_list_mailbox(test_client):
    response = test_client.mailbox.list()

    assert response
