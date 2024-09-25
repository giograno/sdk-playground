from localstack.sdk.clients import LocalStackClient


class TestLocalStackClient:
    client = LocalStackClient()

    def test_get_health(self):
        resp = self.client.get_features_and_services()
        assert resp
