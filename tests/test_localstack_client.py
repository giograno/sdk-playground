from localstack.sdk.clients import LocalStackClient


class TestLocalStackClient:
    client = LocalStackClient()
    def test_get_health(self):
        resp = self.client.get_health()
        assert resp
