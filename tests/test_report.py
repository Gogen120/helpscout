START = '2019-08-27T12:00:00Z'
END = '2019-09-27T12:00:00Z'
RANGE = 'replies'


def test_chat_report(test_client):
    response = test_client.report.chat_report(START, END)

    assert response.ok
    assert response.json()


def test_email_report(test_client):
    response = test_client.report.email_report(START, END)

    assert response.ok
    assert response.json()


def test_phone_report(test_client):
    response = test_client.report.phone_report(START, END)

    assert response.ok
    assert response.json()


def test_company_overall_report(test_client):
    response = test_client.report.company.overall_report(START, END)

    assert response.ok
    assert response.json()


def test_company_customers_helped(test_client):
    response = test_client.report.company.customers_helped(START, END)

    assert response.ok
    assert response.json()


def test_company_drilldown(test_client):
    response = test_client.report.company.drilldown(START, END, RANGE)

    assert response.ok
    assert response.json()


def test_conversation_overall_report(test_client):
    response = test_client.report.conversation.overall_report(START, END)

    assert response.ok
    assert response.json()


def test_conversation_volumes_by_channel(test_client):
    response = test_client.report.conversation.volumes_by_channel(START, END)

    assert response.ok
    assert response.json()


def test_conversation_busiest_time_of_day(test_client):
    response = test_client.report.conversation.busiest_time_of_day(START, END)

    assert response.ok
    assert response.json()


def test_conversation_drilldown(test_client):
    response = test_client.report.conversation.drilldown(START, END)

    assert response.ok
    assert response.json()


def test_conversation_new(test_client):
    response = test_client.report.conversation.new(START, END)

    assert response.ok
    assert response.json()


def test_conversation_new_drilldown(test_client):
    response = test_client.report.conversation.new_drilldown(START, END)

    assert response.ok
    assert response.json()


def test_conversation_received_messages(test_client):
    response = test_client.report.conversation.received_messages(START, END)

    assert response.ok
    assert response.json()


def test_doc_overall_report(test_client):
    response = test_client.report.doc.overall_report(START, END)

    assert response.ok
    assert response.json()


def test_happiness_overall_report(test_client):
    response = test_client.report.happiness.overall_report(START, END)

    assert response.ok
    assert response.json()


def test_happiness_ratings(test_client):
    response = test_client.report.happiness.ratings(START, END)

    assert response.ok
    assert response.json()


def test_productivity_overall_report(test_client):
    response = test_client.report.productivity.overall_report(START, END)

    assert response.ok
    assert response.json()


def test_productivity_first_response_time(test_client):
    response = test_client.report.productivity.first_response_time(START, END)

    assert response.ok
    assert response.json()


def test_productivity_replies_sent(test_client):
    response = test_client.report.productivity.replies_sent(START, END)

    assert response.ok
    assert response.json()


def test_productivity_resolution_time(test_client):
    response = test_client.report.productivity.resolution_time(START, END)

    assert response.ok
    assert response.json()


def test_productivity_resolved(test_client):
    response = test_client.report.productivity.resolved(START, END)

    assert response.ok
    assert response.json()


def test_productivity_response_time(test_client):
    response = test_client.report.productivity.response_time(START, END)

    assert response.ok
    assert response.json()
