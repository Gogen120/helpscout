def test_lost_teams(test_client):
    response = test_client.team.list()

    assert response
