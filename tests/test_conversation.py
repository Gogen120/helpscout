def test_list_conversation(test_client):
    response = test_client.conversation.list_()

    assert response
