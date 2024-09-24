from localstack.sdk.clients import LocalStackClient


def test_get_health():
    client = LocalStackClient()
    resp = client.get_health()
    print(resp)
    assert resp
