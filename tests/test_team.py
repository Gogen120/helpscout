def test_lost_teams(test_client):
    response = test_client.team.list_()

    assert response.ok
    assert response.json()
