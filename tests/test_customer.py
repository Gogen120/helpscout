def test_list_customers(test_client):
    response = test_client.customer.list()

    assert response
