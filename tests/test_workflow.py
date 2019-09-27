def test_list_workflows(test_client):
    response = test_client.workflow.list_()

    assert response.ok
    assert response.json()
