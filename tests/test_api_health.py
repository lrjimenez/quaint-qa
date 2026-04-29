import requests
def test_suite_is_up():
    response = requests.get("https://www.quaintrelle.ai")

    assert response.status_code == 200