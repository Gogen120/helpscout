def test_list_teams(test_client):
    response = test_client.team.list()

    assert response
