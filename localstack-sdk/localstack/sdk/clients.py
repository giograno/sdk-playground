import localstack.generated
from localstack.generated import Configuration
import os


class PodClient:

    def __init__(self, auth_token: str | None = None, host: str = "http://localhost.localstack.cloud:4566"):
        self.auth_token = auth_token or os.getenv("LOCALSTACK_AUTH_TOKEN")
        self.host = host
        assert auth_token




class LocalStackClient():
    configuration: Configuration

    def __init__(self):
        self.configuration = Configuration(host="http://localhost.localstack.cloud:4566")

    def delete_ddb_items(self):
        with localstack.generated.ApiClient(self.configuration) as client:
            api_instance = localstack.generated.AwsApi(client)
            resp = api_instance.delete_ddb_expired_items()
            return resp

    def get_health(self):
        with localstack.generated.ApiClient(self.configuration) as client:
            api_instance = localstack.generated.LocalstackApi(client)
            resp = api_instance.get_features_and_services()
            return resp
